import gzip
import logging
import shutil
from datetime import datetime
from pathlib import Path

import requests

from brreg2es.settings import DATA_DIR

logger = logging.getLogger('brreg2es')


def download_latest():
    """Ref: https://data.brreg.no/enhetsregisteret/api/docs/index.html#_eksempel_1_last_ned_alle_enheter_i_json_format"""
    url = 'https://data.brreg.no/enhetsregisteret/api/enheter/lastned'
    headers = {'Accept': 'application/vnd.brreg.enhetsregisteret.enhet.v1+gzip;charset=UTF-8'}
    local_gz_file = Path(f'{DATA_DIR}/enheter-{datetime.now().date().isoformat()}.json.gz')
    download_file(url, local_gz_file, headers=headers)
    local_file = decompress(local_gz_file)
    return str(local_file)


def download_file(url, local_file: Path, **kwargs):
    if local_file.exists():
        logger.warning(f'Local file {local_file} already exists, skipping.')
        return

    with requests.get(url, stream=True, **kwargs) as res:
        res.raise_for_status()
        with local_file.open('wb') as fp:
            shutil.copyfileobj(res.raw, fp)


def decompress(local_file):
    new_file = Path(DATA_DIR / local_file.stem)
    if new_file.exists():
        logger.warning(f'Local file {new_file} already exists, skipping.')
        return

    with gzip.open(local_file, 'rb') as f_in:
        with new_file.open('wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

    return new_file
