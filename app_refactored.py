from dotenv import load_dotenv

load_dotenv()

import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage


def get_expert_system_message(expert_name):
    """専門家に応じたシステムメッセージを取得"""
    expert_messages = {
        "法律 太郎": "あなたは法律の専門家で、法律に関する質問に答えることができます。",
        "知財 任三郎": "あなたは知財の専門家で、知財に関する質問に答えることができます。"
    }
    return expert_messages.get(expert_name, "")


def create_llm_response(expert_name, user_message):
    """LLMを使用して専門家の回答を生成"""
    try:
        llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
        
        messages = [
            SystemMessage(content=get_expert_system_message(expert_name)),
            HumanMessage(content=user_message),
        ]
        
        result = llm(messages)
        return result.content
    except Exception as e:
        return f"エラーが発生しました: {str(e)}"


def main():
    """メイン関数"""
    st.title("Lesson21:Streamlitアプリケーション by yukinobu")

    # 説明文
    st.write("どちらかの専門家を選択し、入力フォームに相談を入力した後「実行」ボタンを押すことで専門家からの回答を得られます。")
    
    st.divider()
    
    # 専門家の紹介
    st.write("**法律 太郎**: 法律の専門家")
    st.write("**知財 任三郎**: 知財の専門家")
    
    st.divider()
    
    # 専門家の選択
    selected_expert = st.radio(
        "相談したい専門家を選択してください。",
        ["法律 太郎", "知財 任三郎"]
    )
    
    st.divider()
    
    # 相談内容の入力
    user_input = st.text_input(
        label="選択した専門家に相談したい内容を入力してください。",
        placeholder="ここに相談内容を入力してください..."
    )
    
    # 実行ボタン
    if st.button("実行"):
        if not user_input.strip():
            st.warning("相談内容を入力してください。")
            return
        
        st.divider()
        
        # ローディング表示
        with st.spinner("回答を生成中..."):
            response = create_llm_response(selected_expert, user_input)
        
        # 結果の表示
        st.success(f"**{selected_expert}**からの回答:")
        st.write(response)


if __name__ == "__main__":
    main()
