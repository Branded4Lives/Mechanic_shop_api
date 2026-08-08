# Simple Video Script

Target length: 2 minutes.

Do not explain every line of code. Just show that the required pieces exist and that the API works.

## Before You Record

Open:

- VS Code
- Terminal
- Postman

Start the API:

```bash
python run.py
```

Use:

```text
http://127.0.0.1:5000
```

## 1. Intro - 10 Seconds

**Show:** VS Code project folder.

**Say:**

Hi, my name is Brandon. This is my Mechanic Shop API.

It is a Flask REST API for customers, mechanics, and service tickets.

## 2. Project Structure - 15 Seconds

**Show:** File explorer in VS Code.

**Say:**

The project is organized into blueprint folders for customers, mechanics, and service tickets.

Each resource has its own routes and schemas.

## 3. App Factory - 20 Seconds

**Show:** `app/__init__.py`

Point to `create_app`.

Point to the blueprint registration lines:

```python
app.register_blueprint(customers_bp, url_prefix="/customers")
app.register_blueprint(mechanics_bp, url_prefix="/mechanics")
app.register_blueprint(service_tickets_bp, url_prefix="/service-tickets")
```

**Say:**

This is my application factory. It creates the Flask app, initializes the database, and registers the three blueprints.

## 4. Models - 20 Seconds

**Show:** `app/models.py`

Point to:

- `Customer`
- `Mechanic`
- `ServiceTicket`
- `service_ticket_mechanics`

**Say:**

These are my SQLAlchemy models.

Customers can have service tickets, and mechanics can be assigned to service tickets using the many-to-many table.

## 5. Routes And Schemas - 25 Seconds

**Show quickly:**

- `app/mechanics/routes.py`
- `app/mechanics/schemas.py`
- `app/service_tickets/routes.py`
- `app/service_tickets/schemas.py`

**Say:**

The schemas validate and serialize data.

The mechanic routes have full CRUD.

The service ticket routes create tickets, get tickets, assign mechanics, and remove mechanics.

## 6. Postman Demo - 45 Seconds

**Show:** Postman.

Run these requests from the collection:

```text
POST /customers/
POST /mechanics/
POST /service-tickets/
PUT /service-tickets/1/assign-mechanic/1
GET /service-tickets/
```

**Say while clicking:**

First, I create a customer.

Next, I create a mechanic.

Then I create a service ticket for the customer.

Now I assign the mechanic to the service ticket.

Finally, I get all service tickets and can see the ticket data returned by the API.

Use the actual IDs from your responses if they are not `1`.

## 7. Closing - 10 Seconds

**Show:** README and Postman collection.

**Say:**

This project includes the required Flask app structure, models, schemas, routes, README, and Postman collection.

Thank you for watching.

## Emergency Short Version

Use this if you feel rushed:

Hi, my name is Brandon. This is my Mechanic Shop API.

It uses Flask, SQLAlchemy, Marshmallow, blueprints, and Postman.

Here is my app factory and blueprint registration.

Here are my models for customers, mechanics, service tickets, and the mechanic-ticket relationship.

Here are my mechanic routes and service ticket routes.

Now I will test the API in Postman.

I create a customer, create a mechanic, create a service ticket, assign the mechanic, and retrieve all service tickets.

The API returns the expected data.

This project includes the required README and Postman collection.

Thank you for watching.
