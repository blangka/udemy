# class  샘플
import mod1


class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

    def div(self, num):
        self.result /= num
        return self.result


cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

# 객체와 인스턴스의 차이
# cal1은 객체이고, Calculator의 인스턴스이다.

# 상속
class MoreCalculator(Calculator):
    def minus(self, num):
        self.result -= num
        return self.result

    def div(self, num):  # 오버라이딩
        if num == 0:
            return 0
        else:
            self.result /= num
            return self.result


moreCal = MoreCalculator()
print(moreCal.add(3))
print(moreCal.minus(2))
print(moreCal.div(0))


# 클래스 변수
class Family:
    lastname = "김"  # 클래스 변수


print(Family.lastname)

a = Family()
b = Family()

a.lastname = "박"

print(a.lastname)
print(b.lastname)

# 모듈 테스트
print(mod1.add(3, 4))
print(mod1.sub(4, 2))

from mod1 import add, sub

print(add(3, 4))
print(sub(4, 2))
