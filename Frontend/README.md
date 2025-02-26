# MobileX Experience Lab - Frontend

## Requirements

- Poetry: `pip install poetry`

## Debug on my Local machine

```bash
# Install dependencies
poetry install --all-extras

# Run!
streamlit run 0_Home.py
```

## Build a Container image

```bash
tar -czh . | docker build --tag docker.io/{my docker account name}/{my image name}:{version} -
docker push docker.io/{my docker account name}/{my image name}:{version}

# Example:
tar -czh . | docker build --platform linux/amd64 --tag docker.io/1conatus/mobilex-exp-frontend:v0.8 -
docker push docker.io/1conatus/mobilex-exp-frontend:v0.8
```

### Build with buildx

```bash
tar -czh . | docker buildx build --push --pull --tag docker.io/{my docker account name}/{my image name}:{version} -

# Example:
tar -czh . | docker buildx build --push --pull --tag docker.io/kerryeon/mobilex-exp-frontend:v0.1 -
```
