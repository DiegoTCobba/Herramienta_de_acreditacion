from fastapi import APIRouter
from services.parser_service import extraer_tins

router = APIRouter()

@router.post("/")
def tin(data: dict):
    texto = data.get("texto", "")
    tins = extraer_tins(texto)
    return {"tins": tins}
