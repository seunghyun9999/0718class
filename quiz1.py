class 연산 :
    def 덧셈(self,num1,num2):
        result = num1+num2
        return result
    def 뺄셈(self,num1,num2):
        result = num1 - num2
        return result
    def 나눗셈(self,num1,num2):
        result = num1 / num2
        return result

app = 연산()
print(app.뺄셈(1,2))
