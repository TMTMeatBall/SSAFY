# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
# python 내장함수 min, max 사용 금지

def min_max(scores):
    a=0
    b=0
    for b in scores:
        if b>=b:
            print(b)
        else:
            b=b
        for a in scores:
            if a<=a:
                print(a)
        else:
            a=a
    return tuple(a,b)
tuple(a,b) = min_max(scores)
min_max(scores)
#     return min_max
#     # pass
# min_max(scores)
#     # 여기에 코드를 작성하여 함수를 완성합니다.
# print(min(scores),max(scores))

# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    scores = [80, 90, 85, 75]
    print(min_max(scores))    # (75, 90)
