# 講義タイトル：辞書の使い所

# リストで書くと、appleを検索するコードを自分で書く必要がある。
l = [
  ['apple', 100],
  ['banana', 200]
  ['orange', 300]
]

# リストは、ハッシュテーブルを用いているため、検索が早い
fruits = {
  'apple': 100,
  'banana': 200,
  'orange': 300,
}

print(fruits['apple'])