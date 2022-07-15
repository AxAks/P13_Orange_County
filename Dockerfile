FROM python:3.9

RUN groupadd app && useradd -g app app
RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

USER app
CMD python manage.py runserver 0.0.0.0:8000