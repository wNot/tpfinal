from pydantic import BaseModel
from datetime import datetime

#

class CanchaBase(BaseModel):
    nombre: str
    techada: bool

class CrearCancha(CanchaBase):
    pass

class Cancha(CanchaBase):
    id: int
    class config:
        orm_mode=True

class ReservaBase(BaseModel):
    dia: datetime
    duracion: int
    contacto_nombre: str
    contacto_telefono: str

class CrearReserva(ReservaBase):
    cancha_id: int

class Reserva(ReservaBase):
    id: int
    cancha: Cancha
    class config:
        orm_mode=True