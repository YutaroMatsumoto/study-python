# 講義タイトル：リストのコピー

# おそらく値渡し、参照渡しの概念はjavascriptと同じ

# 参照渡し
i = [1, 2, 3, 4, 5]
j = i
j[0] = 100
print('j = ', j)
print('i = ', i)

print('########################')

# 値渡し
x = [1, 2, 3, 4, 5]
y = x.copy() # y = x[:]も同じ
y[0] = 100
print('y = ', y)
print('x = ', x)

print('########################')

# 値渡し
X = 20
Y = X
Y = 5
print(id(X))
print(id(Y))
print(Y)
print(X)

print('########################')

X = ['a', 'b']
Y = X
Y[0] = 'p'
print(id(X))
print(id(Y))
print(Y)
print(X)