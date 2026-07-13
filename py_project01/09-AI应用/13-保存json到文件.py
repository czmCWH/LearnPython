# 1、读写 JSON 格式文件
# JSON 是软件开发中最常用的数据交换格式，而为了简化 JSON 数据的处理，在 Python 标准库中就提供了处理 JSON 数据的核心模块 json。
#   - json.dump() 序列化，将 Python 对象编码成 JSON 数据格式，并将其写入到文件中。
#   - json.load() 反序列化，读取文件中的 JSON 数据解码为 Python 对象。

import json

def write_json():
    with open("./file/test_json.json", "w", encoding="utf-8") as f:
      user = {
          "name": "李白",
          "age": 30,
          "skills": ["编程", "写作"]
      }
      # 参数说明：
      #   - data：要写入的 Python 对象。
      #   - f：文件对象。
      #   - ensure_ascii：是否将非 ASCII 字符转义为 ASCII 码，默认为 True，会把中文转换为百分号编码，因此通常设置为False。
      #   - indent：缩进，默认为 None，表示不缩进。设置为数字时，表示缩进的空格数，美化输出。
      json.dump(user, f, ensure_ascii=False, indent=2)  # 序列化并写入文件

def read_json():
    with open("./file/test_json.json", "r", encoding="utf-8") as f:
      # 反序列化并获取 Python 对象
      data = json.load(f)
      print(type(data))  # <class 'dict'>
      print(data)

if __name__ == "__main__":
    write_json()
    read_json()