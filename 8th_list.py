# 講義タイトル：リスト型

l = [1, 20, 4, 50, 2, 1, 2]
print(l)
print(l[0])
print(l[-1])
print(l[2:4])
print(l[:4])
print(l[1:])

print(len(l))

type(l) # list

print(list('abcdefg'))

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n[::2]) # [1, 3, 5, 7, 9]
print(n[::-1]) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

a = ['a', 'b', 'c']
n = [1, 2, 3]

x = [a, n]
print(x)
