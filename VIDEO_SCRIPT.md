# Video Presentation Script

Target length: 3 to 4 minutes. Keep the video under 5 minutes and upload it directly to Disco.

## 1. Introduction

Hi, my name is [Your Name], and this is my Mechanic Shop API project.

This API manages customers, mechanics, and service tickets for a mechanic shop. It was built with Flask, SQLAlchemy, Marshmallow, and the Application Factory Pattern.

## 2. Project Overview

The app uses separate blueprints for customers, mechanics, and service tickets. Each blueprint has its own `__init__.py`, `routes.py`, and `schemas.py` file.

The database models include customers, mechanics, and service tickets. Service tickets can have multiple mechanics assigned to them, and mechanics can work on multiple service tickets.

## 3. How It Works

The application factory is defined in `app/__init__.py`. That file creates the Flask app, initializes SQLAlchemy, registers the blueprints, and sets the URL prefixes.

The Marshmallow schemas serialize and validate incoming and outgoing JSON data. I used SQLAlchemyAutoSchema for the main resource schemas.

## 4. Demonstration

First, I will start the Flask server with `python run.py`.

Next, I will use Postman to create a customer with the `/customers/` POST route.

Then I will create a mechanic with the `/mechanics/` POST route.

After that, I will create a service ticket with the `/service-tickets/` POST route. The service ticket includes the customer ID, vehicle VIN, description, service date, and status.

Now I will assign the mechanic to the service ticket using:

```text
PUT /service-tickets/<ticket_id>/assign-mechanic/<mechanic_id>
```

Then I will retrieve all service tickets with `GET /service-tickets/` and show that the mechanic is attached to the ticket.

Next, I will remove the mechanic using:

```text
PUT /service-tickets/<ticket_id>/remove-mechanic/<mechanic_id>
```

Finally, I will briefly show update and delete routes for mechanics and customers.

## 5. Closing

This project meets the assignment requirements by using Flask blueprints, Marshmallow schemas, the Application Factory Pattern, full mechanic CRUD routes, service ticket routes, and a Postman collection for endpoint testing.

Thank you for watching my project presentation.

## Quick Recording Checklist

- Keep the video under 5 minutes
- Show your face on camera
- Show the Flask server running
- Show the Postman collection
- Create a customer
- Create a mechanic
- Create a service ticket
- Assign a mechanic
- Remove a mechanic
- Retrieve service tickets
- Mention the app factory and blueprint structure
