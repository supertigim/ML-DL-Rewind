# AI Project Lifecyle로 알아보는 AI 프로젝트 서빙

## 1. Voila를 활용한 프로토타이핑

voila를 설치해서 쥬피터와 연동한다. 노트북 베이스로 빠른 프로토타이핑이 목표

```bash
  pip3 install voila
  pip3 install jupyterlab
  jupyter labextension install @jupyter-voila/jupyterlab-preview 
  jupyter serverextension enable voila --sys-prefix

  # voila/extension이 활성화 되었는지 체크
  jupyter nbextension list

  jupyter notebook 
  # 쥬피터 노트북 화면 상단에 실행 아이콘 생김
  # [주의] VSCODE로 하면 커널 죽는다
```

[느낀점] 편하다고 해서 한번 해봤는데, 아직은 쥬피터 노트북이면 충분할 듯. 개인적으로 가장 큰 문제는 VSCODE에서 정상 동작 안한다는 것. 뭔가 베타버전의 기술의 쓰는 느낌이어서 후에 안정화가 되면 써볼 생각

## 2. Streamlit

파이썬 코드 수정을 최소화하여 웹으로 구현 가능. 녹화 기능이 독특하다

```bash
  # 8501 포트로 실행 
  streamlit run sample_code.py
```

- @st.cache 데코레이터를 사용하여 캐싱하면 reload시 속도 개선

## 3. fastapi

flask에 비해 속도에 강점이 있는 웹프레임워크로 요즘 AI업계에서 핫한 아이템

### [pyenv와 poetry]

지금까지 써온 conda 대신 poetry와 pyenv로 환결 설정 해봄. 처음이라 잘 몰랐는데, poetry는 pyenv가 설정한 python 환경/버전에 완전 의존. 적절하게 설정해 두지 않기 때문에  

```bash
  # 파이썬 버전 설치
  pyenv install 3.10.0 

  # pyenv 버전 변경. 물론 설치가 되어 있어야 함. 삽잘한게 2022.07.29일 최신 파이썬은 3.10.5인데 fastapi 최신 버전이 지원하지 않는 버전이어서 설치가 안됨. 
  pyenv versions # 설치된 모든 버전 확인 
  pyenv global 3.10.0 

  # poetry에서 자주 쓰는 명령어
  poetry init # pyproject.toml 만든 것이라 해당 폴더에 있어야 함
  poetry install # toml에 정의된 모듈 설치 
  poetry shell # 가상 환경 띄우기 
  poetry add [모듈이름] # 새로운 모듈 추가 pip install 과 동일 
```

### How to run

```bash
make -j2 run_app
```

### 기타 파일 설명

- remove_poetry.py: poetry 사이트에서 긁어온 삭제 스크립트
- build_env_For_scipy.sh: 특정 버전 scipy 빌드를 하기위한 환경 변수 셋팅 (brew로 lapack, openblas를 먼저 설치해야함)
- Makefile: streamlit과 fastapi를 둘 다 run하기 위해 위에 코드

## Reference

- [Voila를 사용해 Jupyter Notebook Dashboard 만들기](https://zzsza.github.io/development/2020/01/06/jupyter_notebook_voila_dashboard/)
- [streamlit session state 사용법](https://blog.streamlit.io/session-state-for-streamlit/)
- [No BLAS/LAPACK libraries found when installing SciPy on macOS](https://stackoverflow.com/questions/69954587/no-blas-lapack-libraries-found-when-installing-scipy-on-macos/70880741)