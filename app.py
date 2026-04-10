from flask import Flask
import os

# Create Flask app
app = Flask(__name__)

# Homepage route
@app.route('/')
def home():
    return "Hello! My DevOps Project is Running 🚀"

# Run the app
if __name__ == '__main__':
    # Get port from environment (for Render)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
