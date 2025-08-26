# Stage 1: Build dependencies
FROM python:3.10-slim AS build

# Set the working directory
WORKDIR /app

# Install build dependencies, ensuring package lists are cleaned up
RUN apt-get update && \
    apt-get install -y --no-install-recommends python3-venv && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy only the requirements file first to take advantage of Docker's layer caching
COPY requirements.txt .

# Create the virtual environment and install dependencies in one step
# The venv must be installed to a persistent directory that will be copied later
RUN python3 -m venv /venv && \
    /venv/bin/pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Stage 2: Final runtime image
FROM python:3.10-slim

# Expose the application port
EXPOSE 8000

# Set the working directory
WORKDIR /app

# Copy the venv and application code from the build stage
COPY --from=build /venv /venv
COPY --from=build /app .

# Set the command to run the application using the virtual environment's Python
# The exec form of CMD is preferred for better signal handling
CMD ["/venv/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]
