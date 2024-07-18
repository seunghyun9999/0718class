
class 개인정보 :
    def __init__(self,이름,나이, 연락처):
        self.a = 이름
        self.b = 나이
        self.c = 연락처
    def 출력 (self):
        print('이름:', self.a,
              '\n나이:',self.b,
              '\n연락처:',self.c)
name1 = input('이름:')
age1 = input('나이:')
phone1 = input('연락처:')
num1 = 개인정보 (name1,age1,phone1)
num1.출력()