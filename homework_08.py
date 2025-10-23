# 输出小于或等于n的所有素数及总数
n = int(input('请输入一个正整数n：'))
total = 0

print('n = ' + str(n))
print('小于或等于n的所有素数有：')

# 先排除1和2
if n == 1:
    total = 0
    print('无')
elif n == 2:
    total = 1
    print('2', end = '')

else:                               # n大于2时，已经有一个小于n的质数2，总数加一，并打印2
    print(2, end = ' ')
    total += 1
    for i in range(3, n+1, 2):      # 遍历小于n的数i（除了1，2，偶数）
        # 下面判断i是否为素数
        for j in range(3, i, 2):    # 判断i是否有除了1和自身的因子,即i是否能被j整除,偶数已经排除
            if i % j == 0:          # 若有，说明i不是质数，跳出潜在因子j的遍历
                break
        else:                       # 若没有，说明i是质数，总数加一，并输出i
            total += 1
            print(i, end = ' ')     # 用空格作为分隔符
            if total % 10 == 0:     # 每10个质数换行
                print()

if total % 10 == 0 or n == 1:       # 因为总数为10的倍数时(包括0)已经换行，要另外考虑统一格式
    print(f'素数总数为：{total}\n')
else:
    print()
    print(f'素数总数为：{total}\n')