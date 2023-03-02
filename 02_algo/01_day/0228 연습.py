# 진수 변경의 연습
# n진수 값을 10진수로 변경하기
string_a = input()
int(string_a, 6)  # int(string_a,n) #n은 원하는 진수를 말함


# 10진수 값을 받아서, n진수로 변환하기
def convert(num, n):
    result = ''
    asset = '0123456789ABCDEF'  # 현재는 16진수까지만 표현함
    # num의 값이 0이 될 때까지 반복하며 해당 진수로 나눠야 함
    while num > 0:
        num, tmp = divmod(num, n)  # 몫과 나머지가 나올텐데, 몫은 계속 나눠줄 num에, 나머지는 일시적으로 담고 있으면 되므로 tmp변수에 할당
        result += asset[tmp]

    # 역순으로 뒤집어주면 된다
    result = result[::-1]

    return result


print(convert(149, 2))  # 10010101
print(convert(149, 8))  # 225
print(convert(149, 16))  # 95
print(convert(225687, 3))

#소수점은, n진수에서 n^-k로 정의된다
