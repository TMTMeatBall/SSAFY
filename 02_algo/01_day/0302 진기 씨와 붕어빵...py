# N명의 사람
# 0,M 초를 들여서 K개를 생산
# 기다리는 시간 없이 붕어빵을 고객들에게 제공할 수 있는가의 '여부' 를 따지는 코드
T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    # 1번 케이스에서 2명이 3초, 4초에 오고, 2초의 시간을 들여서 2개 생산하므로, 2초에 2개, 4초에 4개이므로 2인에게 제공 가능
    # 2번 케이스는 2명이 1초 2초에 오기 때문에 1초 시점에 0개 생산이므로 불가능
    time = [0] * 11111
    result = 'Possible'
    for i in range(0, len(time), M):  # time배열에 m초마다 k개씩 생산하고 있음을 작성
        time[i] = K

    for i in range(len(a)):  # (0)3 (1)4
        b = 0
        for j in range(0, a[i] + 1):

            b += time[j]

            if time[j] != 0:  # 여기서 문제 있음 for 문 두개 돌려보기
                time[a[i]] = time[a[i]] - 1
                b -= 1
            elif b == 0:
                result = 'Impossible'  # 아마도 중간중간 0이 섞여있는데 그걸 받아서 imp를 뱉어낸다 고쳐야함
    print(f'#{tc} {result}')

    # for i in range()
    #     a[i] 시점에서 time[:a[i]+1] 에 생산된 붕어빵의 값이 존재하는가?
    #     결국 기다리는 사람이 없어야 하기 때문에, 그 순간에 또는 그 time[i]의 이전에 값이 존재한다면.
    #     poss를 출력
#
