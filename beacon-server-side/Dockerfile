FROM python:3.9-slim

# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Copy the Python script
COPY app.py /app/app.py

# Run the Flask app
CMD ["python", "/app/app.py"]
