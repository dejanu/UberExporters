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

* Cluster docker k8s cluster
```bash

kubectl config use  docker-desktop
kubectl create namespace monitoring
```

* Install Prometheus:

Go for full [kube prometheus](https://github.com/prometheus-operator/kube-prometheus) stack (prometheus operator, prometheus,node exporter,blackbox exporter) or just for [Prometheus operator](https://github.com/prometheus-operator/prometheus-operator?tab=readme-ov-file#helm-chart)

```bash
# install only the operator via helm https://github.com/prometheus-operator/prometheus-operator?tab=readme-ov-file#helm-chart
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install [RELEASE_NAME] prometheus-community/kube-prometheus-stack

# need for  lstat /var/log/pods/monitoring_prom-prometheus-node-exporter...no such file or directory error
helm install prom prometheus-community/kube-prometheus-stack -n monitoring --set prometheus-node-exporter.hostRootFsMount.enabled=false

# check grafana
# get password for admin user
kubectl -n monitoring get secrets prom-grafana -ojsonpath="{.data.admin-password}" | base64 -d
kubectl -n monitoring port-forward svc/prom-grafana 8088:80
```
* Monitor using k8s labels and Prometheus service monitor
```
# deploy go app (which does not exposes metrics)
kubectl create deployment webapp --image=dejanualex/gohello:1.0 --replicas=1
```