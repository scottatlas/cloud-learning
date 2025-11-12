# Use official Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy the current folder (contains health_check.py)
COPY ./artifacts/health_check.py .

# Install boto3
RUN pip install boto3

# Run the health check script
CMD ["python", "health_check.py"]
