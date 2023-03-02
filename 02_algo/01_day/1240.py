pattern = {'0001101': 0,
           '0011001': 1,
           '0010011': 2,
           '0111101': 3,
           '0100011': 4,
           '0110001': 5,
           '0101111': 6,
           '0111011': 7,
           '0110111': 8,
           '0001011': 9}

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    code = ''
    for i in range(N):
        for j in range(M - 1, 54, -1):  # 가장 왼쪽으로 치우친 패턴은 0-55
            if arr[i][j] == '1':  # 암호패턴의 끝 발견
                code = arr[i][j - 55:j + 1]
                break  # for j
        if code != '':
            break  # for i

    passwd = [0] * 8  # 8자리 암호
    for i in range(8):
        passwd[i] = pattern[code[i * 7:i * 7 + 7]]

    check = (passwd[0] + passwd[2] + passwd[4] + passwd[6]) * 3 + passwd[1] + passwd[3] + passwd[5] + passwd[7]
    cs = sum(passwd[0:8:2]) * 3 + sum(passwd[1:8:2])
    ans = 0
    if cs % 10 == 0:  # cs가 10의 배수면 ...
        ans = sum(passwd)
    print(f'#{tc} {ans}')