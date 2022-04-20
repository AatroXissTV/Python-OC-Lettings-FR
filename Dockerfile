FROM python:3.10.2

WORKDIR /app
COPY requirements.txt /app/

# upgrade pip and install requirements.txt
RUN pip install --upgrade pip pip \
    && pip install -r requirements.txt

# copy project
COPY . /app/

# collect static files
RUN python manage.py collectstatic --noinput

# launch server
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
