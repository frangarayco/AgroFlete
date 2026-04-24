import uuid
from sqlalchemy import Column, String, ForeignKey, DateTime, Enum, Date
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.models.base import Base
import enum

class DocType(str, enum.Enum):
    rut_senasa = "rut_senasa"
    dta_senasa = "dta_senasa"
    disinfection_cert = "disinfection_cert"
    vehicle_insurance = "vehicle_insurance"
    driver_license = "driver_license"
    cuit_constance = "cuit_constance"

class DocStatus(str, enum.Enum):
    pending = "pending"
    approved = "approved"
    rejected = "rejected"
    expired = "expired"

class Document(Base):
    __tablename__ = "documents"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    
    # Puede pertenecer a un usuario (registro) o a un vehículo específico
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    vehicle_id = Column(String, ForeignKey("vehicles.id"), nullable=True)
    trip_id = Column(String, ForeignKey("trips.id"), nullable=True) # Para remitos o DTA específicos de un viaje
    
    doc_type = Column(Enum(DocType), nullable=False)
    status = Column(Enum(DocStatus), nullable=False, default=DocStatus.pending)
    
    file_url = Column(String, nullable=False)
    document_number = Column(String, nullable=True)
    expiration_date = Column(Date, nullable=True)
    
    notes = Column(String, nullable=True) # Razón de rechazo por ejemplo
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    user = relationship("User", back_populates="documents")
    vehicle = relationship("Vehicle", back_populates="documents")
    trip = relationship("Trip", back_populates="documents")
