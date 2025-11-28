# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview
This is a backend API built with FastAPI that provides user authentication with JWT and item inventory management. The application uses SQLite for data persistence and includes a complete REST API for managing users and inventory items.

## Specific Features Implemented
- User registration and authentication using JWT tokens
- Password hashing with bcrypt
- CRUD operations for inventory items
- Role-based access control
- SQLite database with SQLAlchemy ORM
- Pydantic validation for request/response data

## Common Development Commands

### Starting the Development Server
```bash
# Using the startup script
./start.sh

# Or directly with uvicorn
uvicorn app.main:app --reload

# With virtual environment
source venv/bin/activate
uvicorn app.main:app --reload
```

### Running Tests
```bash
# Run all tests
source venv/bin/activate
python -m pytest tests/

# Run a specific test file
python -m pytest tests/test_main.py
```

### Installing Dependencies
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install production dependencies
pip install -r requirements.txt

# Install development dependencies
pip install -r requirements-dev.txt
```

### Building and Deployment
```bash
# Build Docker image
docker build -t fastapi-inventory-app .

# Run with Docker
docker run -p 8000:8000 fastapi-inventory-app

# Run with docker-compose
docker-compose up --build
```

## Project Structure
```
app/
├── main.py          # Application entry point
├── models/          # Database models (user.py, item.py)
├── schemas/         # Pydantic schemas (user.py, item.py, token.py)
├── routers/         # API route definitions (auth.py, users.py, items.py)
├── core/            # Core configuration and security (config.py, security.py, dependencies.py)
├── database/        # Database connection and session management (database.py, init_db.py)
├── crud/            # CRUD operations (user.py, item.py)
└── utils/           # Utility functions

tests/
├── test_main.py     # Tests for main application

requirements.txt       # Production dependencies
requirements-dev.txt   # Development dependencies
Dockerfile             # Docker configuration
docker-compose.yml     # Multi-container Docker applications
start.sh               # Startup script
```

## API Endpoints

### Authentication
- `POST /register` - Register a new user
- `POST /token` - Obtain an access token

### Users
- `GET /users/me/` - Get current user information
- `GET /users/{user_id}` - Get a specific user
- `PUT /users/me/` - Update current user

### Items
- `POST /items/` - Create a new item (authenticated)
- `GET /items/` - Get all items
- `GET /items/{item_id}` - Get a specific item
- `PUT /items/{item_id}` - Update a specific item (owner only)
- `DELETE /items/{item_id}` - Delete a specific item (owner only)

## Key Dependencies
- FastAPI (0.104.1): Web framework
- Uvicorn (0.24.0): ASGI server
- SQLAlchemy (2.0.23): ORM for database interactions
- Pydantic (2.5.0): Data validation and settings management
- python-jose (3.3.0): JWT token handling
- passlib (1.7.4): Password hashing
- Alembic (1.13.1): Database migration tool

## Database Initialization
The database is automatically initialized when the application starts. The SQLite database file is created as `test.db` in the project root directory.

## Security Notes
- JWT tokens are configured with a 30-minute expiration time
- Passwords are hashed using bcrypt before storage
- CORS is not configured by default but can be added in `main.py`
- Secret keys should be changed in production environments