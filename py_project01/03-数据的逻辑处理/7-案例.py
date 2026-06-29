# 案例1
# 根据用户输入的用户名和密码，判断是否登录成功，如果登录成功，则显示欢迎信息，否则提示用户继续输入
while True:
    username = input("请输入用户名：")
    password = input("请输入密码：")
    if username == "" or password == "":
        print("用户名或密码不能为空")
        continue
    elif username == "admin" and password == "666888":
        print("登录成功")
        break
    else:
        print("用户名或密码错误，请重新输入")
else:
    print("循环正常结束")

# ⚠️，循环关键字
# break 和 continue 都是循环控制语句，用于控制循环的执行流程，只能出现在循环体中。
# break 用于跳出（结束）当前循环，即终止循环体的执行。当执行 break 时，循环的 else 子句不会被执行。
# continue 用于跳过当前循环的剩余部分，直接进入下一次循环。


# 案例2
# 猜数字游戏：
# 程序随机生成一个1~100之间的整数，玩家有5次机会，每次猜测后，程序会提示玩家猜大了、猜小了或猜对了，直到玩家猜对或用完5次机会为止
import random
secret = random.randint(1, 100)   # ⚠️，randint() 函数用于生成指定范围内的随机整数
for i in range(1, 6):
    guess = int(input("请输入您猜测的数字："))
    if guess > secret:
        print("猜大了")
    elif guess < secret:
        print("猜小了")
    else:
        print("恭喜你猜对了")
        break   # ⚠️，break 跳出循环
else:
    print("很遗憾，5次都没猜对")