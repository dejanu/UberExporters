# UberExporters
Prometheus exporter implementations

# Registries:

- [Dockerhub](https://hub.docker.com/)

# Docker images:

|  Image      | Registry                                                                     |
|-------------|------------------------------------------------------------------------------|
| Grafana     |    https://hub.docker.com/repository/docker/dejanualex/grafana/general       |
| Prometheus  |                                                                              |

* Start setup locally:

```bash
# check setup
docker-compose -f docker-compose config
# foreground
docker-compose -f docker-compose.yaml up
# background
docker-compose -f docker-compose.yaml up -d
```
🐱‍💻 Grafana should be accessible on (localhost:3000)[http://127.0.0.1:3000] and Prometheus on (localhost:9090)[http://127.0.0.1:9090]
