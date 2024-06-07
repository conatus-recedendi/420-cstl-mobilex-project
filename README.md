# MobileX Experience Lab

## kubernetes 서버 연결

1-1, 1-2 둘 중 하나만 세팅하세요.

## 1-1. Minikube 서버 배포

로컬에서 돌릴 때

```
minikube start
kubectl config current-context
```

minikube로 뜨면 성공

### 1-2. MobileX 서버 배포 방법

MobileX 서버에서 돌릴 때

```
mkdir -p ~/.kube
cp computer-system-team-30.yaml ~/.kube/config
chmod 700 ~/.kube
kubectl config current-context
```

computer-system-team 으로 뜨면 성공

## 2. Frontend

2-1, 2-2 순서대로 진행하세요

### 2-1. 프론트엔드 실행 방법

`pip install poetry`

`poetry install --all-extras`

`source .venv/bin/activate`

`streamlit run 0_Home.py`

주의! vscode라면, root 폴더가 /Frontend 이어야 함.

### 2-2. 프론트엔드 배포 방법

주의! tar 할 때, .venv 폴더는 제거해야 함.

`tar -czh . | docker build --platform linux/amd64 --tag docker.io/1conatus/mobilex-exp-frontend:v0.8 -`

`docker push docker.io/1conatus/mobilex-exp-frontend:v0.8`

```
kubectl apply -f frontend.yaml
kubectl get pods -l app=frontend
```

Running이라면 성공

## 3. 백엔드/LLM

3-1, 3-2 순서대로 진행하세요

### 3-1. 백엔드 실행 방법

`pip install poetry`

`poetry install -all-extras`

`source .venv/bin/activate`

`fastapi dev main.py`

### 3-2. 백엔드 배포 방법

주의! tar 할 때, .venv 폴더는 제거해야 함.

`tar -czh . | docker build --platform linux/amd64 --tag docker.io/1conatus/mobilex-exp-backend:v0.1 -`

`docker push docker.io/1conatus/mobilex-exp-backend:v0.1`

```sh
kubectl create secret generic openai --from-literal=OPENAI_API_KEY=your_openai_api_key_here
kubectl apply -f backend.yaml
kubectl get pods -l app=backend
```

Running이라면 성공
