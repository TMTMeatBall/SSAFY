# 너비 * 높이 = 넓이
# 너비 i = 1 : 6 5 4 3 2 1
# 2 : 3 2 1
# 3 : 2 1
# 4 : 1
# 5 : 1
# 6 : 1
# N = int(input())
# cnt = 0
# #너비*높이 형태를 구한다
# for w in range(1, N + 1): # 1 2 3 4 5 6
#     mx_h = N // w  # 최대 높이값의 계산
#     cnt =+ mx_h
#
# for w in range(1,N+1):
#     if w*w <= N:
#         cnt += 1
#
# print(cnt//2)
#1xk로 만들어지는 경우는 n//1가지
#2xk로 만들어지는 경우는 n//2
#위의 것으로 볼 때 k변의 경우는 n//k개
n = int(input())
cnt = 0
for i in range(1,n+1):
    for j in range(i,n//i+1):
        cnt += 1

print(cnt)

for i in range(1,n+1):
    for j in range(i,n//i+1):
        cnt+=1