# FastAPI Inventory Management System

A backend API built with Python FastAPI that provides user authentication with JWT and item inventory management.

## Features

- User registration and authentication with JWT
- CRUD operations for inventory items
- Secure API endpoints with role-based access control

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   For development:
   ```bash
   pip install -r requirements-dev.txt
   ```

## Running the Application

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.

## API Documentation

Once the server is running, you can access:

- Interactive API documentation: `http://localhost:8000/docs`
- Alternative API documentation: `http://localhost:8000/redoc`

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
```

## Authentication

1. Register a new user with `/register`
2. Obtain an access token with `/token`
3. Use the token in the Authorization header for protected endpoints

## Endpoints

### Authentication
- `POST /register` - Register a new user
- `POST /token` - Obtain an access token

### Users
- `GET /users/me/` - Get current user information
- `GET /users/{user_id}` - Get a specific user
- `PUT /users/me/` - Update current user

### Items
- `POST /items/` - Create a new item
- `GET /items/` - Get all items
- `GET /items/{item_id}` - Get a specific item
- `PUT /items/{item_id}` - Update a specific item
- `DELETE /items/{item_id}` - Delete a specific item