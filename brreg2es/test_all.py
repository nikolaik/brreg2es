from pathlib import Path

from brreg2es.tasks import download_latest


def test_download_file():
    out = download_latest()
    assert out
    p = Path(out)
    assert p.exists()
    assert p.suffix == 'json'
