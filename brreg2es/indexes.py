import json
from pathlib import Path

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

from brreg2es.settings import DATA_DIR, ELASTICSEARCH_URL

es_index_settings = {'settings': {'number_of_shards': 1, 'number_of_replicas': 0}}


def get_units(filename='enheter-2020-04-28.json'):
    with Path(DATA_DIR / filename).open() as fp:
        # FIXME: stream this
        units = json.load(fp)
        for u in units:
            yield {
                '_index': '2020-04-28',
                '_source': u
            }


def index_bulk(index_id='2020-04-28', force=True):
    es = Elasticsearch(ELASTICSEARCH_URL)
    if not es.indices.exists(index=index_id):
        es.indices.create(index_id, es_index_settings)

    bulk(es, get_units())
