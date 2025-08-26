FROM ubuntu:latest

WORKDIR /app

COPY . /app/

RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv python3-django

RUN . /app/ubuntuenv/bin/activate
# Create venv and install dependencies
#RUN python3 -m venv env && \
#    /app/env/bin/pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

# Use the python binary inside the virtual environment directly
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

