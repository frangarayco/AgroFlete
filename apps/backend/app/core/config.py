import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "AgroFlete API"
    ENVIRONMENT: str = "development"
    
    # Base de Datos
    SUPABASE_DB_URL: str
    
    # Supabase (Auth / Storage)
    SUPABASE_URL: str = ""
    SUPABASE_KEY: str = ""

    model_config = SettingsConfigDict(
        env_file=".env.local" if os.path.exists(".env.local") else ".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()
