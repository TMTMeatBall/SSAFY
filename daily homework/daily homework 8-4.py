# 스택(Stack)은 LIFO(Last in First Out)으로 구조화된 자료구조를 의미한다. 아래 구성요소를 포함하는 Stack class를 생성하라
# 구성 요소(메서드)      
# i.        __init__(): 인스턴스가 생성될 때 빈 리스트를 각 인스턴스의 이름 공간에 넣는다.      
# ii.        empty(): 스택이 비었다면 True을 반환하고, 그렇지 않다면 False를 반환한다.      
# iii.        top(): 스택의 가장 마지막 데이터를 반환한다. 스택이 비었다면 None을 반환한다.      
# iv.        pop(): 스택의 가장 마지막 데이터의 값을 반환하고, 해당 데이터를 삭제한다. 스택이 비었다면 None을 반환한다.       
# v.        push(): 스택의 가장 마지막 데이터 뒤에 값을 추가한다. 반환값은 없다.      
# vi.        __repr__: 현재 스택의 요소들을 보여준다.

class Stack():
    def __init__(self):
        self.list=[]

    def empty(self):
        if not self.list: #Falsy 조건
        # if len(self.list) == 0: 
        # if self.list==[]:
            return True
        else:
            return False
    def top(self):
        if len(self.list) == 0 :
            return None
        else:
            return self.list[-1]
    def pop(self):
        if self.list == []:
            return None
        else:
            a=self.list[-1]
            del self.list[-1]
            return a 
    def push(self,x):
        self.list.append(x)
    def __repr__(self):
        return str(self.list)


p1=Stack()
p1.empty()
p1.top()
p1.push(1)
p1.top()
p1.push(2)
p1.top()
print(p1.__repr__())

