# Simple test to verify the app can be imported without errors
from app.main import app

def test_app_import():
    assert app is not None
    assert app.title == "Inventory Management API"
    assert app.version == "1.0.0"