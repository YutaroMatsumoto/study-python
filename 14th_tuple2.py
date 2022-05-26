# 講義タイトル：タプルのアンパッキング
from re import I


num_tuple = (10, 20)
print(num_tuple)

x, y = num_tuple
print(x, y)

x, y = (10, 20)
print(x, y)

# 以下の書き方は、右辺がtuple型になっていてそれを展開している
x, y = 10, 20
print(x, y)

print('########################')

min, max = 0, 100
print(min, max)

# 以下のような書き方は見にくい！
a, b, c, d, e, f = 'Mike', '1', '1', '1', 'e', 'f'

print('########################')

# iとjの入れ替え
i = 10
j = 20

tmp = i
i = j
j = tmp
print(i, j)

# アンパッキングを使うと簡単にできる！
a = 100
b = 200
print(a, b)

a, b = b, a
print(a, b)