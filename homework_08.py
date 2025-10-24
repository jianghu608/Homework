# 输出小于或等于n的所有素数及总数
n = int(input('请输入一个正整数n：'))
total = 0
prime_num = []

print('n = ' + str(n))
print('小于或等于n的所有素数有：')

# 先排除1和2
if n == 1:
    total = 0
elif n == 2:
    total = 1
    prime_num.append(2)

else:                               # n大于2时，已经有一个小于n的质数2，总数加一，并添加2
    total += 1
    prime_num.append(2)

    for i in range(3, n+1, 2):      # 遍历小于n的数i（除了1，2，偶数）

        # 下面判断i是否为素数
        for j in range(3, i, 2):    # 判断i是否有除了1和自身的因子,即i是否能被j整除,偶数已经排除
            if i % j == 0:          # 若有，说明i不是质数，跳出潜在因子j的遍历
                break
        else:                       # 若没有，说明i是质数，总数加一，并添加i
            total += 1
            prime_num.append(i)


output =  ', '.join(map(str, prime_num))
print(output)
print(f'素数总数为：{total}\n')