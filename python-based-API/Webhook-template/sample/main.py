from fastapi import FastAPI
from app.routes import webhook_routes
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Webhook API Template")
app.include_router(webhook_routes.router)

@app.get("/")
def root():
    return {"message": "Webhook Receiver Live"}
