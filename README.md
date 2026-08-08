# Mechanic Shop API

This project is a Flask REST API for a mechanic shop. It uses the Application Factory Pattern, SQLAlchemy models, Marshmallow schemas, and Flask blueprints for customers, mechanics, and service tickets.

## Features

- Flask application factory in `app/__init__.py`
- SQLAlchemy models for customers, mechanics, and service tickets
- Many-to-many relationship between mechanics and service tickets
- Blueprint folder for each resource
- Marshmallow schemas for serialization and validation
- Customer CRUD routes
- Mechanic CRUD routes
- Service ticket creation and retrieval
- Assign mechanics to service tickets
- Remove mechanics from service tickets
- Postman collection included for endpoint testing

## Tech Stack

- Python
- Flask
- Flask-SQLAlchemy
- Marshmallow
- Marshmallow-SQLAlchemy
- SQLite

## Project Structure

```text
app/
  customers/
    __init__.py
    routes.py
    schemas.py
  mechanics/
    __init__.py
    routes.py
    schemas.py
  service_tickets/
    __init__.py
    routes.py
    schemas.py
  __init__.py
  extensions.py
  models.py
config.py
run.py
requirements.txt
Mechanic_Shop_API.postman_collection.json
```

## Getting Started

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows PowerShell:

```bash
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Database Setup

By default, the API can run with SQLite for quick local testing. To use MySQL, create a database and add a `.env` file.

Create the MySQL database:

```sql
CREATE DATABASE mechanic_shop_db;
```

Create `.env` from `.env.example` and update the password:

```bash
MECHANIC_SHOP_DATABASE_URI=mysql+pymysql://root:your_password@localhost/mechanic_shop_db
SECRET_KEY=dev-secret-key
```

If `.env` is not present, the app falls back to SQLite:

```text
sqlite:///mechanic_shop.db
```

Run the API:

```bash
python run.py
```

The API runs at:

```text
http://127.0.0.1:5000
```

The SQLite database is created automatically inside the Flask `instance` folder when the app starts.

## Reset The Database

To reset all tables:

```bash
flask --app run init-db
```

## Endpoints

### Customers

```text
POST   /customers/
GET    /customers/
GET    /customers/<customer_id>
PUT    /customers/<customer_id>
DELETE /customers/<customer_id>
```

### Mechanics

```text
POST   /mechanics/
GET    /mechanics/
GET    /mechanics/<mechanic_id>
PUT    /mechanics/<mechanic_id>
DELETE /mechanics/<mechanic_id>
```

### Service Tickets

```text
POST   /service-tickets/
GET    /service-tickets/
GET    /service-tickets/<ticket_id>
PUT    /service-tickets/<ticket_id>
DELETE /service-tickets/<ticket_id>
PUT    /service-tickets/<ticket_id>/assign-mechanic/<mechanic_id>
PUT    /service-tickets/<ticket_id>/remove-mechanic/<mechanic_id>
```

## Example Request Bodies

Create a customer:

```json
{
  "first_name": "Brandon",
  "last_name": "Customer",
  "email": "brandon@example.com",
  "phone": "555-0100",
  "address": "123 Main St"
}
```

Create a mechanic:

```json
{
  "first_name": "Maya",
  "last_name": "Wrench",
  "email": "maya@example.com",
  "phone": "555-0111",
  "specialty": "Diagnostics"
}
```

Create a service ticket:

```json
{
  "customer_id": 1,
  "vin": "1HGCM82633A004352",
  "description": "Oil change and brake inspection",
  "service_date": "2026-08-01",
  "status": "open",
  "mechanic_ids": [1]
}
```

## Postman

Import `Mechanic_Shop_API.postman_collection.json` into Postman. The collection uses a `base_url` variable set to:

```text
http://127.0.0.1:5000
```

Run the API locally before sending the requests.
