# MLFlow 연습

## Docker로 MLFlow 띄우기

별개 없음!

```bash
docker build -t mlflow:1.24.0 .

docker images | grep mlflow

docker run --name mlflow -p 5000:5000 -v $(pwd):/mlflow --rm mlflow:1.24.0

```

## Docker Compose 로 하는 방법

```bash
docker-compose up
```
