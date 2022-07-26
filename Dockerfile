FROM python:3.9

RUN groupadd app && useradd -g app app
RUN mkdir /app
WORKDIR /app

COPY . /app/
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN chown -R app:app /app/

USER app
EXPOSE 8000

CMD gunicorn oc_lettings_site.wsgi --log-file - --log-level error --reload False