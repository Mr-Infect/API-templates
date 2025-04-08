from fastapi import FastAPI
from .database import Base, engine
from .routes import auth_routes
from .auth.oauth_auth import router as oauth_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Auth Template")
app.include_router(auth_routes.router)
app.include_router(oauth_router)

@app.get("/")
def root():
    return {"message": "API Auth Template Running"}
