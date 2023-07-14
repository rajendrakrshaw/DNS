# DNS Server

This is a DNS server that performs complex math calculations based on the provided coordinates and velocity. It exposes an HTTP endpoint to receive DNS requests and returns the calculated location as a response.

## Requirements

- Python 3.9 or higher
- Docker (optional)

## Installation

1. Clone the repository:
```
  git clone https://github.com/your-username/dns-server.git
  cd dns-server
```
2. Install the dependencies:
```
  pip install -r requirements.txt
```

## Usage

1. Start the DNS server:
```
  python main.py
```
2. Send a DNS request using curl or any HTTP client:
```
  curl -X POST -H "Content-Type: application/json" -d '{
    "x": "123.12",
    "y": "456.56",
    "z": "789.89",
    "vel": "20.0"
  }' http://localhost:5000/dns
```
The response will be in JSON format, containing the calculated location.

## Docker Deployment

To deploy the DNS server using Docker, follow these steps:

1. Build the Docker image:
```
docker build -t dns-server .
```
2. Run the Docker container:
```
docker run -p 5000:5000 dns-server
```
The DNS server will be accessible at http://localhost:5000/dns

You can customize the Dockerfile as per your specific needs, such as including additional configurations, environment variables, or specifying a different port to expose.

## Testing

To run the test suite, use the following command:
```
python tests.py
```
