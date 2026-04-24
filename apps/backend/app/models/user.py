import uuid
from sqlalchemy import Column, String, Boolean, DateTime, Enum, Float
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.models.base import Base
import enum

class UserRole(str, enum.Enum):
    admin = "admin"
    transporter = "transporter"
    requester = "requester"

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    # En Supabase, guardaremos el ID que viene de Supabase Auth
    auth_id = Column(String, unique=True, nullable=True, index=True)
    
    email = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    role = Column(Enum(UserRole), nullable=False, default=UserRole.requester)
    
    # Perfil público
    avatar_url = Column(String, nullable=True)
    rating = Column(Float, nullable=True, default=0.0)
    is_verified = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    
    # Identificación comercial
    tax_id = Column(String, nullable=True) # CUIT/CUIL
    company_name = Column(String, nullable=True) # Razón social
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relaciones
    vehicles = relationship("Vehicle", back_populates="owner", cascade="all, delete-orphan")
    documents = relationship("Document", back_populates="user", cascade="all, delete-orphan")
    offers = relationship("TripOffer", back_populates="transporter", cascade="all, delete-orphan")
    
    # Viajes
    requested_trips = relationship("Trip", back_populates="requester", foreign_keys="[Trip.requester_id]")
    transported_trips = relationship("Trip", back_populates="transporter", foreign_keys="[Trip.transporter_id]")
