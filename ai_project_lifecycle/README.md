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

## Reference

- [Voila를 사용해 Jupyter Notebook Dashboard 만들기](https://zzsza.github.io/development/2020/01/06/jupyter_notebook_voila_dashboard/)
- [streamlit session state 사용법](https://blog.streamlit.io/session-state-for-streamlit/)