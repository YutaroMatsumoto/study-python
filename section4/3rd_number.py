print(2 + 2)

# 以下は1.6になり、float型になる
num1 = 8 / 5
print(num1)
print(type(num1))

# 0は省略可能
0.6
.6

print(17 / 3) # 5.666666666666667
print(17 // 3) # 5
print(17 % 3) # 2

print(5 * 5) # 25
print(5 ** 2) # 25

print(5 * 5 * 5 * 5 * 5) # 3125
print(5 ** 5) # 3125

# round関数
pie = 3.141515151515
print(pie)
round(pie, 2) # 3.14

# 数学関数 ← 便利！
import math
result = math.sqrt(25)
print(result) # 5.0

y = math.log2(10)
print(y)

print(help(math))