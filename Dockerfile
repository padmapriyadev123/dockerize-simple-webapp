<<<<<<< HEAD
# Use official Python image
FROM python:3.9

# Set working directory inside container
WORKDIR /app

# Copy all project files to container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Run the app
=======
# Use official Python image
FROM python:3.9

# Set working directory inside container
WORKDIR /app

# Copy all project files to container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Run the app
>>>>>>> 2ad3f051ffbff9141e4c8e475c415afe40ec02d4
CMD ["python", "app.py"]