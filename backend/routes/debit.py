from fastapi import APIRouter
from services.kashio_service import ejecutar_debito

router = APIRouter()

@router.post("/")
def debit(data: dict):
    return ejecutar_debito(data)
