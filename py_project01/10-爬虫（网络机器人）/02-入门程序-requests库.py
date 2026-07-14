# 👉 案例：获取 TIOBE 编程语言排行榜  
# https://www.tiobe.com/tiobe-index/
#
# 实现步骤：
#   1、查看 TIOBE 网站的 robots 协议文件，确认资源获取的规则。 https://www.tiobe.com/robots.txt
#   2. 安装 requests 库，发送请求获取网页内容. pip3 install requests
#   3. 编写 python 代码，访问 TIOBE 网站，获取网页内容。
#

import requests

# 1. 发送请求，获取网页内容
url = 'https://www.tiobe.com/tiobe-index/'
response = requests.get(url)
html_str = response.text

# 2. 打印网页内容
print(html_str)


# requests 库
# Requests 库是 Python 中最流行、最优雅的 HTTP 客户端库，让 Python 代码发送 HTTP 请求变得极其简单。


