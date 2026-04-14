from fastapi import FastAPI
from routes import credit, debit, tin

app = FastAPI(title="Kashio Internal System")

app.include_router(credit.router, prefix="/credit")
app.include_router(debit.router, prefix="/debit")
app.include_router(tin.router, prefix="/tin")
