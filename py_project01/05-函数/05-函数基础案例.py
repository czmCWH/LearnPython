# 案例1
# 定义一个函数：根据传入的底和高计算三角形面积的函数(三角形面积=底*高/2)。
def triangle_area(bottom, height):
    """
    计算三角形面积的函数
    :param bottom: 底
    :param height: 高
    :return: 三角形面积
    """
    return bottom * height / 2

print("底长为30，高为20的三角形面积为：", triangle_area(30, 20))

print("-------------------------")

# 案例2 
# 定义一个函数：计算传入的字符串中元音字母的个数(元音字母为 aeiouAEIoU)。
def count_vowels(s):
    """
    计算字符串中元音字母的个数
    :param s: 输入的字符串
    :return: 元音字母的个数
    """
    # 1、定义元音字母集合
    vowels = "aeiouAEIoU"
    count = 0
    # 2、遍历字符串，判断每个字符是否在元音字母集合中
    for char in s:
        if char in vowels:
            count += 1
    return count

print("统计 hello world 中元音字母的个数为：", count_vowels("hello world"))

print("-------------------------")

# 案例3 
# 定义一个函数：计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分(保留1位小数)，并返回。
def calculate_scores(grades):
    """
    计算成绩的最高分、最低分和平均分
    :param grades: 高考成绩列表
    :return: (最高分, 最低分, 平均分)
    """
    # 1、初始化最高分和最低分为第一个成绩，平均分为0
    max_grade = max(grades)
    min_grade = min(grades)
    average_score = round(sum(grades) / len(grades), 1)
    return max_grade, min_grade, average_score

max_s, min_s, avg_s = calculate_scores([650.5, 676, 689, 691, 769])
print("最高分为：", max_s)
print("最低分为：", min_s)
print("平均分为：", avg_s)