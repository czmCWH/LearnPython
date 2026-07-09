from circle_fun import circle_area, circle_len
def main():
    radius = float(input("请输入圆的半径："))
    print("圆的面积为：", circle_area(radius))
    print("圆的周长为：", circle_len(radius))


if __name__ == "__main__":
    main()