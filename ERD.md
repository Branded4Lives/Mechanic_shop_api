# Entity Relationship Diagram

This ERD represents the SQLAlchemy models in `app/models.py`.

```mermaid
erDiagram
    CUSTOMERS ||--o{ SERVICE_TICKETS : has
    SERVICE_TICKETS ||--o{ SERVICE_TICKET_MECHANICS : includes
    MECHANICS ||--o{ SERVICE_TICKET_MECHANICS : assigned_to

    CUSTOMERS {
        int id PK
        string first_name
        string last_name
        string email UK
        string phone
        string address
    }

    MECHANICS {
        int id PK
        string first_name
        string last_name
        string email UK
        string phone
        string specialty
    }

    SERVICE_TICKETS {
        int id PK
        int customer_id FK
        string vin
        text description
        string service_date
        string status
        datetime created_at
    }

    SERVICE_TICKET_MECHANICS {
        int service_ticket_id PK,FK
        int mechanic_id PK,FK
    }
```

## Relationships

- One customer can have many service tickets.
- Each service ticket belongs to one customer.
- One service ticket can have many mechanics.
- One mechanic can be assigned to many service tickets.
- The `service_ticket_mechanics` table connects mechanics and service tickets with a many-to-many relationship.
