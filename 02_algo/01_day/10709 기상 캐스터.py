H, W = map(int, input().split())
arr = [list(input()) for _ in range(H)]
result = [[0] * W for _ in range(H)]
tf = False
num = 1
for i in range(H):
    for j in range(W):
        if tf == False and arr[i][j] == '.':
            result[i][j] = -1
        elif arr[i][j] == 'c':
            tf = True
            num = 1
        else:
            result[i][j] = num
            num += 1
    tf = False
    num = 1
for i in range(H):
    for j in range(W):
        print(result[i][j], end=' ')
    print()


# res = []
# for _ in range(H):
#     s = input()
#     li = []
#     idx = -1
#     for i in range(W):
#         if s[i] == 'c':
#             li.append(0)
#             idx = i
#         elif idx == -1:
#             li.append(-1)
#         else:
#             li.append(i-idx)
#     res.append(li)
# for a in res:
#     print(*a)