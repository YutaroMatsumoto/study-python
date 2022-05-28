# 講義タイトル：辞書型
d = {'x': 10, 'y': 20}
print(d)
print(type(d))
print(d['x'])
print(d['y'])

d['x'] = 100
print(d)
d['x'] = 'XXXXX'
print(d)
d['z'] = 200
print(d)
d[1] = 100000
print(d)

print('########################')

c = dict(a=10, b=20)
print(c)

b = dict([('a', 10), ('b', 20)]) # {'a': 10, 'b': 20}
print(b)

tupleA = ('a', 10)
print(tupleA)
