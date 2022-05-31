# 講義タイトル：1行が長くなるとき
s = 'aaaaaaaaaaa' + 'bbbbbbbbbbb'
print(s)
# 以下はエラーになる
# s = 'aaaaaaaaaaa' 
#   + 'bbbbbbbbbbb'

s = 'aaaaaaaaaaa' \
    + 'bbbbbbbbbbb'

print(s)

x = 1 + 1 + 1 + 1 + 1 + \
    1 + 1 + 1 + 1 + 1
print(x)
x = (1 + 1 + 1 + 1 + 1 + 
    1 + 1 + 1 + 1 + 1)
print(x)

# pythonのルールとして、80文字続いたら次の行に行くべきとなっている
123456789