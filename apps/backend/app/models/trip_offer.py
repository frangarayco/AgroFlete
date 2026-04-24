import uuid
from sqlalchemy import Column, String, Float, ForeignKey, DateTime, Enum
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.models.base import Base
import enum

class OfferStatus(str, enum.Enum):
    pending = "pending"
    accepted = "accepted"
    rejected = "rejected"
    withdrawn = "withdrawn"

class TripOffer(Base):
    __tablename__ = "trip_offers"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    trip_id = Column(String, ForeignKey("trips.id"), nullable=False)
    transporter_id = Column(String, ForeignKey("users.id"), nullable=False)
    vehicle_id = Column(String, ForeignKey("vehicles.id"), nullable=False)
    
    price_offered = Column(Float, nullable=False)
    status = Column(Enum(OfferStatus), nullable=False, default=OfferStatus.pending)
    
    notes = Column(String, nullable=True)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    trip = relationship("Trip", back_populates="offers")
    transporter = relationship("User", back_populates="offers")
    vehicle = relationship("Vehicle", back_populates="offers")
