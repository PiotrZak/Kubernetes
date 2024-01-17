
Helm is a package manager for Kubernetes that streamlines the deployment and management of applications, while Minikube is a tool that enables running Kubernetes clusters locally for development and testing purposes.



## Open Kubernetes Dashboard:

kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.7.0/aio/deploy/recommended.yaml



## 

- `kubectl get all,cm,secret,ing -A`

displays:

pod
service
daemonset
deployment
replicaset
statefulset
job
configmap
secret
ingress

- `kubectl get pods,svc,secrets`

## Instructions for creating a local cluster

### Starting Up K8s

- `minikube start --driver docker --insecure-registry="10.0.0.0/8"` : Start your local K8s cluster allowing insecure (local registery) using network mask from ipconfig
- `minikube addons enable ingress` : Enable ingress for accessing the cluster
- `kubectl get pods -n ingress-nginx` : Check ingress has started
- `kubectl delete all --all -n  <namespace>` : Remove all resources in the given namespace
- `minikube service <serviceName> -n <namespace>` : Open exposed service through minikube

### Manual K8s configuration (without Helm)

- `kubectl create namespace demo-app` : Create a new K8s namespace in your local cluster
- `kubectl apply -f serviceAccount.yml -n demo-app` : Create service account in given namspace
- `kubectl apply -f serviceAccountSecret.yml -n demo-app` : Create service account secret
- `kubectl create rolebinding demo-app-admin --clusterrole=cluster-admin --serviceaccount=default:demo-app-service-account --namespace=demo-app` : Create admin role
- `kubectl describe secrets/demo-app-service-account-secret` : Get service account secret key and copy it into the kube config yml file

### Starting Up Docker

- `docker pull registry` : Pull Docker registry image
- `docker run -d -p 5000:5000 --restart=always --name registry registry:latest` : Start local Docker registry
- `docker build . -f Dockerfile-JobConsole.yml -t localhost:5000/job-console` : Create a new image of the JobConsole with the prefix of localhost so when we push it will go to the locally hosted Docker registry
- `docker push localhost:5000/job-console` : Push image created above to the registry
- `docker image remove localhost:5000/job-console` : Remove locally cached image
- `docker pull localhost:5000/job-console` : Check you can pull the image from your local registry
- Repeat for the API dockerfile, calling the image localhost:5000/demo-app

### Helm

* `helm create demo-app-api` : Creates a basic Helm chart layout
* `helm install <install-name> <path-to-chart>` : Install a chart, the path must point to the root Helm dir which holds both templates and charts sub dirs
  * e.g. `helm install test-chart ./thisChart`
* `helm install --debug --dry-run <release-name> <path-to-chart>` : Render a chart to the terminal to check the values
* `helm get manifest <release-name>` : Prints out all the resources for the given Helm release
* `helm uninstall <release-name>` : Uninstall the given Helm release
