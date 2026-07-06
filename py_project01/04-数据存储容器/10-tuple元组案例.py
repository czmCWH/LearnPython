# 案例1
# 根据提供的学生成绩单，完成如下需求:
scores = (("s001", "王林", 85, 92, 78), 
          ("s002", "李新", 92, 88, 95), 
          ("s003", "石分", 78, 85, 82),
          ("s004", "张飞", 88, 97, 91),
          ("s005", "赵云", 95, 96, 89),
          ("s006", "刘备", 76, 82, 77),
          ("s007", "关羽", 89, 91, 94),
        )

# 1、计算每个学生的总分、各科平均分，然后一并输出出来。
print("学号\t姓名\t总分\t平均分")

# 方式1
# for s in scores:
#     total = s[2] + s[3] + s[4]
#     avg = total / 3
#     print(f"{s[0]} \t {s[1]} \t {total} \t {avg:.2f}")    # ⚠️，{avg:.2f} 保留两位小数

# 方式2，元组解包
for id, name, *score in scores:
    total = sum(score)
    avg = total / len(score)
    print(f"{id}\t{name}\t{total}\t{avg:.2f}")

print("---------------------------------")

# 2、统计各科成绩的最低分、最高分、平均分，并输出。
chinese = [s[2] for s in scores]
math = [s[3] for s in scores]
english = [s[4] for s in scores]
print(f"语文最高分:{max(chinese)}，最低分:{min(chinese)}， 平均分:{(sum(chinese)/len(chinese)):.2f}")
print(f"数学最高分:{max(math)}, 最低分:{min(math)}, 平均分:{(sum(math)/len(math)):.2f}")
print(f"英语最高分:{max(english), }, 最低分:{min(english)}, 平均分:{(sum(english)/len(english)):.2f}")

print("---------------------------------")

# 3、查找成绩优秀(平均分大于90)的学生，并输出。
for s in scores:
    total = s[2] + s[3] + s[4]
    avg = total / 3
    if avg > 90:
        print(f"优秀学生：{s[0]} \t {s[1]} \t {total} \t {avg:.2f}")
