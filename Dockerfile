FROM python:3.10.12

WORKDIR /TarixManba

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENV TZ=Asia/Tashkent
ENV POSTGRES_DB=tarixmanba_db
ENV POSTGRES_USER=tarixmanba_user
ENV POSTGRES_PASSWORD=tarixmanba_password

COPY requirements.txt /TarixManba/
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /TarixManba/staticfiles
RUN chmod 755 /TarixManba/staticfiles

RUN mkdir -p /TarixManba/media
RUN chmod 755 /TarixManba/media

VOLUME /TarixManba/staticfiles
VOLUME /TarixManba/media

COPY . /TarixManba/

RUN python manage.py collectstatic --noinput

ENV DJANGO_SETTINGS_MODULE=Config.settings

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
