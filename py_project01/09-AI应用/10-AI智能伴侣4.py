# 案例 - 基于 Streamlit 构建 AI 智能伴侣
# 2、侧边栏功能
#   - AI 智能伴侣名字、性格定制，即设置 AI 大模型的系统提示词。

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

# 将系统提示词缓存到 session_state 中，以便在页面多次加载刷新时，保持缓存信息不变。
if "nick_name" not in st.session_state:
    st.session_state.nick_name = "小甜甜"
if "character" not in st.session_state:
    st.session_state.character = "活泼开朗的东北姑娘"

# 显示聊天历史
for message in st.session_state.messages:
    st.chat_message(message['role']).write(message['content'])

# 🎃 步骤3、侧边栏 - 系统提示词
system_prompt = """
你叫%s，现在是用户的真实伴侣，请完全代入伴侣角色。
规则:
  1. 每次只回1条消息
  2. 禁止任何场景或状态描述性文字
  3. 匹配用户的语言
  4. 回复简短，像微信聊天一样
  5. 有需要的话可以用🥰🌸等emoji表情
  6. 用符合伴侣性格的方式对话
  7. 回复的内容，要充分体现伴侣的性格特征

伴侣性格:
  - %s

你必须严格遵守上述规则来回复用户。
"""
 
# 左侧侧边栏
# st.sidebar.subheader("伴侣信息")
# st.sidebar.text_input("昵称：", value="小甜甜")
# st.sidebar.text_area("性格：", value="活泼开朗的东北姑娘", height=100)

with st.sidebar:  # with 是 streamlit 中的 context manager（上下文管理器），用于嵌套多个组件。
    st.subheader("伴侣信息")
    nick_name = st.text_input("昵称：", placeholder="请输入昵称", value=st.session_state.nick_name)
    if nick_name:
        st.session_state.nick_name = nick_name
    character = st.text_area("性格：", height=100, placeholder="请输入性格描述", value=st.session_state.character)
    if character:
        st.session_state.character = character

# 🎃 步骤4、聊天输入框，并发送消息到 AI 大模型，获取返回结果
# 创建与 DeepSeek API 交互的客户端对象。
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

# 聊天消息输入框
question = st.chat_input("请输入您要咨询的问题")

if question:   
    st.chat_message("user").write(question)
    st.session_state.messages.append({ "role": "user", "content": question, })
    # 调用 AI 大模型
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": system_prompt % (st.session_state.nick_name, st.session_state.character)},  # ⚠️ 系统提示词，设置 AI 大模型的角色
            *st.session_state.messages, # 列表解包：滚雪球，将之前的所有消息都发送给大模型。
        ],
        stream=True,  # ⚠️ 流式输出，实时返回结果
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )
    # 流式输出，实时返回结果
    response_message = st.empty()   # ⚠️ 创建一个空的容器占位，用于显示大模型返回的结果
    full_content = ""
    for chunk in response:
        # 流式输出，实时返回结果
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_content += content
            response_message.chat_message("assistant").write(full_content) 
    # 保存大模型返回的结果到缓存中
    st.session_state.messages.append({ "role": "assistant", "content": full_content, })