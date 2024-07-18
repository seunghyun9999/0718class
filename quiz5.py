class 문자 :
    def __init__(self,len2,p,p2):
        self.len2=len2
        self.p=p
        self.p2=p2
    def pay (self,x):
        if len(x)<=self.len2:
            print(self.p)
        elif len(x)>self.len2:
            print(self.p2)
bb=input('문자')
aa = 문자(10,500,1000)
aa.pay(bb)
