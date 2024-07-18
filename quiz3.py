class 부동산 :
    def __init__(self,위치,평수,종류,가격,년도):
        self.위치 = 위치
        self.평수 = 평수
        self.종류 = 종류
        self.가격 = 가격
        self.년도 = 년도
    def 정보 (self) :
        print('위치:',self.위치,
              '\n평수:',self.평수,
              '\n건물의 종류:',self.종류,
              '\n가격:',self.가격,
              '\n년식:',self.년도)

aa = 부동산('방배동','28평','이편한세상','15억','2020년')
aa.정보()