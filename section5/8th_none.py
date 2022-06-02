# 講義タイトル：Noneを判定する場合

# 変数は定義したいけど何も入れたくない場合に使う？
is_empty = None
print(None)
# print(help(None))

if is_empty is None:
    print('None!!')


# print(1 == True)
print(1 is True) # オブジェクト同士が同じものじゃないとTrueにならない
# print(None is None)

