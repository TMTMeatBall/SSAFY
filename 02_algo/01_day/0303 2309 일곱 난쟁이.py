# # 여러 줄에 걸친 input()
# dwarves = []
# for i in range(9):
#     dwarves.append(int(input()))
# # 둘을 빼고 더한 값이 100이면 빼고 나머지를 전부 출력
# # 9명이 정해져 있으므로 언제나 둘만 빼면 된다.
# dwarves.sort()
# a = []
# for i in range(9):
#     for j in range(i + 1, 9):
#         if dwarves[i] + dwarves[j] + 100 == sum(dwarves):
#             a.append(dwarves[i])
#             a.append(dwarves[j])
# dwarves.remove(a[0])
# dwarves.remove(a[1])
# print(*dwarves, sep='\n')
# 또는 12번 line 에서 dwarves.pop[j] 를 먼저 하는 것으로 서로 크기 차이가 있는 i,j가 인덱스 에러가 나지 않게 할 수 있다.
# 이 경우 13번에서는 dwarves.pop[i]
#
# 2.7번의 for문을 돌리는 노빠꾸 방식

dwarves = []
for i in range(9):
    dwarves.append(int(input()))
dwarves.sort()
def solve():
    for i in range(9):
        for j in range(i + 1, 9):
            for k in range(j + 1, 9):
                for l in range(k + 1, 9):
                    for m in range(l + 1, 9):
                        for n in range(m + 1, 9):
                            for o in range(n + 1, 9):
                                if dwarves[i] + dwarves[j] + dwarves[k] + dwarves[l] + dwarves[m] + dwarves[n] + dwarves[
                                    o] == 100:
                                    return (dwarves[i], dwarves[j], dwarves[k], dwarves[l], dwarves[m], dwarves[n],
                                          dwarves[o])

result = solve()
for a in result:
    print(a)