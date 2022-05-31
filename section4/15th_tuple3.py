# 講義タイトル：タプルの使い所
chose_from_two = ('A', 'B', 'C')

answer = []
answer.append('A')
answer.append('C')
print(chose_from_two)
print(answer)

print('########################')

chose_from_two = ['A', 'B', 'C']
answer = []

# 誤ってchose_from_twoにappendしてしまっている
chose_from_two.append('A')
chose_from_two.append('C')

print(chose_from_two)
print(answer)

# 誤って書き換えないようにtupleを利用する！