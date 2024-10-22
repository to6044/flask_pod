#!/bin/bash

# 스크립트 실행 중 오류 발생 시 중단
set -e

# 네임스페이스 설정
NAMESPACE="federated-learning"
DEPLOYMENT="fl-host-deployment.yaml"
SERVICE="fl-host-service.yaml"
CONFIG="fl-host-configmap.yaml"


# 네임스페이스 생성
kubectl create namespace $NAMESPACE || echo "Namespace $NAMESPACE already exists."

echo "Deploying Pod and Service..."
kubectl apply -f $DEPLOYMENT -n $NAMESPACE
kubectl apply -f $SERVICE -n $NAMESPACE
kubectl apply -f $CONFIG -n $NAMESPACE




# 모든 배포가 완료되었음을 알림
echo "Deployment completed. Check the pods and services using kubectl."

