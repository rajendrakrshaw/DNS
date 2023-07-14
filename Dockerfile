# Dockerfile

# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Expose the port on which the DNS server will run
EXPOSE 5000

# Define the command to run the DNS server when the container starts
CMD ["python", "main.py"]
