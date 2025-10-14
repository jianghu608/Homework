# 方法1 for循环
result = 0
for i in range(1,1001):
    if i % 10 == 0:
        continue
    result += i
print(result)

# 方法2 while循环
result = 0
i = 0
while i < 1001:
    if i % 10 == 0:
        i += 1              # i+1 否则一直循环
        continue
    result += i
    i += 1
print(result)
