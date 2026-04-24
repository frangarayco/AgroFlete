import sys
import os

# Agregamos la ruta raíz al path para que Python encuentre 'app'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.db.session import engine
from app.models.base import Base

# Importamos explícitamente los modelos para que SQLAlchemy los reconozca y los cree
from app.models.user import User
from app.models.trip import Trip
from app.models.vehicle import Vehicle
from app.models.document import Document
from app.models.trip_offer import TripOffer

def init_db():
    print("⏳ Conectando a Supabase, eliminando tablas viejas y creando el nuevo esquema...")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    print("✅ ¡Tablas creadas con éxito!")

if __name__ == "__main__":
    init_db()
