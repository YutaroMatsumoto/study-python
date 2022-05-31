# 講義タイトル：if文
x = 10

# ifの中身はインデントを開ける必要がある。
# 4つスペースを入れるのが好まれている
if x < 0:
    print('negative')
elif x == 0:
    print('zero')
else:
    print('positive')


a = 5
b = 10

if a > 0:
    print('a is positire')
    if b > 0:
        print('b is positive')