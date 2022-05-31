# 講義タイトル：文字列のインデックスとスライス

word = 'python'
print(word[0]) # p
print(word[1]) # y
print(word[-1]) # n（最後の文字列が表示）

print(word[0:2]) # py
print(word[2:5]) # tho
print(word[:2]) # py
print(word[2:]) # # thon

# 文字列のインデックスに代入することはできない
# word[0] = 'j'
# print(word)

word = 'j' + word[1:]
print(word) # jython
print(word[:]) # jython

# 文字列の長さ
n = len(word)
print(n) # 6