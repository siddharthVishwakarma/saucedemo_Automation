# Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install Chrome and Chromedriver for Selenium
RUN apt-get update && apt-get install -y \
    chromium-chromedriver \
    chromium \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the test project into the container
COPY . .

# Set environment variable for headless mode
ENV HEADLESS true

# Default command: run the pytest suite
CMD ["pytest", "-q", "--disable-warnings", "--maxfail=1"]
