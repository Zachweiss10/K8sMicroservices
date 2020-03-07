#!/bin/bash
#start minikube
#macOS
minikube start --vm-driver=virtualbox


minikube addons enable ingress

eval $(minikube docker-env)


echo "Building Docker Image..."
sh build.sh
#docker run --name flasktestapp -p 5001:5001 flasktestapp


#Run in minikube
#creates port for outside of cluster communication
#imagepullpolic=Never ****Required for local images

echo "Running Docker Image on KCluster"
kubectl create -f deployment.yml
kubectl apply -f service.yml
kubectl apply -f pod.yml
kubectl apply -f ingress.yml

#Check that it's running
kubectl get pods

