# 講義タイトル：InとNotの使い所
y = [1, 2, 3]
x = 1

if x in y:
  print('in')

if 100 not in y:
  print('not in')

a = 1
b = 2

if not a == b:
  print('Not equal')

# notを使うのは推奨されていない（以下のように書ける）
if a != b:
  print('Not equal')

is_ok = True

# 以下のようなときにnotを使う（boolean型の時？）
if not is_ok:
  print('hello')