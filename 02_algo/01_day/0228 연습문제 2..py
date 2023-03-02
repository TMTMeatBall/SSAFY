# 16진수 문자로 이뤄진 1차 배열이 주어질 때에, 앞에서부터 7bit씩 묶어 십진수로 변환하여 출력해 보기
num = input()
# 입력받은 것을 이진수로 바꾸고, 7개씩 묶어서, 10진수로 변환한다

asset = '0123456789ABCDEF'  # input()
binary_table = {'0': '0000',
                '1': '0001',
                '2': '0010',
                '3': '0011',
                '4': '0100',
                '5': '0101',
                '6': '0110',
                '7': '0111',
                '8': '1000',
                '9': '1001',
                'A': '1010',
                'B': '1011',
                'C': '1100',
                'D': '1101',
                'E': '1110',
                'F': '1111',
                }
binary = ''
for ch in num:
    binary += binary_table[ch]

for i in range(0, len(binary), 7):
    string = binary[i:i + 7]
    print(string)
    print(int(string, 2), end=' ')
