# T = int(input())
# for tc in range(1,T+1):
#     arr = [list(input().strip()) for _ in range(5)]
#     longest = 0
#     for i in range(5):
#         if longest < len(arr[i]):
#             longest = len(arr[i])
#     #기존 리스트를 새로 쓰기?
#
#     for i in range(longest):
#         for j in range(5):
#             if i < arr
#
# T = int(input())
# for tc in range(1, T + 1):
#     word = []
#
#     for i in range(5): #5개가 제시되는 단어
#         word.append(input())
#
#     mx = 0
#     for i in word:
#         if mx < len(i):
#             mx = len(i) #각 word 케이스마다 리스트 안에서 가장 긴 열 파악
#
#     serototal = ''#정답을 넣어줄 빈 문자열
#
#     for i in range(mx): #열
#         for j in range(5): #행
#             if i < len(word[j]):
#                 serototal += word[j][i] #행 별로 가장 긴 mx만큼 열에서 나온 것들을 싹 더해준다
#
#     print(f'#{tc} {serototal}')

# 2. 위의 방식에서 마지막 배열을 이해 못할 때.

T = int(input())
for tc in range(1, T + 1):
    lst = [list(input()) for _ in range(5)]
    checker = [[0] * 15 for _ in range(15)]

    for i in range(5):
        for j in range(len(lst[i])):
            checker[i][j] = lst[i][j]

    answer = ''
    for i in range(15):
        for j in range(15):
            tmp = checker[j][i]
            if tmp != 0:
                answer += tmp

    print(f'#{tc} {answer}')
    #
    # for i in range(15):
    #     for j in range(15):
    #         if checker[i][j] != 0:
    #             answer += checker[j][i]
    # 다음 코드가 문제인 이유에 대해서 : 이렇게 하면 결과창에 행 별 각 열의 길이가 다른 경우에 에러 발생으로 오류를 반환함
    #checker[i][j] != 0: 인 경우에 for i for j 가 도는 순회형태와/checker[j][i] != 0:인 경우에 for i for j의 순회 결과가
    #결과적으로 다름에도 불구하고, 단순히 좌표만 생각해서 추가하면 오류가 날 수 밖에 없다.
    #비교대상과 추가할 대상이 같아야 그 순회하는 차례대로 맞게 들어간다.