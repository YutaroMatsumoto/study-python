# 講義タイトル：タプル型
t = (1, 2, 3, 4, 1, 2)
print(t)
print(type(t))

# t[0] = 100 はできない
# データ操作（値の変更）ができない

print(t[0])
print(t[-1])
print(t[2:5])
print(t.index(1))
print(t.index(1, 1))
print(t.count(1))

print('########################')

t = ([1, 2, 3], [4, 5, 6])
# t + (2, 4)
print('あいうえお')
print(t)

print(t[0][0])
t[0][0] = 100
print(t[0][0])

t = 1, 2, 3 # 間まで区切ればタプル型になる
print(t)
t = 1,
print(t)
# 誤ってカンマをつけることでバグの原因にもなる？

print('########################')
t = ()
print(t)
print(type(t)) # tuple

t = (1)
print(t)
print(type(t)) # integer

t = ('test')
print(t)
print(type(t)) # string

print('########################')
new_tuple = (1, 2, 3) + (4, 5, 6)
print(new_tuple)

# タプルはカンマをつける！
# new_tuple = (1) + (4, 5, 6) 
