from flask import Flask
<<<<<<< HEAD
import os
=======
>>>>>>> 2ad3f05 (Add files via upload)

# Create Flask app
app = Flask(__name__)

# Homepage route
@app.route('/')
def home():
    return "Hello! My DevOps Project is Running 🚀"

# Run the app
if __name__ == '__main__':
<<<<<<< HEAD
    # Get port from environment (for Render)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
=======
    # host=0.0.0.0 allows access outside Docker container
    app.run(host='0.0.0.0', port=5000)
>>>>>>> 2ad3f05 (Add files via upload)
