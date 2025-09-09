# Use official Python slim image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy app files
COPY app.py .
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for Flask
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
