# 👉 1、文件操作
# 文件操作分为3步：打开文件、读/写内容、关闭文件。

# - open() 函数打开文件，返回一个文件对象，通过该对象可以对文件进行操作。
#   编码：是将字符(文字、数字、符号)转换为计算机能够存储和处理的数字代码的规则系统，如:ASCII、GBK、UTF-8。

def write_file():
    # 步骤1：打开文件
    f = open("./file/test.txt", "w", encoding="utf-8")
    print(f)
    # 参数说明：⚠️⚠️⚠️
    # 1、文件名：要打开的文件名，如果文件不存在，则创建该文件。
    # 2、打开模式：指定打开文件的方式，如：r 读、w 写、a 追加等。进行 w、a 模式时，如果文件不存在，则会创建该文件。
    # 3、编码：指定文件的编码格式，如：utf-8、gbk等。

    # 步骤2：写内容
    # 写入文件
    # f.write("望庐山瀑布\n")
    # f.write("日照香炉生紫烟，\n")
    # f.write("遥看瀑布挂前川。\n")
    # f.write("飞流直下三千尺，\n")
    # f.write("疑是银河落九天。")

    f.writelines([
        "望庐山瀑布\n",
        "日照香炉生紫烟，\n",
        "遥看瀑布挂前川。\n",
        "飞流直下三千尺，\n",
        "疑是银河落九天。"
    ])

    # 步骤3：关闭文件，释放资源
    f.close()


def read_file():
    # 步骤1：打开文件
    f = open("./file/test.txt", "r", encoding="utf-8")
    print(f)

    # 步骤2：读内容
    # content = f.read()
    # print(content)
    list = f.readlines()
    for line in list:
        print(line, end="")  # end="" 表示不换行

    # 步骤3：关闭文件
    f.close()


def append_file():
    # 步骤1：打开文件
    f = open("./file/test.txt", "a", encoding="utf-8")

    # 步骤2：追加内容
    f.write("\n李白\n")

    # 步骤3：关闭文件
    f.close()



if __name__ == '__main__':
    write_file()
    read_file()
    append_file()


# 👉 2、正确释放文件资源
# 方式1，try...finally （不推荐，比较繁琐）
# 在 Python 中，可以使用 try...finally 语句来确保文件被正确关闭。
def safe_write_file():
    try:
        # 步骤1：打开文件
        f = open("./file/test.txt", "a", encoding="utf-8")

        # 步骤2：写内容 静夜思
        f.writelines([
            "\n\n",
            "静夜思\n",
            "床前明月光，\n",
            "疑是地上霜。\n",
            "举头望明月，\n",
            "低头思故乡。"
        ])
        
    finally:
        # 步骤3：关闭文件
        f.close()

# ⚠️ ⚠️ ⚠️ 方式2，with 语句 —— 推荐！
# with语句(上下文管理器)的核心作用，就是确保资源的总是被正确获取和释放(即使发生异常，也会被正确释放)，也是项目开发中的推荐方式。
def safe_write_file2():
    with open("./file/test.txt", "a", encoding="utf-8") as f:
        # 写内容，杜甫的《春夜喜雨》
        f.writelines([
            "\n\n",
            "春夜喜雨\n",
            "好雨知时节，当春乃发生。\n",
            "随风潜入夜，润物细无声。\n",
            "野径云俱黑，江船火独明。\n",
            "晓看红湿处，花重锦官城。"
        ])

if __name__ == '__main__':
    safe_write_file()
    safe_write_file2()