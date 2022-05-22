# 講義タイトル：文字のメソッド

s = 'My name is Mike. Hi Mike.'
print(s)

# startswithは、指定した文字列で始まっているか
is_start = s.startswith('My')
print(is_start)

# 指定した文字列がどこにあるか
print(s.find('Mike')) # 11（先頭から検索）
print(s.rfind('Mike')) # 20（後ろから検索）

# 指定した文字列がいくつあるのか
print(s.count('Mike'))

# 先頭を大文字にして、それ以外は小文字にする
print(s.capitalize())

# すべての単語の先頭文字を大文字に
print(s.title())

# すべてを大文字に
print(s.upper())

# すべてを小文字に
print(s.lower())

# 文字列の置き換え
print(s.replace('Mike', 'Nancy'))

