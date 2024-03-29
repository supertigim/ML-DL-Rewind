# Machine Learning 자료 모음

## Tips

1. 모델 변경 대신 HyperParameter 튜닝으로도 성능 개선 가능 (eg. 트리모델에서 오버핏팅을 방지하기 위해 깊이 제한을 한다거나, 하나의 리프에 하나의 데이터만 매칭 되지 않게 바꾼다거나...)
2. 트리 모델을 사용할 경우, 데이터의 Scale은 필요/효과 없음(다만, 다른 모델로 변경을 대비하여 해두는 것이 좋기는 함)
3. 파라미터최적화를 간단히 하려면 랜덤서치, Bayesian 최적화로 먼저 해보자 (그리드서치는 성능이 떨어진다는 논문있음, 근데 어디서 봤는지 기억안남, 그리고, BO가 왠간한 툴보다 좋다고 함)
4. skorch와 python 3.10 대버전이랑 안맞음. helper.py에서 **from collections.abc import Sequence**로 변경 필요
5. statsmodels 모듈 설치시, scipy 버전을 가능하면 최신으로 설정해야 한다.

```bash
    # pyproject.toml에서 
    
    python = ">=3.9.0,<3.11"
    scipy = "^1.9.0"
    statsmodels = "^0.13.2"
```

## Reference

- [Tree모델 Colab코드, 2022.03](https://colab.research.google.com/drive/1vtHHypHqm8LQDUgD7jV7cU9M_ywVfUms#scrollTo=QIuH96v55HVu)
- [위 코드 설명 자료, 2022.03](https://jehyunlee.github.io/2022/07/15/Python-DS-107-kierlecture4/220714_%EC%9D%B4%EC%A0%9C%ED%98%84_KIERML_2203_treemodels.pdf)
- [에너지기술연구원 머신러닝 세미나 유튜브](https://www.youtube.com/user/vinci109/videos)
- [PyCaret + Ray 조합으로 Bayesian Optimization, 2021.03](https://www.kdnuggets.com/2021/03/bayesian-hyperparameter-optimization-tune-sklearn-pycaret.html)
- [RMSLE or Root Mean Squared Log Error, 2020.07](https://ahnjg.tistory.com/90)
- [DecisionTreeRegressor 예제, 파라미터 최적화방법도 소개](DecisionTreeRegressor)
- [pycaret에서 search_library 중에서 tune-sklearn을 사용할 때 방법, 2021.06](https://data-newbie.tistory.com/755)
- [skorch: A scikit-learn compatible neural network library that wraps PyTorch.](https://github.com/skorch-dev/skorch)
- [pandas.get_dummies 대신 sklearn.preprocessing.OneHotEncoder를 쓰자](https://psystat.tistory.com/136)
- [libomp.dylib 문제 해결 at 맥북](https://shelling203.tistory.com/47)
- [Pandas: convert date 'object' to int](https://stackoverflow.com/questions/50863691/pandas-convert-date-object-to-int)
- [Time Series Forecasting - ARIMA](https://doheon.github.io/%EC%BD%94%EB%93%9C%EA%B5%AC%ED%98%84/time-series/ci-1.arima-post/)
- [pytest - 코드를 테스트 해봅시다](https://binux.tistory.com/47)
