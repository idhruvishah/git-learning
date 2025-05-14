from flask import Flask, request, jsonify
from functools import wraps
import base64

app = Flask(__name__)

# Hardcoded credentials for demo
USERNAME = "admin"
PASSWORD = "password123"

# Function to return 401 error
def unauthorized():
    return jsonify({"message": "Authentication required"}), 401

# Function to check credentials
def check_auth(username, password):
    return username == USERNAME and password == PASSWORD

# Decorator for basic auth
def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return unauthorized()

        try:
            scheme, credentials = auth_header.split()
            if scheme.lower() != 'basic':
                return unauthorized()

            decoded = base64.b64decode(credentials).decode('utf-8')
            username, password = decoded.split(':', 1)

            if not check_auth(username, password):
                return unauthorized()
        except Exception as e:
            return unauthorized()

        return f(*args, **kwargs)
    return decorated

# Public route (no auth)
@app.route('/public', methods=['GET'])
def public():
    return jsonify({"message": "This is public data"})

# Secure route (requires basic auth)
@app.route('/secure-data', methods=['GET'])
@requires_auth
def secure():
    return jsonify({"message": "This is secure data accessible only to authenticated users."})

if __name__ == '__main__':
    app.run(debug=True)



print("Hey I Am dip patel")
print("heyijcbnnkdbcndbc")