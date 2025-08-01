from dotenv import load_dotenv

load_dotenv()


import streamlit as st

from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

st.title("Lesson21:Streamlitアプリケーション by yukinobu")

st.write(" どちらかの専門家を選択し、入力フォームに相談を入力した後「実行」ボタンを押すことで専門家からの回答を得られます。")

st.divider()

st.write(" 法律 太郎: 法律の専門家")
st.write(" 知財 任三郎: 知財の専門家")

st.divider()

selected_item = st.radio(
    "相談したい専門家を選択してください。",
    ["法律 太郎", "知財 任三郎"]
)

st.divider()

input_message = st.text_input(label="選択した専門家に相談したい内容を入力してください。")




if st.button("実行"):
    st.divider()
    st.write("・・・回答まで10秒ほど、お待ちください")
    st.divider()


    if selected_item == "法律 太郎":
        #LLMのインスタンスを作成
        #モデル名はgpt-4o-miniを使用し、温度は0に
        llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

        messages = [

            SystemMessage(content="あなたは法律の専門家で、法律に関する質問に答えることができます。"),

            HumanMessage(content= input_message),

        ]

    elif selected_item == "知財 任三郎":
        llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

        messages = [

            SystemMessage(content="あなたは知財の専門家で、知財に関する質問に答えることができます。"),

            HumanMessage(content= input_message),

        ]

    result = llm(messages)

    st.write(result.content)
    # 出力結果を表示    