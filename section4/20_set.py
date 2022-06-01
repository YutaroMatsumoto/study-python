# 講義タイトル：集合型
a = {1, 2, 2, 3, 4, 4, 4, 5, 6}
print(a) # {1, 2, 3, 4, 5, 6}
print(type(a))

b = {2, 3, 3, 6, 7}
print(b) # {2, 3, 6, 7}

print(a - b) # {1, 4, 5}
print(b - a) # {7}

# aにもありbにもあるもの
print(a & b) # {2, 3, 6}

# aまたはbにあるもの
print(a | b) # {1, 2, 3, 4, 5, 6, 7}

# aまたはbかつ重複していないもの
print(a ^ b) # {1, 4, 5, 7}