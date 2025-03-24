# Use official Python image as base
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy only requirements first for better caching
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app files
COPY . .

# Expose the port Flask runs on
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]