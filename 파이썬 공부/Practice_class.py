# Calculator 클래스 생성
class Calculator:
    def __init__(self):           # __init__(self): >> 객체를 초기화 하는 생성자 역할을 함. 초기 설정 함수 같은거.
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))