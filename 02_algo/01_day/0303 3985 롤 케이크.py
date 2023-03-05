L = int(input())
N = int(input())

arr = [0] * (L + 1)
pred_i = 0
pred_cnt = 0

for i in range(1, N + 1):
    P, K = map(int, input().split())

    for j in range(P, K + 1):
        if arr[j] != 0:
            arr[j] = i
    if pred_cnt < K - P:
        pred_cnt = K - P
        pred_i = i

mx_cnt = 0
mx_i = 0
for i in range(1, N + 1):
    cnt = arr.count(i)
    if mx_cnt < cnt:
        mx_cnt = cnt
        mx_i = i


