n = int(input("请设置一个数字："))
a = 0
i = "恭喜你猜对了！"
b = "很遗憾，你猜的太大了"
c = "很遗憾，你猜的太小了"
while a != n:
    a = int(input("请猜猜这个数："))
    if a < n:
        print(c)
    elif a > n:
        print(b)
print(i)
