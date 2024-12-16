from fastapi import APIRouter, Depends, HTTPException
#Apirouter: construir endpoints
#Httpexception: excepciones
#Depends: dependencias de apis
from sqlalchemy.orm import Session
#ORM: intermediario entre la bdd y mi backend
from .. import schemes,crud
from ..database import SessionLocal
from datetime import datetime


router= APIRouter()


def get_db():
    db= SessionLocal()
    try:
        yield db            #yield: verifica si existe una sesion local a la bdd
    finally:
        db.close()          #cierra la sesion local a la bdd



@router.post('/canchas/',response_model=schemes.Cancha)
#Construye la url o endpoint que vamos a utilizar en React para crear una cancha

def CrearCancha(cancha:schemes.CrearCancha,db:Session=Depends(get_db)):
    return crud.crear_cancha(db,cancha)
    #el Depends llama a la funcion get_db para verificar la sesion local
    #el return va al archivo crud, trae crear cancha, le enviamos la conexion a la bdd y la cancha que estamos creando


@router.post('/reservas/',response_model=schemes.Reserva)

def CrearReserva(reserva:schemes.CrearReserva,db:Session=Depends(get_db)):
    try:
        return crud.crear_reserva(db,reserva)
    except ValueError as e:
        raise HTTPException(status_code=400,detail=str(e))

@router.get('/canchas/',response_model=list[schemes.Cancha])

def GetCancha(db:Session=Depends(get_db)):
    return crud.get_cancha(db)

@router.get('/reservas/',response_model=list[schemes.Reserva])

def GetReserva(db:Session=Depends(get_db), cancha_id: int=None, dia: datetime=None):
    try:
        if cancha_id and dia:
            return crud.get_reserva(db,cancha_id=cancha_id,dia=dia)
        else:
            raise HTTPException(status_code=400, detail=str("No se encontró la Reserva"))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

