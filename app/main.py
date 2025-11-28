from fastapi import FastAPI, responses
from fastapi.staticfiles import StaticFiles
from app.database.init_db import init_db
from app.api.v1 import auth, users, items

# Initialize database
init_db()

app = FastAPI(
    title="Inventory Management API",
    version="1.0.0",
    redoc_url=None  # Disable default ReDoc only
)

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Custom ReDoc endpoint
@app.get("/redoc", include_in_schema=False)
async def custom_redoc():
    return responses.HTMLResponse("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>ReDoc</title>
        <meta charset="utf-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <body>
        <redoc spec-url="/openapi.json"></redoc>
        <script src="/static/redoc.standalone.js"> </script>
    </body>
    </html>
    """)

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