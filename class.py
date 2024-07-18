num = [1,2,3,4,5,6,7]
num.append(8)
# . 은 앞에 있는 클래스에 대한 사용 가능한 함수를 뒤에 실행하는 것
# 붕어방 틀 에서 팥붕 슈붕 피붕 나오는거임

class Dog :
    def __init__(self , name , breed):
        self.dog_name = name
        self.dog_breed = breed
        self.dog_sex = '남'
    def bark(self):
        print(self.dog_name+'왈')



my_dog=Dog('뽀삐','말티즈')
print(my_dog)