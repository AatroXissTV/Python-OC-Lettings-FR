FROM python:3.10-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV SENTRY_DSN $SENTRY_DSN
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 8000
RUN python manage.py collectstatic --noinput --clear
RUN python dumpdata -o data.json
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]