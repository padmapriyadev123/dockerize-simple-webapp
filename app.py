from flask import Flask

# Create Flask app
app = Flask(__name__)

# Homepage route
@app.route('/')
def home():
    return "Hello! My DevOps Project is Running 🚀"

# Run the app
if __name__ == '__main__':
    # host=0.0.0.0 allows access outside Docker container
    app.run(host='0.0.0.0', port=5000)