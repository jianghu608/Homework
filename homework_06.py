import math
x = float(input("请输入x的值："))

if x < 0:
    y = abs(x)
elif x < 5:
    y = math.exp(x) * math.cos(x * math.pi /180)
elif x < 10:
    y = x ** 3
else:
    y = (7 + 8 * x) * math.log(x)

if y % 1 == 0:
    print(int(y))       # 为了美观，转换为整型
else:
    print(round(y,2))
