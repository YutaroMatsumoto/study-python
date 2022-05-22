s = 'test'
print(s)

print("I don't know")
print('I don\'t know')
print('say "I don\'t know"')
print("say \"I don't know\"")

print('hello. \nHow are you?')

# バックスラッシュで開業したくない場合は文字列のてまえでrをつける
print(r'C:\name\name')

# ダブルクウォート3つ
print("""line1
line2
line3""")

# バックスラッシュを書くことで、「次のコードは次の行から」となる
print("""\
line1
line2
line3\
""")

print('Hi.' * 3) # Hi.Hi.Hi.
print('Hi.' * 3 + 'Mike') # Hi.Hi.Hi.Mike

print('Py' + 'thon') # Python
print('Py''thon') # Python

prefix = 'Py'
print(prefix + 'thon') # 変数は + で連結

# 長い文章をつなげるときに便利
s = ('aaaaaaaaaaaaaaaaaaaaaaaaa'
    'bbbbbbbbbbbbbbbbbbbbbbbbb')
s2 = 'aaaaaaaaaaaaaaaaaaaaaaaaa'\
    'bbbbbbbbbbbbbbbbbbbbbbbbb'
print(s)
print(s2)