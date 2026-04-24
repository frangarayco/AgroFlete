from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# En Supabase necesitamos usar un connection pooler a veces, pero para el backend de FastAPI
# solemos conectarnos por el pooler de Session (puerto 6543)
# Ajustamos si la URL viene con algo distinto a postgresql://
DB_URL = settings.SUPABASE_DB_URL.replace("postgres://", "postgresql://")

engine = create_engine(
    DB_URL,
    pool_pre_ping=True, # Verifica que la conexión está viva
    pool_size=5,
    max_overflow=10
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
