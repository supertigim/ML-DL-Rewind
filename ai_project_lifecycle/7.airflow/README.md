# Airflow 사용법 간단 정리

## Airflow 실행 방법

```bash
poetry shell
#export AIRFLOW_HOME=.
export AIRFLOW_HOME=~/workspace/ML-DL-Rewind/ai_project_lifecycle/7.airflow
export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES

airflow db init
airflow users create --username admin --password admin --firstname tigim --lastname kim --role Admin --email abc@def.com

# airflow web 서버 구ㅇ
airflow webserver --port 8080

# 다른 CLI에서 엔진 기동
airflow scheduler
```

## Reference

- [Docker로 사용하기](https://github.com/zzsza/Boostcamp-AI-Tech-Product-Serving/blob/main/part4/02-airflow/docker-readme.md)
- [Apache Airflow Tutorials for Beginner](https://heumsi.github.io/apache-airflow-tutorials-for-beginner/)
- [Apache Airflow 기반의 데이터 파이프라인](http://www.yes24.com/Product/Goods/107878326)
- [Fix - Task exited with return code Negsignal.SIGABRT](https://stackoverflow.com/questions/66012040/task-exited-with-return-code-negsignal-sigabrt-airflow-task-fails-with-snowflak)
