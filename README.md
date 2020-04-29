## brreg2es 📂
Index data from Enhetsregisteret (Brønnøysundregisteret) in Elasticsearch and keep updated.

### Installation

```shell script
docker-compose up
docker-compose run worker python -m brreg2es.run  # run index job
xdg-open http://localhost:5601  # open kibana dashboard
```

### Kibana setup
In Kibana you can explore and visualize the data. First you need to allow Kibana to create mappings by setting up an index pattern.

Use `*` as the index pattern and do NOT select a timeseries field.

## TODO:
- Fetch updates using https://data.brreg.no/enhetsregisteret/api/oppdateringer/enheter?dato=<iso8601 datetime>
- Index underenheter