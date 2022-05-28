# 講義タイトル：辞書型のメソッド
d = {'x': 10, 'y': 20}
print(d)
# help(d)

print(d.keys())
print(d.values())

print('########################')

d2 = {'x': 1000, 'j': 500}
print(d2)

d.update(d2)
print(d)

print(d['x'])
print(d.get('x'))

# print(d['z']) #エラーになる
# print(d.get('z')) #空が返ってくる

ab = d.pop('x')
print(ab)
print(d)

# del d['y']
d.clear()
print(d)

d2 = {'a': 100, 'b': 200}
print('a' in d2)
print('j' in d2)
