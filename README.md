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

```python 
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

## 주기적으로 방문하는 사이트

- [Object Detection on COCO test-dev](https://paperswithcode.com/sota/object-detection-on-coco)

## 볼만한 논문 설명 or 코드 예제

(updated in 2022.07.20)

- [Implementing Visual Transformer in PyTorch](https://github.com/FrancescoSaverioZuppichini/ViT)
- [Transformer 설명 및 간단 한글 챗봇 만들기](https://wikidocs.net/31379)
- [해외 프로축구 선수 예제로 설명한 Node2Vec 노트북](https://github.com/eliorc/Medium/blob/master/Nod2Vec-FIFA17-Example.ipynb)
- [차원축소 방법 비교: PCA, t-SNE, AutoEncoder](https://github.com/eliorc/Medium/blob/master/PCA-tSNE-AE.ipynb)
- [MNIST로 알아보는 비지도 학습: K-Means(with PCA), t-SNE with DBSCAN, AutoEncoder](https://yamalab.tistory.com/118)

## dataset

- [seaborn.load_dataset 사용을 위한 샘플 데이터 레포지토리](https://github.com/mwaskom/seaborn-data)
- [scikit-learn dataset 종류](https://scikit-learn.org/stable/datasets.html)

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
