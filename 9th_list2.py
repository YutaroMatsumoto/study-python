# 講義タイトル：リストの操作
s = list('abcdefg')
print(s)
print(s[0])

s[0] = 'X'
print(s)
print(s[2:5])

s[2:5] = ['C', 'D', 'E']
print(s)

s[2:5] = []
print(s)

s[:] = []
print(s)

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n.append(100) # 配列の末尾に追加
print(n) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100]

n.insert(0, 200) #配列の指定箇所に追加
print(n) # [200, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100]

n.pop()
print(n) # [200, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

n.pop(0)
print(n) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

del n[0] # 強力
print(n) # [2, 3, 4, 5, 6, 7, 8, 9, 10]

print('########################')

n = [1, 2, 2, 2, 3]
n.remove(2) # 該当のインデックスの値を削除
print(n)
n.remove(2)
print(n)
n.remove(2)
print(n)


print('########################')
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
x = a + b
print(x)
a+=b
print(a)

x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]
x.extend(x)
print(x)
