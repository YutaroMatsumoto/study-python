# 講義タイトル：集合のメソッド
s = {1, 2, 3, 4, 5}
print(s)

# 集合型にインデックスはないため、以下はエラーになる
# s[0]

s.add(6)
print(s) #{1, 2, 3, 4, 5, 6}
s.add(6)
print(s) #{1, 2, 3, 4, 5, 6}

s.remove(6)
print(s) # {1, 2, 3, 4, 5}

s.clear()
print(s) # set()

print('########################')
a = {}
print(type(a))
