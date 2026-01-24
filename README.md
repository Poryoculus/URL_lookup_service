

# Malware URL Lookup Service

## Overview

A high-performance HTTP API designed to verify URL safety. The service checks requested URLs against a database of known malicious hostnames, paths, and query strings. It is optimized for use as a synchronous check within an HTTP proxy layer.

## 🚀 Getting Started (Docker)

The easiest way to run the service, including the database, is using **Docker Compose**.

1. **Clone the repository**
```bash
git clone https://github.com/Poryoculus/URL_lookup_service.git
cd URL_lookup_service

```


2. **Launch the stack**
```bash
docker compose up --build

```


3. **Access the Service**
* **API Base:** `http://localhost:8000`
* **Interactive Docs (Swagger):** `http://localhost:8000/docs`


---

## 🛠 API Specification

### Lookup Endpoint

Checks if a specific URL is flagged as malicious.

**Format:** `GET /urlinfo/1/{hostname_and_port}/{path_and_query}`

**Example Request:** `GET http://localhost:8000/urlinfo/1/www.evil.com:80/download?file=virus.exe`

**Success Response:**


```json
{
  "url": "www.evil.com:80/download?file=virus.exe",
  "is_malware": true,
  "safe": false
}

```


---

## 🧪 Testing the API

Once the containers are running, you can test the following URLs to verify the logic. These cover standard lookups, custom ports, and query string matching.

### 1. Simple Malware Match

**URL:** `bad.com/malware`

**Curl Command:**

```bash
curl "http://localhost:8000/urlinfo/1/bad.com/malware"

```

### 2. Match with Custom Port

**URL:** `malware-host.net:8080/v1/payload?target=sys32`

**Curl Command:**

```bash
curl "http://localhost:8000/urlinfo/1/malware-host.net:8080/v1/payload?target=sys32"

```

### 3. Match with specific Query String

**URL:** `evil.com/phish?redirect=login`

**Curl Command:**

```bash
curl "http://localhost:8000/urlinfo/1/evil.com/phish?redirect=login"

```

### 4. Safe URL (Not in Database)

**URL:** `google.com/search`

**Curl Command:**

```bash
curl "http://localhost:8000/urlinfo/1/google.com/search"

```

---

## 💻 Local Development

If you prefer to run the API outside of Docker for development:

1. **Setup Environment**
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install .

```


2. **Run with Hot-Reload**
```bash
uvicorn src.main:app --reload

```


3. **Testing**
The project uses `pytest` for automated testing.
```bash
pytest

```

---

🏗 Project Structure & Standards

    Modern Packaging: Managed via pyproject.toml (PEP 621).

    Linting: Configured with Ruff for high-performance code analysis.

    Database: SQLAlchemy integration with PostgreSQL (Hosted on Railway).

    Containerization: Multi-stage Docker builds for lean production images.

    Automated Migrations: Python-based migration runner to ensure schema consistency on startup.

⚙️ Environment Configuration

The application requires a PostgreSQL connection string. Create a .env file in the root directory:
Fragmento de código

DATABASE_URL=postgresql://user:password@hostname:port/databasename

    Note: For this technical test, the database is hosted on Railway. The application will automatically run migrations defined in /migrations upon startup to ensure the malware_urls table and seed data are present.
---

## Development Notes

This project adheres to a clean Git workflow and follows modern Python best practices. Code quality is maintained through automated linting and unit tests. AI-assisted tools may be used for boilerplate, but all logic is manually reviewed and validated for security and accuracy.

