


# HNG12 Stage 0 Backend API

A simple REST API that returns basic information including an email address, current datetime in ISO 8601 format, and GitHub repository URL.

## Features

- **JSON Response:** Returns the required information in JSON format.
- **CORS Support:** Handles cross-origin requests seamlessly.
- **Dynamic Datetime:** Automatically generates the current datetime in ISO 8601 format (UTC).
- **Fast Performance:** Ensures a response time of less than 500ms.

## Technology Stack

- **Python 3.8+**
- **FastAPI** - A modern web framework for building APIs.
- **Uvicorn** - An ASGI server for serving FastAPI applications.
- **pytz** - Library for timezone handling.

### Example Usage

You can test the API using postman :
request type : GET

```url
https://stage0-theclaire.onrender.com
```

## Local Setup

Follow these steps to set up the project on your local machine:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/TATA-THECLAIRE/stage0-Theclaire.git
   cd your-repo
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install fastapi uvicorn pytz
   ```

4. **Run the application:**
   ```bash
   uvicorn main:app --reload
   ```
   The API will be available at `http://localhost:8000`.

## API Documentation

### Endpoint

- **URL:** `https://stage0-theclaire.onrender.com`
- **Method:** `GET`
- **CORS:** Enabled for all origins

### Response Format

```json
{
    "email": "tatatheclaire@gmail.com",
    "current_datetime": "2025-01-30T09:30:00Z",
    "github_url": "https://github.com/yourusername/your-repo"
}
```

### Response Fields

- **`email`:** The email address used for HNG12 registration.
- **`current_datetime`:** Current UTC datetime in ISO 8601 format.
- **`github_url`:** URL to the GitHub repository.

### Example Usage

You can test the API using postman :

```url
https://stage0-theclaire.onrender.com
```

## Deployment

This API is deployed on :

**Render**


Follow the platform-specific deployment instructions and ensure you set up environment variables if needed.

## Related Resources

Explore more about Python development at [HNG Python Developers](https://hng.tech/hire/python-developers).

