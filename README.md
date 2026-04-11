# DjangoTestBeam

A Django REST Framework project demonstrating core ORM relationship patterns — OneToOne, ForeignKey (one-to-many), and ManyToMany — through a simple e-commerce data model. Includes Docker Compose for a production-like stack with PostgreSQL, Redis, Daphne, and Nginx.

## Features

- Full CRUD REST API for Users, Profiles, Orders, and Products
- Demonstrates all three Django ORM relationship types in a single cohesive data model
- WebSocket support via Django Channels + Daphne
- Swagger / OpenAPI documentation via `drf-yasg`
- Dockerized with PostgreSQL, Redis, Nginx, and Gunicorn

## Tech Stack

| Layer | Technology |
|---|---|
| Web framework | Django 5.2 + DRF 3.16 |
| WebSockets | Django Channels 4 + Daphne |
| Database | PostgreSQL (psycopg2) |
| Cache / broker | Redis |
| API docs | drf-yasg (Swagger) |
| Deployment | Docker Compose + Nginx |

## Data Model

```
User ──────────── Profile   (OneToOne)
 │
 └──< Order >──── Product   (ForeignKey + ManyToMany)
```

| Model | Key Fields |
|---|---|
| `User` | `username` |
| `Profile` | `user` (OneToOne), `email`, `address` |
| `Product` | `name`, `price` |
| `Order` | `user` (FK), `products` (M2M), `created_at` |

## Project Structure

```
DjangoTestBeam/
├── app/
│   ├── models.py       # User, Profile, Order, Product
│   ├── serializers.py  # ModelSerializers for all entities
│   ├── views.py        # ListCreate + RetrieveUpdateDestroy generics
│   └── urls.py
├── main/               # Django settings, root URL conf
├── docker/             # Dockerfiles, Nginx config, entrypoint scripts
├── docker-compose.yml
├── .env.example
└── requirements.txt
```

## Getting Started

### Local Setup

```bash
git clone https://github.com/Nezdeshniy/DjangoTestBeam.git
cd DjangoTestBeam
cp .env.example .env  # fill in your values
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Docker

```bash
cp .env.dockerexample .env.docker
docker compose up --build
```

The API will be available at `http://localhost`.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET / POST | `/users/` | List or create users |
| GET / PUT / DELETE | `/users/<id>/` | Retrieve, update, or delete a user |
| GET / POST | `/profiles/` | List or create profiles |
| GET / POST | `/products/` | List or create products |
| GET / POST | `/orders/` | List or create orders |

Swagger UI is available at `/swagger/`.

## Environment Variables

| Variable | Description |
|---|---|
| `SECRET_KEY` | Django secret key |
| `DEBUG` | `1` for development, `0` for production |
| `DB_ENGINE` | Database backend driver |
| `DB_NAME` | PostgreSQL database name |
| `DB_USER` | PostgreSQL username |
| `DB_PASSWORD` | PostgreSQL password |
| `DB_HOST` | Database host |
| `DB_PORT` | Database port (default `5432`) |
