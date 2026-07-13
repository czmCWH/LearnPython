# 案例 - 基于 Streamlit 构建 AI 智能伴侣
# 2、实现功能：
#   - AI 大模型会话记忆
# 当前与 AI 大模型的交互本质是无状态的，每一次请求响应都是相互独立的。（AI大模型本身没有真正的会话记忆能力）。
# 解决方案：
#   - 会话历史滚雪球：在调用 AI 大模型之前，将之前的所有消息都发送给大模型，让其具备会话记忆能力。
# 
# 测试验证：
#   - 12个苹果，3个人怎么分？
#   - 6个人怎么分？

import streamlit as st
import os 
from openai import OpenAI 

# 🎃 步骤1、设置页面配置信息
# 设置页面配置信息
st.set_page_config(
    page_title="AI 智能伴侣",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
    }
)

# 页面标题
st.title('AI 智能伴侣')
st.logo("./resources/robot_logo.png")

# 🎃 步骤2、Session State 缓存聊天消息
# https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state
# Session State 缓存的信息是到内存中的，并不会持久化到磁盘上，每次手动刷新页面，缓存信息会丢失。
# ⚠️：每次执行 st.chat_input 时，Streamlit 会重新执行整个 Python 文件，页面重新渲染，导致之前的聊天历史丢失。
print("<---------------> 重新执行此文件，渲染展示页面")
# 初始化 - 缓存所有聊天消息
if 'messages' not in st.session_state:
    st.session_state.messages = []

# 显示聊天历史
for message in st.session_state.messages:
    st.chat_message(message['role']).write(message['content'])

# 🎃 步骤3、聊天输入框，并发送消息到 AI 大模型，获取返回结果
# 系统提示词
system_prompt = """
你是一名非常可爱的AI助理，你的名字叫小甜甜，请你使用温柔可爱的语气回答用户的问题。
"""
# 创建与 DeepSeek API 交互的客户端对象。
client = OpenAI(
    # os.environ，拿到所有的环境变量；然后再获取 DEEPSEEK_API_KEY 环境变量对应的值。
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

# 聊天消息输入框
question = st.chat_input("请输入您要咨询的问题")

if question:    # ⚠️，字符串会自动转换为布尔值，非空字符串为True
    st.chat_message("user").write(question) # "user" 代表用户发送的消息，会自动显示在左侧，并带有头像
    st.session_state.messages.append({ "role": "user", "content": question, })
    # 调用 AI 大模型
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": system_prompt},
            # {"role": "user", "content": question}, 
            *st.session_state.messages, # ⚠️⚠️⚠️ 列表解包：滚雪球，将之前的所有消息都发送给大模型。
        ],
        stream=False,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )
    print("<--------------- 大模型返回结果: ", response.choices[0].message.content)
    st.chat_message("assistant").write(response.choices[0].message.content)
    st.session_state.messages.append({ "role": "assistant", "content": response.choices[0].message.content, })
    
