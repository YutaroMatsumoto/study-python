# 講義タイトル：文字の代入

# formatで指定した値が中括弧の中に代入される
print('a is {}'.format('a'))

print('a is {} {} {}'.format(1, 2, 3)) # 数字なども型変換される

print('a is {0} {1} {2}'.format(1, 2, 3))

print('My name is {0} {1}. Watashi ha {1} {0}'.format('Yutaro', 'Matsumoto'))

print('My name is {name} {family}. Watashi ha {family} {name}'.format(name='Yutaro', family='Matsumoto'))

str(1) # 文字列型の1になる
str(3.14) # 文字列型の1になる
str(True) # 文字列型の1になる

# f-strings（python3.6より利用可能。処理早い。）
a = 'a'
print(f'a is {a}')

x, y, z = 1, 2, 3
print(f'a is {x}, {y}, {z}')
print(f'a is {z}, {y}, {x}')

name = 'Jun'
family = 'Matsumoto'
print(f'My name is {name} {family}. Watashi ha {family} {name}')