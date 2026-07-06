# 案例1 —— 邮箱格式验证
# 用户输入一个邮箱，验证邮箱格式是否正确(包含一个@和至少一个.)，如果输入正确，输出"邮箱格式正确"，否则输出"邮箱格式错误"。

email = input("请输入您的邮箱地址：")
if email.count("@") == 1 and email.count(".") >= 1:
    print("邮箱格式正确")
else:
    print("邮箱格式错误")

# 方式2，使用 in 运算符，判断是否包含指定的字符串
if email.count("@") == 1 and "." in email:
    print("-- 邮箱格式正确")
else:
    print("-- 邮箱格式错误")