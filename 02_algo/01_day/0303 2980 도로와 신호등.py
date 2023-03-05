# N, L = map(int, input().split())
# cur_idx = 0
# time = 0
#
# empty = []
# for _ in range(N):
#     empty.append(list(map(int, input().split())))
#     i = 0
# while cur_idx < L - 1:
#
#     time += 1
#     cur_idx += 1
#     if cur_idx == empty[i][0]:  # D
#         if time % (empty[i][1] + empty[i][2]) < empty[i][1]:  # R,G,R
#             time += time % (empty[i][1] + empty[i][2])  # R,G
#             i = i + 1
# print(time)
# 0에서 L 까지 초당 1씩 간다.
# #해당 지점에 도착했을 때에(D) 빨간 불이면 R이 끝날 때까지 멈춘다
# time이 증가할 때에, 매 상태를 반환한다? 차는 D초에 D 지점에 있다. 즉, D가 수집되는 시점에서 R인지 G인지 판정해서,
# 만약 R이라면 G까지 남은 시간을 재서 그 만큼만 총 시간인 L에 가산한다


# 가고 있음을 어떻게 표현하지
N, L = map(int, input().split())
road = [0] * (L + 1)
for _ in range(N):
    D, R, G = map(int, input().split())
    road[D] = [R, G]
time = 0  # 시간
pos = 0  # 위치

while pos < L - 1:
    if road[pos] != 0:
        time += 1
        pos += 1
    else:  # 시신호등 발견시
        R, G = road[pos]
        if (time % (R + G)) < R:
            time += 1
        else:
            time += 1
            pos += 1

print(time)
