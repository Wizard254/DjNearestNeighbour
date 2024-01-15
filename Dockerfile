# app/Dockerfile

FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/Wizard254/DjNearestNeighbour.git .

RUN pip3 install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate

EXPOSE 9090

#HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:9090"]
