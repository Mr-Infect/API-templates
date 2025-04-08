from fastapi import FastAPI
from app.database import Base, engine
from app.routes import item_routes

Base.metadata.create_all(bind=engine)

app = FastAPI(title="CRUD API Template")
app.include_router(item_routes.router)

@app.get("/")
def root():
    return {"message": "CRUD Template Running"}
