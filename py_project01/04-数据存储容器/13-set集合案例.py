# set 集合案例
# 根据提供的班级学生的选课情况, 完成如下需求:

# 选修足球学生名单
football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
# 选修篮球学生名单
baSketball_set = {"张铁", "墨居仁","王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
# 选修法语学生名单
french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子", "红蝶", "厉飞雨", "韩立", "曾牛"}
# 选修艺术学生名单
art_set = {"遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}


# 1、找出同时选修了法语和艺术的学生
# 方式1，求交集
s = french_set.intersection(art_set)
print("同时选修了法语和艺术的学生:", s)
# ⚠️ 方式2，求交集，使用 & 运算符，推荐！
s = french_set & art_set
print("同时选修了法语和艺术的学生:", s)

print("-----------------------------")

# 2、找出同时选修了所有四门课程的学生
s = football_set.intersection(baSketball_set).intersection(french_set).intersection(art_set)
print("同时选修了所有四门课程的学生:", s)
s = football_set & baSketball_set & french_set & art_set
print("同时选修了所有四门课程的学生:", s)

print("-----------------------------")

# 3、找出选修了足球, 但是没有选修篮球的学生

# 方式1，求差集
s = football_set.difference(baSketball_set)
print("选修了足球, 但是没有选修篮球的学生:", s)

# ⚠️ 方式2，求差集，使用 - 运算符，推荐
s = football_set - baSketball_set
print("选修了足球, 但是没有选修篮球的学生:", s)

# ⚠️ 方式3，集合推导式，语法：{表达式(要插入列表的元素) for 变量 in 可迭代对象 if 条件}
s = {s for s in football_set if s not in baSketball_set}
print("选修了足球, 但是没有选修篮球的学生:", s)

print("-----------------------------")

# 4、统计每一个学生选修的课程数量

# 方式1，.union() 函数，求并集，获取所有的学生名集合
# football_set.union(baSketball_set).union(french_set).union(art_set)

# 方式2，| 运算符，求并集，获取所有的学生名集合
# football_set | baSketball_set | french_set | art_set

for s in football_set | baSketball_set | french_set | art_set:
    count = 0
    if s in football_set:
        count += 1
    if s in baSketball_set:
        count += 1
    if s in french_set:
        count += 1
    if s in art_set:
        count += 1
    print("%s \t 选修了 %d 门课程" % (s, count))
else:
    print("统计完毕")