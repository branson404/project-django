FROM python:3.10-slim AS build

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends python3-venv && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN python3 -m venv /venv && \
    /venv/bin/pip install --no-cache-dir -r requirements.txt

COPY . .

# Stage 2
FROM python:3.10-slim

EXPOSE 8000

WORKDIR /app

COPY --from=build /venv /venv
COPY --from=build /app .

CMD ["/venv/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]
