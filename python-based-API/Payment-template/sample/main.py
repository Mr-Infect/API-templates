from fastapi import FastAPI
from app.routes.payment_routes import router as payment_router

app = FastAPI(title="Payment API Template")
app.include_router(payment_router)

@app.get("/")
def root():
    return {"message": "Welcome to the Python Payment API Template"}
