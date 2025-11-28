# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview
This is a backend API built with FastAPI, a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.

## Common Development Commands

### Starting the Development Server
```bash
uvicorn app.main:app --reload
```

### Running Tests
```bash
# Run all tests
pytest

# Run a specific test file
pytest tests/test_users.py

# Run tests with coverage
pytest --cov=app tests/
```

### Linting and Formatting
```bash
# Run linter
flake8 .

# Run formatter
black .

# Run both
black . && flake8 .
```

### Building and Deployment
```bash
# Install dependencies
pip install -r requirements.txt

# Install for development
pip install -r requirements-dev.txt

# Build Docker image
docker build -t my-fastapi-app .

# Run with Docker
docker run -p 8000:8000 my-fastapi-app
```

## Project Structure
```
app/
├── main.py          # Application entry point
├── models/          # Database models
├── schemas/         # Pydantic schemas for request/response validation
├── routers/         # API route definitions
├── core/            # Core configuration and security
├── database/        # Database connection and session management
├── crud/            # CRUD operations
└── utils/           # Utility functions

tests/
├── conftest.py      # Test configuration and fixtures
├── test_main.py     # Tests for main application
└── test_routers/    # Tests for individual routers

requirements.txt       # Production dependencies
requirements-dev.txt   # Development dependencies
Dockerfile             # Docker configuration
docker-compose.yml     # Multi-container Docker applications
```

## Architecture Overview

### Entry Point (main.py)
- Creates the FastAPI application instance
- Includes routers from the routers directory
- Configures middleware, CORS, and exception handlers

### Routers
- Define API endpoints grouped by resource (users, items, etc.)
- Handle HTTP methods (GET, POST, PUT, DELETE)
- Use dependency injection for authentication and database sessions

### Models
- SQLAlchemy ORM models representing database tables
- Define relationships between entities
- Include methods for database operations

### Schemas
- Pydantic models for request/response validation
- Data serialization and deserialization
- Type hints for improved developer experience

### Database Layer
- Database session management
- Connection pooling
- Migration scripts (if using Alembic)

### Core Configuration
- Environment variable management
- Security settings (JWT, password hashing)
- Application settings and constants

## Testing Approach
- Unit tests for individual functions
- Integration tests for API endpoints
- Fixtures for database setup and teardown
- Mock external services when appropriate

## Key Dependencies
- FastAPI: Web framework
- Uvicorn: ASGI server
- SQLAlchemy: ORM for database interactions
- Pydantic: Data validation and settings management
- Pytest: Testing framework
- Alembic: Database migration tool (if applicable)