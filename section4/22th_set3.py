# 講義タイトル：集合の使い所

# 自分とAさんの共通の知人を探す
my_frends = {'A', 'C', 'D'}
A_friends = {'B', 'D', 'E', 'F'}
print(my_frends & A_friends)

# 自分が購入した果物をリストに追加していく
f = ['apple', 'banana', 'apple', 'banana']
kind = set(f) # 型をリストから集合に変換
print(kind)