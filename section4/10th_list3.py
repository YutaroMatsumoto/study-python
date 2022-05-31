# 講義タイトル：リストのメソッド
r = [1, 2, 3, 4, 5, 1, 2, 3,]
print(r.index(3))
print(r.index(3, 3))

print(r.count(3))

r.sort()
print(r)
r.sort(reverse=True)
print(r)
r.reverse()
print(r)
r.reverse()
print(r)


print('########################')

s = 'My name is Mike.'
print(s)
to_split = s.split(' ')
print(to_split)

x = ' ######## '.join(to_split)
print(x)

# print(help(list))