from sqlalchemy.orm import Session
from . import model,schemes
from datetime import datetime, timedelta

def get_cancha(db:Session):
    return db.query(model.Cancha).all()

def get_reserva(db:Session,cancha_id:int,dia:datetime):
    return db.query(model.Reserva).filter(model.Reserva.cancha_id==cancha_id,
                                          model.Reserva.dia>=dia,
                                          model.Reserva.dia<dia+timedelta(days=1)).all()

def crear_cancha(db:Session,cancha:schemes.CrearCancha):
    db_cancha=model.Cancha(**cancha.model_dump())
    db.add(db_cancha)
    db.commit()
    db.refresh(db_cancha)
    return db_cancha

def crear_reserva(db:Session,reserva:schemes.CrearReserva):
    reservas = get_reserva(db,reserva.cancha_id,reserva.dia)
    for r in reservas:
        if not(reserva.dia+timedelta(hours=reserva.duracion)<=r.dia+timedelta(hours=r.duracion)):
            raise ValueError("Horario o cancha no disponible")
    db_reserva=model.Reserva(**reserva.model_dump())
    db.add(db_reserva)
    db.commit()
    db.refresh()
    return db_reserva