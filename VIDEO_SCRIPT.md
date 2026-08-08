# Video Presentation Script

Target length: 3 to 5 minutes. Keep it simple, show the required files, then show the API working in Postman.

## Before You Record

Have these open:

- VS Code with this project open
- A terminal in the project folder
- Postman with `Mechanic_Shop_API.postman_collection.json` imported

Start the API before or during the recording:

```bash
python run.py
```

The API should be running at:

```text
http://127.0.0.1:5000
```

## 1. Introduction - 15 Seconds

Where to be: VS Code, project root.

What to say:

Hi, my name is Brandon, and this is my Mechanic Shop API project.

This is a Flask REST API for a mechanic shop. It manages customers, mechanics, and service tickets. The project uses the Application Factory Pattern, SQLAlchemy models, Marshmallow schemas, Flask blueprints, and a Postman collection for testing.

## 2. Show The Project Structure - 30 Seconds

Where to be: VS Code file explorer.

What to show:

- `app/`
- `app/customers/`
- `app/mechanics/`
- `app/service_tickets/`
- `app/models.py`
- `README.md`
- `Mechanic_Shop_API.postman_collection.json`

What to say:

The project is organized by resource. Customers, mechanics, and service tickets each have their own blueprint folder. Each folder has an `__init__.py`, a `routes.py`, and a `schemas.py` file.

This keeps the API organized and matches the assignment requirement for blueprint folders.

## 3. Show The Application Factory - 30 Seconds

Where to be: `app/__init__.py`.

What to show:

Point to `create_app`.

Then point to these lines:

```python
app.register_blueprint(customers_bp, url_prefix="/customers")
app.register_blueprint(mechanics_bp, url_prefix="/mechanics")
app.register_blueprint(service_tickets_bp, url_prefix="/service-tickets")
```

What to say:

This file uses the Application Factory Pattern. The `create_app` function creates the Flask app, initializes the database, registers the blueprints, and assigns the required URL prefixes.

The mechanic routes use `/mechanics`, and the service ticket routes use `/service-tickets`, which matches the rubric.

## 4. Show The Models - 30 Seconds

Where to be: `app/models.py`.

What to show:

- `Customer`
- `Mechanic`
- `ServiceTicket`
- `service_ticket_mechanics`

What to say:

These are my database models. A customer can have many service tickets. Mechanics and service tickets have a many-to-many relationship through the `service_ticket_mechanics` table.

That relationship is what allows a mechanic to be assigned to a service ticket and removed from a service ticket.

## 5. Show Mechanic Schema And Routes - 45 Seconds

Where to be: first `app/mechanics/schemas.py`, then `app/mechanics/routes.py`.

What to show in `schemas.py`:

- `MechanicSchema`
- `MechanicCreateSchema`
- `MechanicUpdateSchema`

What to say:

This file contains the Marshmallow schemas for mechanics. I used `SQLAlchemyAutoSchema` for serialization, and separate create and update schemas for validating incoming JSON.

Where to be next: `app/mechanics/routes.py`.

What to show:

- `POST /`
- `GET /`
- `GET /<int:mechanic_id>`
- `PUT /<int:mechanic_id>`
- `DELETE /<int:mechanic_id>`

What to say:

These are the full CRUD routes for mechanics. I can create, retrieve, update, and delete mechanics. The route paths are short because the blueprint already has the `/mechanics` URL prefix.

## 6. Show Service Ticket Schema And Routes - 45 Seconds

Where to be: first `app/service_tickets/schemas.py`, then `app/service_tickets/routes.py`.

What to show in `schemas.py`:

- `ServiceTicketSchema`
- nested `customer`
- nested `mechanics`
- `mechanic_ids`

What to say:

This schema serializes service tickets and includes nested customer and mechanic information. The create schema accepts `mechanic_ids`, so mechanics can be attached when a ticket is created.

Where to be next: `app/service_tickets/routes.py`.

What to show:

- `POST /`
- `GET /`
- `PUT /<int:ticket_id>/assign-mechanic/<int:mechanic_id>`
- `PUT /<int:ticket_id>/remove-mechanic/<int:mechanic_id>`

What to say:

These service ticket routes match the assignment requirements. I can create service tickets, retrieve all service tickets, assign mechanics, and remove mechanics using the relationship list.

## 7. Postman Demo - 1 To 2 Minutes

Where to be: Terminal first.

What to show:

Run:

```bash
python run.py
```

What to say:

Now I am running the Flask server locally so I can test the API in Postman.

Where to be next: Postman.

### Step 1: Create A Customer

Request:

```text
POST {{base_url}}/customers/
```

Body:

```json
{
  "first_name": "Brandon",
  "last_name": "Customer",
  "email": "brandon@example.com",
  "phone": "555-0100",
  "address": "123 Main St"
}
```

What to say:

First, I create a customer. The response gives me a customer ID, which I will use when creating the service ticket.

### Step 2: Create A Mechanic

Request:

```text
POST {{base_url}}/mechanics/
```

Body:

```json
{
  "first_name": "Maya",
  "last_name": "Wrench",
  "email": "maya@example.com",
  "phone": "555-0111",
  "specialty": "Diagnostics"
}
```

What to say:

Next, I create a mechanic. The response gives me a mechanic ID.

### Step 3: Create A Service Ticket

Request:

```text
POST {{base_url}}/service-tickets/
```

Body:

```json
{
  "customer_id": 1,
  "vin": "1HGCM82633A004352",
  "description": "Oil change and brake inspection",
  "service_date": "2026-08-08",
  "status": "open"
}
```

What to say:

Now I create a service ticket for the customer. The ticket includes the customer ID, VIN, description, service date, and status.

Use the actual customer ID from your response if it is not `1`.

### Step 4: Assign A Mechanic

Request:

```text
PUT {{base_url}}/service-tickets/1/assign-mechanic/1
```

What to say:

Now I assign the mechanic to the service ticket. This uses the many-to-many relationship between service tickets and mechanics.

Use the actual ticket ID and mechanic ID from your responses if they are not `1`.

### Step 5: Get All Service Tickets

Request:

```text
GET {{base_url}}/service-tickets/
```

What to say:

Now I retrieve all service tickets. In the response, I can see the ticket information and the assigned mechanic.

### Step 6: Remove A Mechanic

Request:

```text
PUT {{base_url}}/service-tickets/1/remove-mechanic/1
```

What to say:

Finally, I remove the mechanic from the service ticket. This shows that the relationship can be added and removed through the API.

## 8. Show README And Postman Collection - 20 Seconds

Where to be: VS Code.

What to show:

- `README.md`
- `Mechanic_Shop_API.postman_collection.json`

What to say:

The repository includes a README with setup and endpoint instructions. It also includes an exported Postman collection so the endpoints can be tested.

## 9. Closing - 15 Seconds

Where to be: VS Code or Postman.

What to say:

This project meets the rubric by using the Application Factory Pattern, Flask blueprints, Marshmallow schemas, full mechanic CRUD routes, service ticket creation, mechanic assignment and removal, service ticket retrieval, README instructions, and an exported Postman collection.

Thank you for watching my presentation.

## Quick Rubric Checklist

- Show `app/__init__.py`
- Show blueprint registration
- Show `app/mechanics/`
- Show `app/service_tickets/`
- Show Marshmallow schemas
- Show mechanic CRUD routes
- Show service ticket create and get routes
- Show assign mechanic route
- Show remove mechanic route
- Show Postman tests
- Show README
- Mention GitHub repository and Disco video upload

