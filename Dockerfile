FROM ubuntu:latest

WORKDIR /app

COPY . /app/

RUN apt-get update && \
    apt-get install -y python3 python3-venv

#RUN . /app/ubuntuenv/bin/activate
# Create venv and install dependencies
RUN python3 -m venv env && \
    source env/bin/activate && \
    pip3 install --no-cache-dir -r requirements.txt

FROM python:3.10-slim

EXPOSE 8000

ENTRYPOINT ["python3"]
# Use the python binary inside the virtual environment directly
CMD ["manage.py", "runserver", "0.0.0.0:8000"]

