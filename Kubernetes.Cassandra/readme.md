This project is based on: https://github.com/erangaeb/Scalable-Cassandra-deployment-on-Kubernetes

Advantages of Cassandra:

1. It's open-source.
2. It follows peer-to-peer architecture rather than master-slave architecture, so there isn't a single point of failure.
3. Cassandra can be easily scaled down or up.
4. It features data replication, so it's fault-tolerant and has high availability.

_____
> [!IMPORTANT] 
> MakeFile:
> ```
> make deploy
> ```


> [!NOTE] 
> ```
> helm plugin list
> ```
> -> secrets 2.0.2   This plugin provides secrets values encryption for Helm charts secure storing

____


Cassandra Deployment of Kubernetes;

MiniKube -> minikube is local Kubernetes, focusing on making it easy to learn and develop for Kubernetes.
```
minikube status
minikube start
```
> [!NOTE] 
> ```
> minikube dashboard
> ```
____

Leveraging Kubernetes concepts such as PersistentVolume and StatefulSets, we can provide a resilient installation of Cassandra and be confident that its data (state) are safe.

```
kubectl create -f cassandra-service.yaml
kubectl get svc cassandra

kubectl create -f local-volumes.yaml
kubectl get pv

The StatefulSet is responsible for creating the Pods.

kubectl create -f cassandra-statefulset.yaml
kubectl get statefulsets


kubectl delete persistentvolume cassandra-data-1
kubectl delete service cassandra -n default
```
____
```
helm install <full name override> <chart name>/ --values <chart name>/values.yaml
```

helm install cassandra cassandra/ --values cassandra/env/test/values.yaml

View all helm installations:

> [!NOTE]
> ```
> helm list
> ```

> [!NOTE]
> Information about specific installations:
> ```
> helm get all cassandra
> ```

Purging the old release:

> [!NOTE]
> helm uninstall release_name


1. Settings ENV Variables:

export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=cassandra,app.kubernetes.io/instance=cassandra" -o jsonpath="{.items[0].metadata.name}")


export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")

kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT




1. Get the application URL by running these commands:

```
kubectl describe pod cassandra-0
```

```
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=cassandra,app.kubernetes.io/instance=cassandra" -o jsonpath="{.items[0].metadata.name}")

  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")

  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
```
