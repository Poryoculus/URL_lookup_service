

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

--


## Part 2 Q&A

1. The size of the URL list could grow infinitely. How might you scale this beyond the memory capacity of the system?

    R: If the URL list grows too large for memory, I would store the URLs in a database instead of keeping them in memory. For example, using a managed database like Amazon RDS or DynamoDB would allow the data to grow without being limited by the application memory. This would also make the data persistent and easier to manage.

2. Assume that the number of requests will exceed the capacity of a single system. How might you solve this, and how might this change if you have to distribute this workload to an additional region, such as Europe?

    R: If one system is not enough to handle the traffic, I would run multiple instances of the API and put them behind a load balancer so requests are distributed between them.

    If the service also needs to run in another region like Europe, I would deploy the application there as well and use a global routing solution like AWS Global Accelerator so users are routed to the closest region.

3. What are some strategies you might use to update the service with new URLs? (e.g., 5,000 URLs a day with updates every 10 minutes).

    R: To handle frequent updates, I would create a process that runs every few minutes to insert or update the URLs in the database. This could be a scheduled job or a small service that processes new data in batches. This way, the main API is not affected by the update process.

4. You’re woken up at 3am. What are some of the things you’ll look for?

    R: I would have Splunk monitoring this app. I would first check the monitoring and logs to see if there are errors or if the service is down. I would check if the instances are running, if there is high CPU or memory usage, and review application logs to understand what is failing.

5. Does that change anything you’ve done in the app?

    R: Yes, it would make me add better logging and a health check endpoint so it’s easier to see if the service is running correctly and to help troubleshoot problems faster.

6. What are some considerations for the lifecycle of the app?

    R: I would think about things like monitoring, updating dependencies, handling growing data, and making sure the system can scale as usage increases. I would also consider backups and basic security updates over time.

7. You need to deploy a new version of this application. What would you do?

    R: I would build a new Docker image for the new version and deploy it through a CI/CD pipeline. I would try to deploy it in a way that avoids downtime, for example by updating instances gradually. If there are problems, I would be able to roll back to the previous version.



