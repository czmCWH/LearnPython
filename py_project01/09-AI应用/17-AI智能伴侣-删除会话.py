# 1、会话管理 —— 优化
#   - 会话历史排序；
#   - 添加分割线；
# 

import streamlit as st
import os 
from openai import OpenAI 
from datetime import datetime
import json

def generate_session_id():
    """生成会话ID"""
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S") # ⚠️ 获取当前系统时间

def save_session():
    """
    保存当前会话的消息记录到磁盘文件中。
    """
    if st.session_state.session_id:
        session_data = {
            "messages": st.session_state.messages,
            "nick_name": st.session_state.nick_name,
            "character": st.session_state.character,
            "session_id": st.session_state.session_id
        }
        # 如果 sessions 目录不存在，则创建
        if not os.path.exists("sessions"):
            os.mkdir("sessions")
        # 保存会话到磁盘文件中
        with open(f"sessions/{st.session_state.session_id}.json", "w", encoding="utf-8") as f:
            json.dump(session_data, f, ensure_ascii=False, indent=2)

def load_sesssion_list():
    """
    加载历史会话列表。即，会话文件名列表。
    """
    session_list = []
    if os.path.exists("sessions"):
        file_list = os.listdir("sessions")  # 加载 sessions 目录下的所有文件
        for fileName in file_list:
            if fileName.endswith(".json"):
                session_list.append(fileName[:-5])  # 去掉文件名后缀 .json，只保留文件名，添加到会话列表中
         # 按会话时间倒序排序
        session_list.sort(reverse=True) 
    return session_list

def load_session(session_id):
    """
    加载指定会话的消息记录。
    """
    try:
        if os.path.exists(f"sessions/{session_id}.json"): # 如果会话文件存在，则加载会话信息
            with open(f"sessions/{session_id}.json", "r", encoding="utf-8") as f:
                session_data = json.load(f)
                st.session_state.messages = session_data['messages']
                st.session_state.nick_name = session_data['nick_name']
                st.session_state.character = session_data['character']
                st.session_state.session_id = session_data['session_id']
    except Exception as e:
        st.error(f"加载会话失败：{e}")

def remove_session(session_id):
    """删除指定会话文件。"""
    try:
        if os.path.exists(f"sessions/{session_id}.json"):
            os.remove(f"sessions/{session_id}.json")
            # 如果删除的是当前会话，则需要清空消息列表
            if session_id == st.session_state.session_id:
                st.session_state.messages = []
                st.session_id = generate_session_id()  # 重新生成会话ID
            st.success("会话已删除！")
    except Exception as e:
        st.error(f"删除会话失败：{e}")

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

# 缓存会话ID
if "session_id" not in st.session_state:
    st.session_state.session_id = generate_session_id()

# 会话名称
st.text(f"会话名称：{st.session_state.session_id}")

# 显示聊天历史
for message in st.session_state.messages:
    st.chat_message(message['role']).write(message['content'])

# 🎃 步骤3、侧边栏 

# 系统提示词面板
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
    # 1、AI 会话面板
    st.subheader("AI控制列表")
    
    # 1.1、新建会话
    if st.button("新建会话", width="stretch", icon="✏️"):   #  点击按钮，返回 True，否则返回 False
        # 1、保存当前会话
        save_session()
        # 2、创建新的会话，如果消息列表非空，则创建新的会话
        if st.session_state.messages:
            # 清空当前会话的消息记录
            st.session_state.messages = []
            st.session_state.session_id = generate_session_id()
            # 保存新建会话
            save_session()
            # 刷新当前页面
            st.rerun()
    
    # 1.2、加载历史会话
    st.text("会话历史：")
    session_list = load_sesssion_list()
    for session_id in session_list:
        # 设置行布局：会话ID按钮、删除按钮
        col1, col2 = st.columns([4, 1])
        with col1:
            # ⚠️⚠️⚠️  三元运算符语法：值1 if 条件 else 值2
            if st.button(session_id, width="stretch", icon="📄", key=f"load_{session_id}", type="primary" if st.session_state.session_id == session_id else "secondary"):
                # 点击会话ID按钮，加载指定会话的内容
                load_session(session_id)
                st.rerun()  # 重新执行当前文件，渲染展示页面
        with col2:
            if st.button("",  width="stretch", icon="❌️", key=f"delete_{session_id}"):
                # 点击删除按钮，删除会话
                remove_session(session_id)
                st.rerun()  # 重新执行当前文件，渲染展示页面

    # 分割线，用于分隔左侧侧边栏的两个面板
    st.divider()

    # 2、伴侣信息面板
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
    st.session_state.messages.append({ "role": "assistant", "content": full_content,})
    # 保存会话
    save_session()
