# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview
This is a backend API built with FastAPI that provides user authentication with JWT and item inventory management. The application uses SQLite for data persistence and includes a complete REST API for managing users and inventory items.

## Architecture Overview
The application follows a modular architecture pattern with clear separation of concerns:

- **main.py**: Entry point that initializes the database and sets up the FastAPI application
- **models/**: SQLAlchemy ORM models defining the database schema (User and Item)
- **schemas/**: Pydantic models for request/response validation
- **routers/**: API endpoint definitions organized by feature (auth, users, items)
- **crud/**: Database operations abstracted into reusable functions
- **core/**: Security utilities, configuration, and dependency injection
- **database/**: Database connection setup and session management
- **tests/**: Unit tests using pytest

The application uses dependency injection for database sessions and follows FastAPI best practices for asynchronous request handling.

## Specific Features Implemented
- User registration and authentication using JWT tokens
- Password hashing with bcrypt
- CRUD operations for inventory items
- Role-based access control
- SQLite database with SQLAlchemy ORM
- Pydantic validation for request/response data
- Health check endpoints
- Automated database initialization

## Common Development Commands

### Setting Up the Development Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies (testing, linting, formatting)
pip install -r requirements-dev.txt
```

### Starting the Development Server
```bash
# Using the startup script
./start.sh

# Or directly with uvicorn
uvicorn app.main:app --reload

# With virtual environment activated
source venv/bin/activate
uvicorn app.main:app --reload
```

### Running Tests
```bash
# Run all tests
source venv/bin/activate
python -m pytest tests/

# Run tests with coverage
python -m pytest --cov=app tests/

# Run a specific test file
python -m pytest tests/test_main.py

# Run tests in verbose mode
python -m pytest -v tests/
```

### Code Quality and Formatting
```bash
# Format code with Black
black .

# Check for linting issues with Flake8
flake8 .

# Run both formatting and linting
black . && flake8 .
```

### Installing Dependencies
```bash
# Install production dependencies
pip install -r requirements.txt

# Install development dependencies
pip install -r requirements-dev.txt

# Add a new dependency
pip install package_name
pip freeze > requirements.txt  # Update requirements file
```

### Database Operations
```bash
# The database is automatically initialized when the application starts
# No manual database setup is required

# To reset the database, delete the test.db file
rm test.db
```

### Building and Deployment

#### Docker Deployment
```bash
# Build Docker image
docker build -t fastapi-inventory-app .

# Run with Docker
docker run -p 8000:8000 fastapi-inventory-app

# Run with docker-compose
docker-compose up --build
```

#### Manual Deployment
```bash
# Production deployment with uvicorn
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

## Project Structure
```
app/
├── main.py              # Application entry point
├── models/              # Database models (user.py, item.py)
├── schemas/             # Pydantic schemas (user.py, item.py, token.py)
├── routers/             # API route definitions (auth.py, users.py, items.py)
├── core/                # Core configuration and security (config.py, security.py, dependencies.py)
├── database/            # Database connection and session management (database.py, init_db.py)
├── crud/                # CRUD operations (user.py, item.py)
└── utils/               # Utility functions (currently empty)

tests/
├── test_main.py         # Tests for main application endpoints

requirements.txt         # Production dependencies
requirements-dev.txt     # Development dependencies (testing, linting)
Dockerfile               # Docker configuration
docker-compose.yml       # Multi-container Docker applications
start.sh                 # Startup script
README.md                # Project documentation
```

## API Endpoints

### Authentication
- `POST /v1/register` - Register a new user
- `POST /v1/token` - Obtain an access token

### Health Check
- `GET /` - Welcome message
- `GET /health` - Health status check
- `GET /v1` - Welcome message for v1 API

### Users
- `GET /v1/users/me/` - Get current user information
- `GET /v1/users/{user_id}` - Get a specific user
- `PUT /v1/users/me/` - Update current user

### Items
- `POST /v1/items/` - Create a new item (authenticated)
- `GET /v1/items/` - Get all items
- `GET /v1/items/{item_id}` - Get a specific item
- `PUT /v1/items/{item_id}` - Update a specific item (owner only)
- `DELETE /v1/items/{item_id}` - Delete a specific item (owner only)

## Key Dependencies
- FastAPI (0.104.1): Web framework with automatic API documentation
- Uvicorn (0.24.0): ASGI server for running the application
- SQLAlchemy (2.0.23): ORM for database interactions
- Pydantic (2.5.0): Data validation and settings management
- python-jose (3.3.0): JWT token handling with cryptographic support
- passlib (1.7.4): Password hashing with bcrypt
- python-multipart (0.0.6): Support for multipart/form-data
- Alembic (1.13.1): Database migration tool
- pytest (7.4.3): Testing framework
- black (23.11.0): Code formatter
- flake8 (6.1.0): Code linter

## Database Design
The application uses SQLite for simplicity, with two main tables:

1. **Users Table**: Stores user account information
   - id: Primary key
   - email: Unique email address
   - hashed_password: Bcrypt-hashed password
   - is_active: Boolean flag for account status
   - created_at: Timestamp of account creation

2. **Items Table**: Stores inventory items
   - id: Primary key
   - title: Item name/title
   - description: Optional item description
   - owner_id: Foreign key to Users table
   - created_at: Timestamp of item creation

## Security Implementation
- JWT tokens with 30-minute expiration time (configurable)
- Passwords hashed using bcrypt before storage
- Token-based authentication for protected endpoints
- CORS is not configured by default but can be added in `main.py`
- Secret keys should be changed in production environments (configured in `core/config.py`)

## Configuration
Environment variables can be set in a `.env` file. The application uses pydantic-settings for configuration management:

- `SECRET_KEY`: JWT signing key (change in production)
- `ALGORITHM`: JWT algorithm (defaults to HS256)
- `ACCESS_TOKEN_EXPIRE_MINUTES`: Token expiration time (defaults to 30 minutes)

## Testing
Tests are implemented using pytest and FastAPI's TestClient. The test suite currently covers:
- Root endpoint availability
- Health check endpoint
- Basic API functionality

To expand test coverage, add new test functions in `tests/test_main.py` following the existing patterns.

## API Documentation
When the server is running, interactive API documentation is available at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

These documentation interfaces allow for testing API endpoints directly from the browser.