FROM python:3.10-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV SENTRY_DSN $SENTRY_DSN
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python3 manage.py collectstatic --noinput --clear
RUN python3 dumpdata -o data.json
COPY . /app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]