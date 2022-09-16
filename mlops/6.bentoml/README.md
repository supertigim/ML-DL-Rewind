# BentoML 예제

## 환경 설정

```shell
poetry install
```

## 이전 실험의 내용 마이그레이션

```bash
python ./app/main.py 
bentoml serve MaskAPIService:latest --port 5001 
python -m streamlit run app/frontend.py
```
