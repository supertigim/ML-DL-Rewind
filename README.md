# Machine Learning and Deep Learning Rewind in 2022

아는 것 정리하기, 앞으로 공부할 것 정리하기

## Colab 사용 하기  

```python  
    # 현재 위치 
    import os 
    print(os.getcwd())
    !ls

    # 구글 드라이드 활용 - 접근 허가를 묻는 창이 뜬다. ok해주면 됨
    from google.colab import drive 
    drive.mount('./MyDrive')

    cd MyDrive/MyDrive
    ls                      # 구글 드라이드 내용 출력됨 

    cd Colab                # 여기다 만들어서 난 쓴다 (Optional)

```

```bash 
    # 추가적으로 해주면 좋은 작업 
    
    # Step 1. Matplotlib 업그레이드
    !pip install matplotlib -U 
    !pip install seaborn -U
    !pip install pandas -U

    # Step 2. 한글 설치 및 사용 설정
    !apt-get -qq install -y fonts-nanum
    !fc-cache -fv  
    !rm ~/.cache/matplotlib -rf

    # Step 3. 셀 실행 후 런타임 재시작
```

## 잘 까먹는 명령어

```bash

# 기본 가상 환경. 공식 문서도 버린...
python -m venv .venv
source .venv/bin/activate

# 사용하는 모듈 freeze 하기 
pip list --not-required --format=freeze > requirements.txt 

# 도커 실행 
docker run -it --name 컨테이너이름(ps로 찾는이름) -e 환경변수 -d -p 8888:8888 -v /local/folder/:/container/folder 이미지이름(템플릿)

# 도커 접근 (ssh 형태)
docker exec -it 컨테이너이름 /bin/bash

```

## 자주 방문하는 사이트

- [Browse State-of-the-Art](https://paperswithcode.com/sota)
- [SuperGLUE Leaderboard](https://super.gluebenchmark.com/leaderboard)
- [Object Detection on COCO test-dev](https://paperswithcode.com/sota/object-detection-on-coco)
- [캐글 코드](https://www.kaggle.com/code)
- [Annotation Tools 모음](https://github.com/zenml-io/awesome-open-data-annotation?fbclid=IwAR1pdaoWWHDZLFDU8u7xCYOrrJaWYDSwjfGDaDSHgVHYKbVeJW6BPqtUdTY)

## 볼만한 논문 설명 or 코드 예제

(updated in 2022.07.20)

- [Implementing Visual Transformer in PyTorch](https://github.com/FrancescoSaverioZuppichini/ViT)
- [Transformer 설명 및 간단 한글 챗봇 만들기](https://wikidocs.net/31379)
- [해외 프로축구 선수 예제로 설명한 Node2Vec 노트북](https://github.com/eliorc/Medium/blob/master/Nod2Vec-FIFA17-Example.ipynb)
- [차원축소 방법 비교: PCA, t-SNE, AutoEncoder](https://github.com/eliorc/Medium/blob/master/PCA-tSNE-AE.ipynb)
- [MNIST로 알아보는 비지도 학습: K-Means(with PCA), t-SNE with DBSCAN, AutoEncoder](https://yamalab.tistory.com/118)
- [It’s NeRF From Nothing: Build A Complete NeRF with PyTorch](https://towardsdatascience.com/its-nerf-from-nothing-build-a-vanilla-nerf-with-pytorch-7846e4c45666)
- [NeRF From Nothing - 위 블로그 colab](https://colab.research.google.com/drive/1TppdSsLz8uKoNwqJqDGg8se8BHQcvg_K?usp=sharing#scrollTo=vUI5BA9BXlTm)
- [D-NeRF 데이터셋](https://www.dropbox.com/s/0bf6fl0ye2vz3vr/data.zip?dl=0)

## dataset

- [캐글 데이터셋](https://www.kaggle.com/datasets)
- [허킹페이스 데이터셋](https://huggingface.co/datasets)
- [seaborn.load_dataset 사용을 위한 샘플 데이터 레포지토리](https://github.com/mwaskom/seaborn-data)
- [scikit-learn dataset 종류](https://scikit-learn.org/stable/datasets.html)
- [유명인 이미지 모음 | CelebA: 캐나다에서 FaceID 프로젝트 할 때 사용한 데이터셋](https://datagen.tech/guides/image-datasets/celeba/)

## Reference  

- [업스테이지](https://www.youtube.com/channel/UCXJY5PPAToqqSketm5_PrDw/videos)
- [마크다운 수식 TeX 문법](https://velog.io/@d2h10s/LaTex-Markdown-%EC%88%98%EC%8B%9D-%EC%9E%91%EC%84%B1%EB%B2%95)
- [Check if this is a path](https://m.blog.naver.com/monkey5255/221758850260)
- [python web scraping request error](https://stackoverflow.com/questions/61968521/python-web-scraping-request-errormod-security)
- [notMNIST download site](http://yaroslavvb.com/upload/notMNIST/)
- [py_remote_extract_tar_gzip.py](https://gist.github.com/devhero/8ae2229d9ea1a59003ced4587c9cb236)
- [Colab 이용방법, 환경설정 등](https://theorydb.github.io/dev/2019/08/23/dev-ml-colab/)
- [Tensorboard add image](https://stackoverflow.com/questions/67094398/assertionerror-size-of-input-tensor-and-input-format-are-different-tensorboa)
- [How to use Multi-GPU](https://medium.com/huggingface/training-larger-batches-practical-tips-on-1-gpu-multi-gpu-distributed-setups-ec88c3e51255)
- [쥬피터 단축키 모음](https://kkokkilkon.tistory.com/151)
- [Docker run 옵션 종류](https://wooono.tistory.com/348)
- [Can't push image to google container registry - Caller does not have permission 'storage.buckets.get'](https://stackoverflow.com/questions/51873072/cant-push-image-to-google-container-registry-caller-does-not-have-permission)
