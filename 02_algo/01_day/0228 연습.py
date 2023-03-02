# # 진수 변경의 연습
# # n진수 값을 10진수로 변경하기
# string_a = input()
# int(string_a, 6)  # int(string_a,n) #n은 원하는 진수를 말함
#
#
# # 10진수 값을 받아서, n진수로 변환하기
# def convert(num, n):
#     result = ''
#     asset = '0123456789ABCDEF'  # 현재는 16진수까지만 표현함
#     # num의 값이 0이 될 때까지 반복하며 해당 진수로 나눠야 함
#     while num > 0:
#         num, tmp = divmod(num, n)  # 몫과 나머지가 나올텐데, 몫은 계속 나눠줄 num에, 나머지는 일시적으로 담고 있으면 되므로 tmp변수에 할당
#         result += asset[tmp]
#
#     # 역순으로 뒤집어주면 된다
#     result = result[::-1]
#
#     return result
#
#
# print(convert(149, 2))  # 10010101
# print(convert(149, 8))  # 225
# print(convert(149, 16))  # 95
# print(convert(225687, 3))
#
# #소수점은, n진수에서 n^-k로 정의된다
# # 연습문제1
# """
# 0000000111100000011000000111100110000110000111100111100111111001100111
# """
#
# s = '0000000111100000011000000111100110000110000111100111100111111001100111'  # input()
#
# # 1. 슬라이싱 방법...
# for i in range(0, len(s), 7):
#     a = s[i:i + 7]
#     num = int(a, 2)
#     print(num, end=' ')
#
# print()
# # 2. 이중포문을 사용하는 방법
# for i in range(0, len(s), 7):
#     hap = 0
#     for j in range(6, -1, -1):
#         hap += (1 if s[i+j] == '1' else 0) * (2 ** (6 - j))
#     print(hap, end=' ')
#
# # 연습문제2
# s = '0F97A3'  # input()
#
# binary_table = {
#     '0': '0000',
#     '1': '0001',
#     '2': '0010',
#     '3': '0011',
#     '4': '0100',
#     '5': '0101',
#     '6': '0110',
#     '7': '0111',
#     '8': '1000',
#     '9': '1001',
#     'A': '1010',
#     'B': '1011',
#     'C': '1100',
#     'D': '1101',
#     'E': '1110',
#     'F': '1111',
# }
# # 누적할 문자열 변수
# binary = ''
# # 각 s의 문자를 순회하면서 4자리의 이진수로 바꿔준다!
# for ch in s:
#     binary += binary_table[ch]
#
# # 7bit 씩 잘라서 정수로 출력
# for i in range(0, len(binary), 7):
#     string = binary[i:i + 7]
#     # print(string)
#     print(int(string, 2), end=' ')
#
# # 연습문제3
# s = '0269FAC9A0'  # input()
#
# binary_table = {
#     '0': '0000',
#     '1': '0001',
#     '2': '0010',
#     '3': '0011',
#     '4': '0100',
#     '5': '0101',
#     '6': '0110',
#     '7': '0111',
#     '8': '1000',
#     '9': '1001',
#     'A': '1010',
#     'B': '1011',
#     'C': '1100',
#     'D': '1101',
#     'E': '1110',
#     'F': '1111',
# }
# # 누적할 문자열 변수
# binary_string = ''
# # 각 s의 문자를 순회하면서 4자리의 이진수로 바꿔준다!
# for ch in s:
#     binary_string += binary_table[ch]
#
# # print(binary_string)
#
# # 암호비트패턴 테이블
# pattern_table = {
#     '001101': 0,
#     '010011': 1,
#     '111011': 2,
#     '110001': 3,
#     '100011': 4,
#     '110111': 5,
#     '001011': 6,
#     '111101': 7,
#     '011001': 8,
#     '101111': 9,
# }
#
# # 문자열 s에 대해... 암호 패턴이 시작하는 첫 위치를 탐색
# idx = 0
# for i in range(len(binary_string)):
#     # 문자열을 6개씩 슬라이싱... -> 암호패턴! idx = i하고, break!
#     if binary_string[i:i + 6] in pattern_table:
#         idx = i
#         break
#
# # 암호 패턴을 그대로 6자리씩 끊어서 변환 -> 출력
# for i in range(idx, len(binary_string), 6):
#     string = binary_string[i:i + 6]
#     if len(string) != 6:
#         break
#     print(pattern_table[string], end=' ')

