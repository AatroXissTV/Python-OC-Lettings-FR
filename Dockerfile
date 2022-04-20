FROM python:3.10-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV SENTRY_DSN $SENTRY_DSN
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install psycopg2-binary==2.8.6
COPY . /app
EXPOSE 8000
RUN python manage.py collectstatic --noinput --clear
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]