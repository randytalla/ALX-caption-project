# ALX-caption-project
E-commerce API

This is a RESTful API built with Django and Django REST Framework (DRF) for an e-commerce platform. It provides endpoints for user management (registration, login, logout, profile) and product management (CRUD operations with searching, filtering, and pagination). The API uses JWT authentication for secure access to protected endpoints..

Features
Users API:
User registration and login with JWT authentication.
Profile management (view and update).
Logout with token blacklisting.

Products API:
Product listing with pagination (5 items per page).
Search by name or category.
Filter by category, price, or stock quantity.
Full CRUD operations (create, read, update, delete).


Tech Stack
Backend: Django, Django REST Framework
Database: SQLite 
Authentication: JWT via rest_framework_simplejwt
Filtering: django-filter
Pagination: DRF’s PageNumberPagination


Prerequisites
Python 3.8+
pip (Python package manager)
Git


Setup Instructions
1. Clone the Repository
git clone https://github.com/yourusername/ecommerce-api.git
cd ecommerce-api


3. Install Dependencies
pip install -r requirements.txt

4. Apply Migrations
python manage.py migrate

5. Create a Superuser (Optional)
For admin access:
python manage.py createsuperuser


6. Run the Server
python manage.py runserver


The API will be available at http://127.0.0.1:8000/

Configuration
Edit ecommerce_api/settings.py for custom settings:

Database: SQLite.
JWT: Adjust token lifetimes in SIMPLE_JWT.
Pagination: Modify PAGE_SIZE in REST_FRAMEWORK

API Endpoints
Base URL
http://127.0.0.1:8000/api/


Users API
- Endpoint: /users/register/
- Method: POST
- Description: Register a new user


- Endpoint: /users/login/
- Method: POST
- Description: Log in and get JWT tokens

- Endpoint: /users/logout/
- Method: POST
- Description: Log out (blacklist token)

- Endpoint: /users/profile/
- Method: GET
- Description: View user profile

- Endpoint: /users/profile/
- Method: PUT
- Description: Update user profile

Authentication Header: Authorization: Bearer <access-token> for protected endpoints.
Login Response: Returns refresh, access, and user data.

Products API


Endpoint: /products/
Method: GET
Description: List all products (paginated)

Endpoint: /products/
Method: POST
Description: Create a new product

Endpoint: /products/<id>/
Method: POST
Description: Retrieve a product


Endpoint: /products/<id>/
Method: PUT
Description: Update a product

Endpoint: /products/<id>/
Method: DELETE
Description: Update a product


Example Usage with Postman
1. Register a User
Request: POST /api/users/register/

Body:
    {
        "email": "test@example.com",
        "username": "testuser",
        "password": "test12345"
    }
Response: User data (201 Created).

2. Log In
Request: POST /api/users/login/

Body:
    {
        "email": "test@example.com",
        "password": "test12345"
    }
Response: {"refresh": "...", "access": "...", "user": {...}}.

3. List Products (Paginated)
Request: GET /api/products/
Response (if >5 products)



{
    "count": 10,
    "next": "/api/products/?page=2",
    "previous": null,
    "results": [{...}, {...}, ...]  // 5 products
}

4. Search Products
Request: GET /api/products/?search=APO
Response: Filtered product list.










