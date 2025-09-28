number_list = [34, 5, 89, 3, 32, 122]

print("整组数：", end='')
print(number_list)

total = 0
for i in number_list:
    total +=  i
print(total/len(number_list))