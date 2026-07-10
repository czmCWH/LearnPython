# 👉 1、使用 Python 调用 DeepSeek API
#
# AI大模型通用请求参数：
#   system，表示给大模型设置的系统角色，即给大模型设置人设。如：你是一名非常可爱的AI助理，你的名字叫小甜甜，请你使用温柔可爱的语气回答用户的问题。
#   user，表示用户发送给大模型的提示词。 

# 👉 2、AI大模型 —— 没有会话记忆
# 通过 API 访问AI大模型时，与AI大模型的交互本质是无状态的，每一次请求响应都是相互独立的。AI大模型本身没有真正的会话记忆能力。
# 但是，我们可以通过一些手段来实现会话记忆。
#
# 会话记忆的实现方式：
# 方式1：会话历史滚雪球
#   实现 ：用户每次发送的提示词都保存下来，下一次请求时将历史对话拼接在一起发给大模型。

# 👉 3、代码实现，使用 DeepSeek API
# 通过前面的操作步骤，我们已经获得了DeepSeek API key。
# 参考官方示例代码，编写代码：https://api-docs.deepseek.com/zh-cn/
#
# ⚠️ PyPI: 全称 Python Package Index，是 Python 官方和社区共同维护的 Python 第三方软件包的官方仓库。
# pip：是 Python 官方提供的 Python 的包管理工具，提供了对 Python 包的安装、卸载、查询等功能。
#
# ⚠️ 配置 Python 环境变量
# 直接编辑 ~/.zshrc 文件，在最下面添加一行：`export DEEPSEEK_API_KEY=x`
# 终端执行，使配置立即生效：`source ~/.zshrc`
#

# 导入os模块，用于获取环境变量
import os 
# OpenAI 官方 Python SDK, 用于调用 DeepSeek API。需要先安装，在终端执行：pip3 install openai
from openai import OpenAI 

# 步骤1，创建与 DeepSeek API 交互的客户端对象。
client = OpenAI(
    # os.environ，拿到所有的环境变量；然后再获取 DEEPSEEK_API_KEY 环境变量对应的值。
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

# 步骤2，调用 DeepSeek API，与 AI 大模型进行交互。
response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[
        {"role": "system", "content": "你是一名非常可爱的AI助理，你的名字叫小甜甜，请你使用温柔可爱的语气回答用户的问题。"},
        {"role": "user", "content": "你是谁？你能帮我干什么？"},
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}}
)

# 步骤3，打印 AI 大模型返回的结果
print(response.choices[0].message.content)



# 👉 4、pip 包管理工具的使用
# 安装最新版本软件包：pip3 install openai
# 安装指定版本的软件包：pip3 install openai==0.27.8
# 卸载软件包：pip3 uninstall openai
# 列出已安装的软件包：pip3 list
# 查看软件包详情：pip3 show openai