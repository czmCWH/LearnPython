# 1、三角形类型判断
# 根据输入的三个边长（正整数），判断三角形的类型：等边三角形、等腰三角形、一般三角形、不能构成三角形
# 分析：
#   - 三角形的三条边长必须大于零，且任意两边长之和大于第三边长
#   - 等边三角形：a==b==c
#   - 等腰三角形：a==b or b==c or a==c
#   - 一般三角形：a+b>c and a+c>b and b+c>a

a = int(input("请输入第一个边长："))
b = int(input("请输入第二个边长："))
c = int(input("请输入第三个边长："))


if a + b > c and a + c > b and b + c > a:
  if a == b and b == c:
    print("等边三角形")
  elif a == b or b == c or a == c:
    print("等腰三角形")
  else:
    print("一般三角形")
else:
    print(f"{a} {b} {c} 不能构成三角形")

print("-------------------------------")
