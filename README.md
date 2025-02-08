# Number Classification API

A REST API that provides mathematical properties and fun facts about numbers.

## API Specification

### Endpoint
```
GET /api/classify-number?number=371
```

### Success Response (200 OK)
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

### Error Response (400 Bad Request)
```json
{
    "number": "alphabet",
    "error": true
}
```

## Features

- Determines if a number is prime
- Determines if a number is perfect
- Identifies Armstrong numbers
- Calculates digit sum
- Provides even/odd property
- Fetches fun facts about numbers from Numbers API

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running Locally

```bash
python app.py
```

The API will be available at `http://localhost:10000`

## Deployment

This API is deployed on Render.com. The live API is available at:
[Your-Render-URL]/api/classify-number?number=371

## Technology Stack

- Python
- Flask
- CORS support
- JSON responses
- Numbers API integration

## Notes

- Response time is optimized to be under 500ms for most requests
- CORS is enabled for cross-origin requests
- Input validation ensures only valid integers are processed
- Error handling returns appropriate status codes