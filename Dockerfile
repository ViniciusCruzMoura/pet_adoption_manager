FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["sh", "-c", " \
    python manage.py migrate ; \
    python manage.py collectstatic --noinput && \
    gunicorn --config gunicorn-cfg.py core.wsgi & \
    celery -A core worker --beat --scheduler django --loglevel=info --concurrency=1 \
"]