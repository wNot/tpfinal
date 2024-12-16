from sqlalchemy import Column, Integer, String, Boolean, Datetime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class Cancha(Base):
    __tablename__= "canchas"
    id = Column(Integer,primary_key=True,index=True)
    nombre = Column(String, unique=True,nullable=False)
    techada = Column(Boolean, default=False)
    reservas = relationship("Reserva",back_populates="cancha")

class Reserva(Base):
    __tablename__= "reservas"
    id = Column(Integer,primary_key=True,index=True)
    cancha_id = Column(Integer, ForeignKey("canchas.id"),nullable=False)
    dia = Column(Datetime, nullable=False)
    duracion = Column(Integer, nullable=False)
    contacto_nombre = Column(String,nullable=False)
    contacto_telefono = Column(String, nullable=False)
    cancha = relationship("Cancha",back_populates="reservas")

