
# PyTorch 공부

## 기본 PyTorch 구조  

    numpy + AutoGrad + DL Functions

## 맥에서 설치 방법

```bash
    # using conda
    $ conda create -n pytorch
    $ conda install pytorch torchvision -c pytorch
    $ conda install -n pytorch ipykernel --update-deps --force-reinstall 
```

## pytorch 프로젝트 생성

```bash

    # clone template project 
    % git clone https://github.com/victoresque/pytorch-template.git 
    % cd pytorch-template
    # create a new project from template
    % python new_project.py ../my_torch_project
    % cd ../my_torch_project
    # train the sample MNIST model 
    % python train.py -c config.json
```

## Reference

- [PyTorch Project Template](https://github.com/victoresque/pytorch-template#requirements)
