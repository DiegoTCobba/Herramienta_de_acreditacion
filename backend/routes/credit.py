from fastapi import APIRouter
from services.kashio_service import ejecutar_credito

router = APIRouter()

@router.post("/")
def credit(data: dict):
    return ejecutar_credito(data)
