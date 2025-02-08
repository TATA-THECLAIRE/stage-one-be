import os
import math
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    
    for i in range(2, int(math.sqrt(abs(n))) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect_number(n):
    """Check if a number is a perfect number."""
    if n <= 0:
        return False
    
    divisor_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisor_sum == n

def is_armstrong_number(n):
    """Check if a number is an Armstrong number."""
    if n < 0:
        return False
    
    num_str = str(abs(n))
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    return armstrong_sum == abs(n)

def get_number_fact(number):
    """Fetch a mathematical fact about the number from Numbers API."""
    try:
        response = requests.get(
            f"http://numbersapi.com/{number}/math",
            timeout=2
        )
        return response.text if response.status_code == 200 else f"{number} is a number"
    except:
        return f"{number} is a number"

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    # Get number from query parameter
    number_param = request.args.get('number')
    
    # If number parameter is missing
    if number_param is None:
        return jsonify({
            "number": "",
            "error": True
        }), 400
    
    # Try to convert to integer
    try:
        number = int(number_param)
    except (ValueError, TypeError):
        return jsonify({
            "number": number_param,
            "error": True
        }), 400
    
    # Determine properties
    properties = []
    
    # Check Armstrong
    if is_armstrong_number(number):
        properties.append("armstrong")
    
    # Check even/odd
    if number % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")
    
    # Prepare response
    response = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect_number(number),
        "properties": properties,
        "digit_sum": sum(int(digit) for digit in str(abs(number))),
        "fun_fact": get_number_fact(number)
    }
    
    return jsonify(response)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)