# #
# FROM python:3.9
# ENV PYTHONUNBUFFERED=1
# WORKDIR /code
# COPY requirements.txt /code/
# RUN pip install -r requirements.txt
# COPY . /code/

# FROM python:3.8-slim-buster

# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1
# ENV PATH="/scripts:${./venv}"

# RUN pip install --upgrade pip

# COPY ./requirements.txt /requirements.txt

# RUN apt-get update
# RUN apt-get install -y --no-install-recommends sqlite3

# COPY . /app

# WORKDIR /app

# RUN pip install -r requirements.txt

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# new experiment start

# FROM python:3.8.5-alpine

# RUN pip install --upgrade pip

# COPY ./requirements.txt .
# RUN pip install -r requirements.txt

# COPY ./Samarth_Restaurant /app

# WORKDIR /app

# COPY ./entrypoint.sh /
# ENTRYPOINT ["sh", "/entrypoint.sh"]
# FROM python:3.8
# ENV PYTHONUNBUFFERED=1
# WORKDIR /app
# COPY . /app
# RUN pip install -r requirements.txt
# RUN python manage.py makemigrations
# RUN python manage.py migrate
# EXPOSE 8000
# CMD ["python","manage.py","runserver","0.0.0.0:8000"]

# FROM python:3.10-slim-buster

# # Set working directory
# WORKDIR /app

# # Copy the entire project directory
# COPY . /app

# # Install project dependencies
# RUN pip install -r requirements.txt

# # Expose port
# EXPOSE 8000

# # Run the development server
# CMD ["python", "Samarth_Restaurant/manage.py", "runserver", "0.0.0.0:8000"]

FROM python:3.10-slim-buster

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

VOLUME ["/app/db.sqlite3"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]