# -*- coding: utf-8 -*-
import streamlit as st
import io
import os
import yaml
from PIL import Image
from predict import load_model, get_prediction
from confirm_button_hack import cache_on_button_press

# SETTING PAGE CONFIG TO WIDE MODE
st.set_page_config(layout="wide")
root_password = 'password'

def main() -> None:
    st.title("Mask Classification Model")

    # 1. 모델 로드
    with open("config.yaml") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    
    model = load_model()
    model.eval()

    # 2. stremlit 파일 업로더
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg","png"])

    # 3. 파일이 업로드 되면 화면 출력 
    if uploaded_file:
        image_bytes = uploaded_file.getvalue()
        image = Image.open(io.BytesIO(image_bytes))

        st.image(image, caption='Uploaded Image') # 이미지 출력 

        # 4. Prediction 
        st.write("Classifying...")
        _, y_hat = get_prediction(model, image_bytes)
        label = config['classes'][y_hat.item()]

        # 5. 결과 출력 
        st.write(f'label is {label}')

@cache_on_button_press('Authenticate')
def authenticate(password) ->bool:
    '''
        화면 Password 설정하기 
    '''
    st.write(type(password))
    return password == root_password

if __name__ == '__main__':
    password = st.text_input('password', type="password")
    if authenticate(password):
        st.success('You are authenticated!')
        main()
    else:
        st.error('The password is invalid.')