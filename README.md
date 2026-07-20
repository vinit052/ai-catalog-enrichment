# AI Catalog Enrichment API

AI-powered product catalog enrichment platform built with **FastAPI**, designed to process product data files, enrich catalog information, and integrate with vector search and backend services.

The application is containerized for local development and structured to support future production deployment using external managed services.

---

## Table of Contents

- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Architecture Overview](#architecture-overview)
- [Local Development Setup](#local-development-setup)
  - [Prerequisites](#prerequisites)
  - [Environment Configuration](#environment-configuration)
  - [Start Application](#start-application)
  - [Stop Application](#stop-application)
- [Application URLs](#application-urls)
- [API Endpoints](#api-endpoints)
  - [System Information](#system-information)
  - [Health Check](#health-check)
  - [Product Upload](#product-upload)
- [Docker Commands](#docker-commands)
  - [View Logs](#view-logs)
  - [Restart Application](#restart-application)
  - [Access Container Shell](#access-container-shell)
  - [Rebuild After Dependency Changes](#rebuild-after-dependency-changes)
- [Development Mode](#development-mode)
- [Future Production Architecture](#future-production-architecture)
- [License](#license)

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

```
├── .env                                      # Local environment variables
├── .env.example                              # Environment variable template
├── .gitignore                                # Git ignore configuration
├── README.md                                 # Project documentation
├── docker-compose.yml                        # Local development services
│
└── app/
    ├── Dockerfile                            # Application container setup
    ├── requirements.txt                      # Python dependencies
    │
    └── src/                                  # Application source code
        ├── main.py                           # FastAPI application entry point
        ├── alembic.ini                       # Database migration configuration
        │
        ├── alembic/                          # Database migration management
        │   ├── README
        │   ├── env.py                        # Alembic migration environment
        │   ├── script.py.mako                # Migration template
        │   └── versions/                     # Migration history
        │       └── dab8637ca681_create_imports_and_items_tables.py
        │                                      # Creates imports and items tables
        │
        ├── dependencies/                     # FastAPI dependency injection layer
        │   ├── __init__.py
        │   ├── database.py                   # Database dependency provider
        │   └── services.py                   # Service dependency wiring
        │
        ├── core/                             # Core business application layer
        │   ├── __init__.py
        │   ├── config.py                     # Application configuration
        │   │
        │   ├── exceptions/                   # Custom application exceptions
        │   │   ├── database.py
        │   │   └── service.py
        │   │
        │   ├── infra/                        # External infrastructure layer
        │   │   ├── __init__.py
        │   │   │
        │   │   ├── database/                 # Database infrastructure
        │   │   │   ├── __init__.py
        │   │   │   ├── base.py               # SQLAlchemy base class
        │   │   │   ├── connection.py         # Database connection setup
        │   │   │   ├── session.py            # Database session management
        │   │   │   └── models/               # Database ORM models
        │   │   │       ├── __init__.py
        │   │   │       ├── import_model.py   # Import table model
        │   │   │       └── item.py           # Item table model
        │   │   │
        │   │   ├── llm/                      # LLM integration layer
        │   │   │   └── __init__.py
        │   │   │
        │   │   ├── qdrant/                   # Vector database integration
        │   │   │   ├── __init__.py
        │   │   │   └── client.py
        │   │   │
        │   │   └── redis/                    # Redis messaging integration
        │   │       ├── consumer.py           # Redis consumer
        │   │       ├── publisher.py          # Redis publisher
        │   │       └── redis_client.py       # Redis connection client
        │   │
        │   ├── mappers/                      # Data transformation layer
        │   │   ├── import_mapper.py          # Import entity mapper
        │   │   └── item_mapper.py            # Item entity mapper
        │   │
        │   ├── repositories/                 # Database access layer
        │   │   ├── base_repository.py
        │   │   ├── import_repository.py      # Import database operations
        │   │   └── item_repository.py        # Item database operations
        │   │
        │   └── services/                     # Business logic layer
        │       ├── __init__.py
        │       ├── import_service.py         # Import business operations
        │       ├── item_service.py           # Item business operations
        │       │
        │       └── ingestion/                # Import ingestion workflow
        │           ├── __init__.py
        │           ├── ingestion_service.py  # Main ingestion orchestration
        │           ├── parser_service.py     # File parsing workflow
        │           ├── validation_service.py # Data validation workflow
        │           ├── enrichment_queue_service.py
        │           │                         # Enrichment queue handling
        │           └── response_builder.py   # API response builder
        │
        ├── parsers/                          # File parsing implementations
        │   ├── __init__.py
        │   ├── base_parser.py                # Parser base interface
        │   ├── csv_parser.py                 # CSV parser
        │   ├── excel_parser.py               # Excel parser
        │   └── image_parser.py               # Image parser
        │
        ├── routers/                          # FastAPI API routes
        │   ├── __init__.py
        │   ├── health.py                     # Health check endpoint
        │   ├── imports.py                    # Import APIs
        │   ├── item.py                       # Item APIs
        │   └── upload.py                     # File upload APIs
        │
        └── validators/                       # Business validation layer
            └── product_import_validator.py   # Product import validation rules
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
  FastAPI Application
  |
  ├── Routers (API Layer)
  │     |
  │     ├── Health API
  │     ├── Import API
  │     ├── Upload API
  │     └── Item API
  |
  ├── Dependencies
  │     |
  │     ├── Database Session Injection
  │     └── Service Dependency Wiring
  |
  ├── Core Services (Business Layer)
  │     |
  │     ├── Ingestion Service
  │     │     |
  │     │     ├── Parser Service
  │     │     ├── Validation Service
  │     │     ├── Import Service
  │     │     └── Enrichment Queue Service
  │     |
  │     ├── Import Service
  │     └── Item Service
  |
  ├── Repositories (Data Access Layer)
  │     |
  │     ├── Import Repository
  │     └── Item Repository
  |
  ├── Infrastructure Layer
  │     |
  │     ├── PostgreSQL
  │     ├── Redis
  │     ├── Qdrant
  │     └── LLM Integrations
  |
  ├── Parsers
  │     |
  │     ├── CSV Parser
  │     ├── Excel Parser
  │     └── Image Parser
  |
  └── Validators
        |
        └── Product Import Validation
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
Background Workers
```

No application code changes should be required.

# License

Internal project.
