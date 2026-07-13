# 👉 1、Streamlit
# Streamlit 是一个开源的 Python 库，专为数据工程师及机器学习工程师设计，用来快速基于 Python 代码构建交互式的 web 网站（不需要懂任何前端技术）。
# 专门用于快速构建和分享数据科学、机器学习以及可视化相关的交互式 Web 应用。
# 官网：https://streamlit.io/
# 官方文档：https://docs.streamlit.io/
#
# 基本使用：
#   - 安装，终端执行：pip install streamlit
#   - 在 Python 文件中编写代码，并导入 streamlit
#   - 基于 Streamlit 提供的 API，编写交互式 web 组件
#   - 运行 Python 文件：streamlit run ./06-Streamlit.py 
#   - 访问 http://localhost:8501 查看效果

import streamlit as st

# 大标题
st.title('Streamlit 入门演示')
st.header('这是一个二级标题')
st.subheader('这是一个三级标题')


# 👉 2、Streamlit 基本使用
# 详细查看官方文档：https://docs.streamlit.io/develop/api-reference/write-magic

# 2.1、段落文字
st.write("《三国演义》全称《三国志通俗演义》，是中国古典四大名著之一，由明代小说家罗贯中在民间传说、话本与史书《三国志》的基础上创作而成。小说以东汉末年至西晋初年的历史为背景，生动描绘了魏、蜀、吴三国鼎立、群雄逐鹿的壮阔画卷。")
st.write("全书以“天下大势，分久必合，合久必分”开篇，围绕赤壁之战、官渡之战、夷陵之战等重大事件，塑造了曹操、刘备、孙权、诸葛亮、关羽、张飞、赵云、周瑜等一大批性格鲜明、深入人心的艺术形象。作品“七分实事，三分虚构”，既有金戈铁马的战争场面，也有运筹帷幄的智谋较量，更贯穿了“拥刘反曹”的仁政理想与忠义精神。")
st.write("作为历史演义小说的开山之作，《三国演义》语言半文半白，情节跌宕起伏，不仅深刻影响了后世文学与戏曲，更成为中国人集体记忆中的智慧宝库与英雄史诗。")

# 2.2、图片
st.image('./resources/卡通.jpeg', width=300)

# 2.3、音频
st.audio('./resources/月半小夜曲.mp3')

# 2.4、视频
st.video('./resources/风景.mp4')

# 2.5、logo，会一直显示在左上角
st.logo("./resources/logo.png")

# 2.6、表格
student_data = {
  "姓名": ["小明", "张三", "李四", "王五", "赵六"],
  "学号": ["001", "002", "003", "004", "005"],
  "年龄": [18, 20, 22, 19, 17],
  "成绩": [90, 85, 88, 92, 89]
}
st.table(student_data)

# 2.7、输入框
name = st.text_input("请输入你的名字：")
st.write(f"你好，{name}！")

pwd = st.text_input("请输入你的密码：", type="password")
st.write(f"你的密码是：{pwd}")

# 2.8、单选按钮
option = st.radio("你最喜欢的编程语言是？", ("Python", "Java", "C++"), index=1)
st.write(f"你的选择是：{option}")


# 👉 3、Streamlit 页面设置
# 参考官方文档：https://docs.streamlit.io/develop/api-reference/configuration/st.set_page_config

st.set_page_config(
    page_title="Streamlit 浏览器标题",
    # page_icon 设置浏览器标签的icon，可以使用 emoji 作为图标
    page_icon="🏀",
    # layout 设置页面布局，可选值：wide：示页面宽度会扩展到浏览器窗口的整个宽度；centered，表示页面居中显示；
    layout="centered",
    # initial_sidebar_state 设置侧边栏的初始状态，可选值：expanded、collapsed，表示展开或折叠
    initial_sidebar_state="expanded",
    # menu_items 设置右上角侧边栏的菜单项，可以自定义帮助文档、报告bug等链接
    menu_items={
        'Get Help': 'https://www.itcast.cn/',
        'Report a bug': "https://www.itcast.cn/",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)