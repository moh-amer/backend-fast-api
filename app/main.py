from fastapi import FastAPI
from app.database.init_db import init_db
from app.api.v1 import auth, users, items

# Initialize database
init_db()

app = FastAPI(title="Inventory Management API", version="1.0.0")

# Include routers with v1 prefix
app.include_router(auth.router, prefix="/v1")
app.include_router(users.router, prefix="/v1")
app.include_router(items.router, prefix="/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Inventory Management API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/v1")
def read_v1_root():
    return {"message": "Welcome to the Inventory Management API v1"}