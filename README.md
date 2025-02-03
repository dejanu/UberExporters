# UberExporters
Prometheus exporter implementations

# Registries:

- [Dockerhub](https://hub.docker.com/)

# Docker images:

|  Image             | Registry                                                                     |
|--------------------|------------------------------------------------------------------------------|
| Grafana    9.5.2   |    https://hub.docker.com/repository/docker/rcc650/grafana/general           |
| Prometheus 2.48.0  |    https://hub.docker.com/repository/docker/rcc650/prometheus/general        |

## Start setup locally:

```bash
# check setup
docker-compose -f docker-compose.yaml config
# foreground
docker-compose -f docker-compose.yaml up
# background
docker-compose -f docker-compose.yaml up -d
```
🐱‍💻 Grafana should be accessible on [localhost:3000](http://127.0.0.1:3000) and Prometheus on [localhost:9090](http://127.0.0.1:9090)


## K8S setup

```bash
# use docker k8s cluster
kubectl config use  docker-desktop
```