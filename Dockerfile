FROM python:3.10-slim


WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DJANGO_SUPERUSER_USERNAME=admin \
    DJANGO_SUPERUSER_EMAIL=admin@example.com \
    DJANGO_SUPERUSER_PASSWORD=changeme


EXPOSE 8000


CMD ["sh", "-c", "python manage.py migrate && \
                  echo \"from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser(username=os.environ['DJANGO_SUPERUSER_USERNAME'], email=os.environ['DJANGO_SUPERUSER_EMAIL'], password=os.environ['DJANGO_SUPERUSER_PASSWORD']) if not User.objects.filter(username=os.environ['DJANGO_SUPERUSER_USERNAME']).exists() else None\" | python manage.py shell && \
                  python manage.py runserver 0.0.0.0:8000"]
