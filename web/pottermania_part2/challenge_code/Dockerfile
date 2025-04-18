# Use a Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current dir into the container at /app
COPY app/ /app

# Installing dependencies
RUN pip install --no-cache-dir --upgrade pip && pip install -r requirements.txt

# Expose port 5000 
EXPOSE 5000

# Start the Flask app
CMD ["python", "magic.py"]


