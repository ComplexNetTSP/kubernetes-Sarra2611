# Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Copy application files
COPY app.py /app/app.py

# Install dependencies
RUN pip install flask pymongo

# Expose Flask application port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
