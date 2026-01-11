# Use official python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy all files to container
COPY . .

# Command to run python file
CMD ["python", "hotel_billing.py"]
