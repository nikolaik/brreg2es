from celery import Celery

from brreg2es.downloads import download_latest as download_latest_sync
from brreg2es.indexes import index_bulk as index_bulk_sync

app = Celery('brreg2es')
app.config_from_object('brreg2es.celeryconfig')


@app.task()
def download_latest():
    return download_latest_sync()


@app.task()
def index_bulk():
    # This takes around 166 seconds
    index_bulk_sync()
