FROM python:3.8-slim

RUN pip install -U pip pipenv
COPY Pipfile* /
RUN pipenv install --deploy --system

CMD ["celery", "worker", "-A", "brreg2es.tasks", "-l", "info"]
