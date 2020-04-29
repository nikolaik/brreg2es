## brreg2es 📂
Index data from Enhetsregisteret (Brønnøysundregisteret) in Elasticsearch and keep updated.

### Installation

```shell script
docker-compose up
docker-compose run worker python -m brreg2es.run  # run index job
xdg-open http://localhost:5601
```

## TODO:
- Fetch updates using https://data.brreg.no/enhetsregisteret/api/oppdateringer/enheter?dato=<iso8601 datetime>
- Index underenheter