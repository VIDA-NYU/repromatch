FROM debian:jessie

RUN apt-get update && \
    apt-get install -y python python-virtualenv python-dev build-essential \
        libjpeg-dev zlib1g-dev libxml2-dev libxslt-dev \
        openjdk-7-jre-headless
WORKDIR /repromatch
COPY requirements.txt /repromatch/
RUN virtualenv /venv && . /venv/bin/activate && \
    export CFLAGS=-I/usr/include/libxml2 && \
    pip install -r requirements.txt
COPY manage.py project.db runsolr.sh /repromatch/
COPY apache-solr-3.5.0 /repromatch/apache-solr-3.5.0
COPY repromatch /repromatch/repromatch
COPY tools /repromatch/tools
RUN sed -i "s/SECRET_KEY = ''/SECRET_KEY='$(dd if=/dev/urandom bs=3 count=15 | base64 | sed 's/[\/]//g')'/" repromatch/settings.py
RUN echo 'urlpatterns = patterns("", (r"^static/(?P<path>.*)$", "django.views.static.serve", {"document_root": settings.BASE_DIR + "/repromatch/static"})) + urlpatterns' >>repromatch/urls.py
CMD ["/bin/sh", "-c", "./runsolr.sh & . /venv/bin/activate && ./manage.py runserver 0.0.0.0:8000"]
EXPOSE 8000
