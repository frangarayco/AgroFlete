import uuid
import enum
from sqlalchemy import Column, String, Float, Integer, ForeignKey, DateTime, Enum, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.models.base import Base

class VehicleType(str, enum.Enum):
    jaula = "jaula"
    tolva = "tolva"
    chasis = "chasis"
    acoplado = "acoplado"
    playo = "playo"
    otro = "otro"

class VehicleStatus(str, enum.Enum):
    available = "available"
    in_trip = "in_trip"
    maintenance = "maintenance"
    inactive = "inactive"

class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    owner_id = Column(String, ForeignKey("users.id"), nullable=False)
    
    license_plate = Column(String, unique=True, nullable=False, index=True)
    trailer_license_plate = Column(String, nullable=True) # Para acoplados
    
    brand = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    
    # Especificaciones
    max_weight_capacity = Column(Float, nullable=False) # En kg
    vehicle_type = Column(Enum(VehicleType), nullable=False)
    
    status = Column(Enum(VehicleStatus), nullable=False, default=VehicleStatus.available)
    is_active = Column(Boolean, default=True)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    owner = relationship("User", back_populates="vehicles")
    documents = relationship("Document", back_populates="vehicle", cascade="all, delete-orphan")
    offers = relationship("TripOffer", back_populates="vehicle", cascade="all, delete-orphan")
    trips = relationship("Trip", back_populates="vehicle")
