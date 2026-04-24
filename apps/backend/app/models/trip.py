import uuid
from sqlalchemy import Column, String, Float, DateTime, Enum, ForeignKey, Text, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.models.base import Base
import enum

class PaymentStatus(str, enum.Enum):
    pending = "pending"
    advance_paid = "advance_paid"
    completed = "completed"

class TripStatus(str, enum.Enum):
    pending = "pending"
    matched = "matched"
    in_progress = "in_progress"
    completed = "completed"
    cancelled = "cancelled"

class CargoType(str, enum.Enum):
    hacienda = "hacienda"
    granos = "granos"
    frutas = "frutas"
    otro = "otro"

class Trip(Base):
    __tablename__ = "trips"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    
    # Relaciones con usuarios y activos
    requester_id = Column(String, ForeignKey("users.id"), nullable=False)
    transporter_id = Column(String, ForeignKey("users.id"), nullable=True)
    vehicle_id = Column(String, ForeignKey("vehicles.id"), nullable=True)
    
    status = Column(Enum(TripStatus), nullable=False, default=TripStatus.pending)
    payment_status = Column(Enum(PaymentStatus), nullable=False, default=PaymentStatus.pending)
    cargo_type = Column(Enum(CargoType), nullable=False)
    cargo_details = Column(JSON, nullable=True)
    
    # Origen
    origin_address = Column(String, nullable=False)
    origin_lat = Column(Float, nullable=False)
    origin_lng = Column(Float, nullable=False)
    
    # Destino
    dest_address = Column(String, nullable=False)
    dest_lat = Column(Float, nullable=False)
    dest_lng = Column(Float, nullable=False)
    
    scheduled_date = Column(DateTime(timezone=True), nullable=False)
    estimated_weight = Column(Float, nullable=False) # En kg
    estimated_distance = Column(Float, nullable=True) # En km
    
    # Financiero
    agreed_price = Column(Float, nullable=True)
    commission_rate = Column(Float, nullable=False, default=0.12) # 12% por defecto
    
    notes = Column(Text, nullable=True)
    
    started_at = Column(DateTime(timezone=True), nullable=True)
    completed_at = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Referencias ORM (Bidireccionales correctas)
    requester = relationship("User", foreign_keys=[requester_id], back_populates="requested_trips")
    transporter = relationship("User", foreign_keys=[transporter_id], back_populates="transported_trips")
    vehicle = relationship("Vehicle", foreign_keys=[vehicle_id], back_populates="trips")
    offers = relationship("TripOffer", back_populates="trip", cascade="all, delete-orphan")
    documents = relationship("Document", back_populates="trip", cascade="all, delete-orphan")
