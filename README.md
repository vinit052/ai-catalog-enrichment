# AI Catalog Enrichment API

AI-powered product catalog enrichment platform built with **FastAPI**, designed to process product data files, enrich catalog information, and integrate with vector search and backend services.

The application is containerized for local development and structured to support future production deployment using external managed services.

---

## Features

Current features:

* FastAPI REST API
* Docker-based local development environment
* Environment-based configuration
* Health monitoring endpoint
* Redis integration
* Qdrant vector database integration
* PostgreSQL database setup
* Product file upload foundation
* Swagger and ReDoc API documentation

Planned features:

* CSV/XLSX catalog processing
* Product data validation
* AI-based product enrichment
* Image processing
* Embedding generation
* Vector search
* Background job processing

---

# Technology Stack

## Backend

* Python 3.12
* FastAPI
* Uvicorn

## Databases & Services

* PostgreSQL 16
* Redis 7
* Qdrant Vector Database

## Development

* Docker
* Docker Compose
* Environment-based configuration

---

# Project Structure

## Project Structure

```
.
├── .env
├── .env.example
├── .gitignore
├── README.md
├── docker-compose.yml
│
└── app/
    ├── Dockerfile
    ├── requirements.txt
    │
    └── src/
        ├── main.py                         # FastAPI application entry point
        ├── dependencies.py                 # Dependency injection configuration
        ├── alembic.ini                      # Alembic configuration
        │
        ├── alembic/                         # Database migrations
        │   ├── env.py
        │   ├── README
        │   ├── script.py.mako
        │   └── versions/
        │       └── dab8637ca681_create_imports_and_items_tables.py
        │
        ├── core/                            # Core application layer
        │   │
        │   ├── config.py                    # Application configuration
        │   │
        │   ├── exceptions/                  # Custom exceptions
        │   │   ├── database.py
        │   │   └── service.py
        │   │
        │   ├── infra/                       # Infrastructure layer
        │   │   │
        │   │   ├── database/
        │   │   │   ├── base.py              # SQLAlchemy Base
        │   │   │   ├── connection.py        # Database connection
        │   │   │   ├── session.py           # Database session handling
        │   │   │   │
        │   │   │   └── models/
        │   │   │       ├── import_model.py  # Import table ORM model
        │   │   │       ├── item.py          # Item table ORM model
        │   │   │       └── __init__.py
        │   │   │
        │   │   ├── llm/                     # LLM integrations
        │   │   │   └── __init__.py
        │   │   │
        │   │   ├── qdrant/                  # Vector database integration
        │   │   │   ├── client.py
        │   │   │   └── __init__.py
        │   │   │
        │   │   └── redis/                   # Redis integration
        │   │       └── redis_client.py
        │   │
        │   ├── mappers/                     # Data transformation layer
        │   │   ├── import_mapper.py         # Creates Import model objects
        │   │   └── item_mapper.py           # Creates Item model objects
        │   │
        │   ├── repositories/                 # Database access layer
        │   │   ├── base_repository.py
        │   │   ├── import_repository.py     # Import database operations
        │   │   └── item_repository.py       # Item database operations
        │   │
        │   └── services/                    # Domain services
        │       ├── import_service.py        # Import transaction workflow
        │       └── item_service.py          # Item operations
        │
        ├── routers/                         # API endpoints
        │   ├── health.py                    # Health check API
        │   ├── upload.py                    # File upload API
        │   ├── item.py                      # Item APIs
        │   └── __init__.py
        │
        ├── services/                        # Application services
        │   └── file_service.py              # File processing workflow
        │
        ├── parsers/                         # File parsing layer
        │   ├── base_parser.py
        │   ├── csv_parser.py
        │   ├── excel_parser.py
        │   ├── image_parser.py
        │   └── __init__.py
        │
        ├── validators/                      # Validation layer
        │   └── product_import_validator.py
        │
        └── schemas/                          # Request/response schemas
            └── product.py
```


---

# Local Development Setup

## Prerequisites

Install:

* Docker
* Docker Compose

Verify:

```bash
docker --version
docker compose version
```

---

# Environment Configuration

Copy example environment file:

```bash
cp .env.example .env
```

Update values according to your local setup.

Example:

```env
APP_ENV=development
APP_PORT=8000

REDIS_HOST=redis
REDIS_PORT=6379

QDRANT_HOST=qdrant
QDRANT_PORT=6333

POSTGRES_HOST=postgres
POSTGRES_PORT=5432
POSTGRES_DB=myapp
POSTGRES_USER=myuser
POSTGRES_PASSWORD=mypassword
```

---

# Start Application

Build containers:

```bash
docker compose build
```

Start services:

```bash
docker compose up -d
```

Check running services:

```bash
docker compose ps
```

Expected services:

```
app
postgres
redis
qdrant
```

---

# Stop Application

Stop containers:

```bash
docker compose down
```

Remove containers and volumes:

```bash
docker compose down -v
```

---

# Application URLs

## API

```
http://localhost:8000
```

## Swagger Documentation

```
http://localhost:8000/docs
```

## ReDoc Documentation

```
http://localhost:8000/redoc
```

## OpenAPI Schema

```
http://localhost:8000/openapi.json
```

---

# API Endpoints

## System Information

### GET /

Returns application information.

Example response:

```json
{
  "name": "AI Catalog Enrichment API",
  "status": "running",
  "environment": "development"
}
```

---

## Health Check

### GET /health/

Checks application dependencies.

Services checked:

* Redis
* Qdrant

Example:

```json
{
  "status": "ok",
  "services": {
    "redis": true,
    "qdrant": true
  }
}
```

---

## Product Upload

### POST /products/upload

Upload product catalog files.

Supported formats:

* CSV
* XLS
* XLSX
* JPG
* PNG

Example:

```bash
curl -X POST \
http://localhost:8000/products/upload \
-F "file=@products.csv"
```

---

# Docker Commands

## View Logs

Application logs:

```bash
docker compose logs -f app
```

All services:

```bash
docker compose logs -f
```

---

## Restart Application

```bash
docker compose restart app
```

---

## Access Container Shell

```bash
docker exec -it ai-catalog-erichment bash
```

---

## Rebuild After Dependency Changes

```bash
docker compose build app
docker compose up -d
```

---

# Development Mode

The application runs with Uvicorn reload enabled:

```
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Source code changes automatically reload the API.

---

# Architecture Overview

```
Client
 |
 |
FastAPI
 |
 ├── Routers
 │     |
 │     ├── Health API
 │     └── Product API
 |
 ├── Services
 │     |
 │     └── File Processing
 |
 |
 ├── PostgreSQL
 |
 ├── Redis
 |
 └── Qdrant
```

---

# Future Production Architecture

The application is designed so production services can be changed using environment variables.

Example:

Development:

```
Docker PostgreSQL
Docker Redis
Docker Qdrant
```

Production:

```
Managed PostgreSQL
Managed Redis
Cloud Qdrant
Object Storage
Background Workers
```

No application code changes should be required.

# License

Internal project.
