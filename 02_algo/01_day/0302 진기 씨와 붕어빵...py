# N명의 사람
# 0,M 초를 들여서 K개를 생산
# 기다리는 시간 없이 붕어빵을 고객들에게 제공할 수 있는가의 '여부' 를 따지는 코드
T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    time = list(map(int, input().split()))
    time.sort()  # 손님 도착시간

    cnt = 0  # 붕어빵

    idx = 0  # 손님

    result = 0 #결과 반환

    for i in range(time[-1] + 1): #가장 마지막 손님까지의 범위 설정
        if i != 0:
            if i % M == 0: #나머지가 없다 = 붕어빵이 생산되는 그 시간을 말함
                cnt += K #생산량만큼 cnt에 추가
        if i == time[idx]: #i가 손님 도착 시간과 같아진 순간에
            if cnt == 0: #cnt==0이면 배급 불가하므로 imp를 반환
                result = 'Impossible'
                break #이후 과정 필요없으므로 break
            else: #cnt !=0이라면
                cnt -= 1 #idx는 1개 나아가서 다음 번 손님 시간으로 진행, cnt는 생산된 것에서 1개 제거
                idx += 1
        if i == time[-1]: #i가 모든 손님을 다 받았다면, 완료했으므로 result에 poss를 반환
            result = 'Possible'
    print(f'#{tc} {result}') #출력

for t in range(int(input())):
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort()
    tree = [0] * 11112

    for i in range(M, 11112):
        tree[i] = i // M * K

    j = 1
    res = 0
    for i in lst:
        if tree[i] - j >= 0:
            res += 1

        j += 1

    if res == N:
        print(f'#{t + 1} Possible')
    else:
        print(f'#{t + 1} Impossible')
    # 1번 케이스에서 2명이 3초, 4초에 오고, 2초의 시간을 들여서 2개 생산하므로, 2초에 2개, 4초에 4개이므로 2인에게 제공 가능
    # # 2번 케이스는 2명이 1초 2초에 오기 때문에 1초 시점에 0개 생산이므로 불가능
    # time = [0] * 11111
    # result = 'Possible'
    #
    # for i in range(0, len(time), M):  # time배열에 M초마다 K개씩 생산하고 있음을 작성
    #     time[i] = K #M초마다의
    #
    # for i in range(len(a)):  # (0)3 (1)4
    #     b = 0
    #
    #     for j in range(0, a[i] + 1):
    #
    #         b += time[j]
    #
    #         if b != 0:  # 여기서 문제 있음 for 문 두개 돌려보기
    #
    #             b -= 1
    #
    #         elif b == 0:
    #             result = 'Impossible'  # 아마도 중간중간 0이 섞여있는데 그걸 받아서 imp를 뱉어낸다 고쳐야함

    # for i in range()
    #     a[i] 시점에서 time[:a[i]+1] 에 생산된 붕어빵의 값이 존재하는가?
    #     결국 기다리는 사람이 없어야 하기 때문에, 그 순간에 또는 그 time[i]의 이전에 값이 존재한다면.
    #     poss를 출력
#
