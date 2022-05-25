# 講義タイトル：リストの使い所
seat = []
min = 0
max = 5
print(min <= len(seat) < max)

seat.append('a')
print(min <= len(seat) < max)
print(len(seat))

seat.append('b')
print(min <= len(seat) < max)
print(len(seat))

seat.append('c')
print(min <= len(seat) < max)
print(len(seat))

seat.append('d')
print(min <= len(seat) < max)
print(len(seat))

seat.append('e')
print(min <= len(seat) < max)
print(len(seat))
print(seat)

seat.pop(0)
print(min <= len(seat) < max)
print(len(seat))
# print(seat)
