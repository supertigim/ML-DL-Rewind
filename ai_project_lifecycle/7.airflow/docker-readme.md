# Airflow Docker

## 실행 방법

- Docker 이미지를 직접 실행하는 방법과 Docker Compose를 사용하는 방법 2가지

## 1.Docker 이미지 직접 실행하는 방법

### Docker Network 생성하기

Airflow의 모든 컴포넌트가 Docker 컨테이너로 배포될텐데, 이 컨테이너들간의 통신할 네트워크를 먼저 생성

다음 명령어로 Docker Network를 생성

```bash
docker network create airflow

# 다음으로 확인
$ docker network ls
NETWORK ID     NAME      DRIVER    SCOPE
b8f5eb31452e   airflow   bridge    local
```

### Meta Database 사용하기

Meta Database로 PostgreSQL하며, Postgres 컨테이너에 Volume 마운트할 디렉토리 생성

```bash
mkdir data

#Postgres 컨테이너 실행
docker run \
  --name airflow-database \
  -d \
  --network airflow \
  -v $(pwd)/data:/var/lib/postgresql/data \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=admin \
  postgres:13

# 컨테이너가 제대로 실행되었는지 확인 
docker ps
```

### Meta Database 초기화 하기

다음 명령어로 Meta Database를 초기화

```bash
$ docker run \
  --name airflow-init \
  --network airflow \
  --entrypoint /bin/bash \
  -e AIRFLOW__CORE__SQL_ALCHEMY_CONN=postgresql+psycopg2://airflow:1234@airflow-database:5432/airflow \
  apache/airflow:2.2.3-python3.8 \
  -c " \
    airflow db init && \
    airflow users create \
      --username admin \
      --password admin \
      --firstname tigim \
      --lastname kim \
      --role Admin \
      --email abc@efg.com \
  "
```

### Scheduler 실행하기

다음 명령어로 Scheduler를 실행합니다

```bash
$ docker run \
  --name airflow-scheduler \
  --network airflow \
  -d \
  -e AIRFLOW__CORE__SQL_ALCHEMY_CONN=postgresql+psycopg2://admin:admin@airflow-database:5432/airflow \
  -e AIRFLOW__CORE__EXECUTOR=LocalExecutor \
  -v $PWD/dags:/opt/airflow/dags \
  apache/airflow:2.2.3-python3.8 \
  airflow scheduler

#컨테이너 실행 확인
docker ps
```

### Webserver 실행하기

다음 명령어로 Webserver를 실행합니다.

```bash
docker run \
  --name airflow-webserver \
  --network airflow \
  -d \
  -p 8080:8080 \
  -e AIRFLOW__CORE__SQL_ALCHEMY_CONN=postgresql+psycopg2://admin:admin@airflow-database:5432/airflow \
  -v $PWD/dags:/opt/airflow/dags \
  apache/airflow:2.2.3-python3.8 \
  airflow webserver

# 컨테이너 확인 
docker ps
```

#### Code Server 실행하기

Code Server는 VSCode의 Web Browser 버전입니다.
서버에 직접 접속하여 DAG 파일을 작성하지 않고, 이 Code Server를 이용하여 작성할 수 있도록 해봅시다.

다음처럼 Docker 컨테이너로 실행합니다. 이 때 `dags/` 디렉토리를 마운트합니다.

```bash
docker run -it --name code-server \
  --name airflow-code-server \
  -d \
  -v "$(pwd)/dags:/home/coder/project" \
  -p 8888:8888 \
  -e PASSWORD=admin \
  -e HOST=0.0.0.0 \
  -e PORT=8888 \
  codercom/code-server:4.0.2

# 컨테이너 확인 
docker ps
```

## 2.Docker Compose를 사용하는 방법

아래 명령어로 Docker Compose를 실행

```bash
docker-compose up

# 컨테이너 확인 
docker-compose ps
```

### Airflow Webserver 접속

브라우저에서 `http://localhost:8080`로 접속하며, 초기 계정 정보는 `admin` / `admin`

### Code Server 접속

`http://localhost:8888`에서 초기 비밀번호는 `admin`

`dags/` 폴더에서 Airflow DAG 파일을 생성하면 Airflow Webserver에서 확인 가능

만약 Code Server를 사용하지 않는다면, `$AIRFLOW_HOME/dags`에 파일을 옮기면 Airflow Scheduler가 파일을 파싱해 Airflow Webserver에서 확인 가능

## Reference

- [docker-compose.yml 참고](https://github.com/zzsza/Boostcamp-AI-Tech-Product-Serving/blob/main/part4/02-airflow/docker-compose.yml)
