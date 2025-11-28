from fastapi import FastAPI
from app.database.init_db import init_db
from app.routers import auth, users, items

# Initialize database
init_db()

app = FastAPI(title="Inventory Management API", version="1.0.0")

# Include routers
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(items.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Inventory Management API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}