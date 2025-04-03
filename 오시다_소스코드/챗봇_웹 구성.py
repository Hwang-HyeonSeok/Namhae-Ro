# import
from openai import OpenAI
import openai
import streamlit as st

# OpenAI API 키 설정
api_key = ""

# ChatGPT 기본 모델 호출 함수
def ask_chatgpt1(question):

    # api key 지정
    client = OpenAI(api_key = api_key)

    # # API를 사용하여 'gpt-3.5-turbo' 모델로부터 응답을 생성합니다.
    response = client.chat.completions.create(
        model = 'gpt-3.5-turbo',
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},  # 기본 역할 부여
            {"role": "user", "content": question},                          # 질문
        ]
    )

    return response.choices[0].message.content

# 튜닝된 모델 호출 함수
def tunning_model(question):

    # api key 지정
    client = OpenAI(api_key = api_key)

    # # API를 사용하여 'gpt-3.5-turbo' 모델로부터 응답을 생성합니다.
    response = client.chat.completions.create(
        model="ft:gpt-4o-mini-2024-07-18:aivle::AmdMMDVB",
       # model = 'gpt-3.5-turbo',
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},  # 기본 역할 부여
            {"role": "user", "content": question},                          # 질문
        ]
    )

    return response.choices[0].message.content

# Streamlit UI
st.title("ChatGPT와 대화하기")
st.write("텍스트 입력창에 질문을 입력하면 ChatGPT가 응답합니다.")

# 사용자 입력
user_input = st.text_input("질문을 입력하세요:")

# 버튼 클릭 시 ChatGPT 호출(위 아래 중 하나 선택해서 주석 제거)
# gpt-3.5-turbo 기본 모델
# if st.button("응답 받기"):
#     if user_input.strip():  # 입력이 있는 경우에만 실행
#         with st.spinner("ChatGPT와 대화 중..."):
#             response = ask_chatgpt1(user_input)
#             st.text_area("ChatGPT의 응답:", response, height=200)
#     else:
#         st.warning("질문을 입력해주세요!")

# tunning model
if st.button("응답 받기"):
    if user_input.strip():  # 입력이 있는 경우에만 실행
        with st.spinner("ChatGPT와 대화 중..."):
            response = tunning_model(user_input)
            st.text_area("ChatGPT의 응답:", response, height=200)
    else:
        st.warning("질문을 입력해주세요!")
