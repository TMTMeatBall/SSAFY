# N장의 인풋과 M의 수치
# a.append 해 가면서 M을 넘지 않으면서 최대한 가까운 카드 3장합
N, M = map(int, input().split())
cards = list(map(int, input().split()))
# 3장끼리의 합을 구하되, 최댓값을 구하면서, M보다 작거나, 같아야만 한다
cards.sort()
sum = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            tmp = cards[i] + cards[j] + cards[k]
            if sum < tmp and tmp <= M:
                sum = tmp

print(sum)
