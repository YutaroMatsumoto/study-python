num = 1
name = 'Mike'
is_ok = True

# type関数を使うことで型を確認できる
print(num, type(num))
print(name, type(name))
print(is_ok, type(is_ok))

num2 = 1
name2 = 'Mike'
num2 = name2
print(num2, type(num2))

name3 = '1'
new_num = int(name3)
print(new_num, type(new_num))

num4: int = 1
name4: str = '1'
num4 = name4 # string型として認識される

# 基本的には型宣言しないで使われる
# 変数の先頭文字に数字は使えない
# ifも変数名にはできない
