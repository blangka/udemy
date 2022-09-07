# 자료형 학습
# 정수형, 실수형, 문자열, 리스트, 튜플, 딕셔너리, 집합, 불리언
a = 123
b = 1.2
c = 4.24E10
d = "hello"
e = [1, 2, 3]
f = (1, 2, 3)
g = {"a": 1, "b": 2, "c": 3}
h = {1, 2, 3}
i = True

# 문자열 자료형의 종류
print("test")
print('test')
print('''test''')
print("""test""")

# 어떤때 사용하느냐면 문자열 안에 따옴표를 넣고 싶을때
print("test's")
# 백슬러시를 사용해서 따옴표를 넣을 수 있다.
print('test\'s')

# 문자열 곱하기
a = "test" * 3
print(a)

# 길이 구하기
print(len(a))

# 문자 인덱싱
a = "test is string"
print(a[0])
print(a[-1])
print(a[0:4])

# 슬라이싱
a = "20220101chicken19000"
date = a[:8]
menu = a[8:15]
money = a[15:]
print(date)

# 문자열 대입
a = "I eat %d apples." % 3
print(a)
a = "I eat %s apples." % "five"
print(a)

# 인덱스와 이름을 혼용해서 넣기
a = "I eat {0} apples. so I was sick for {1} days.".format(3, 10)
print(a)

# 왼쪽 정렬
a = "{0:<10}".format("hi")
print(a)

# 오른쪽 정렬
a = "{0:>10}".format("hi")
print(a)

# 가운데 정렬
a = "{0:^10}".format("hi")
print(a)

# 공백 채우기
a = "{0:=^10}".format("hi")
print(a)

# 소수점 표현
a = "{0:0.4f}".format(3.42134234)
print(a)

# f 문자열 포매팅
name = "홍길동"
age = 30
a = f"나의 이름은 {name}입니다. 나이는 {age}입니다."

# 위치 알려주기
a = "Life is too short"
print(a.index("t"))
print(a.find("t"))

# 문자열 삽입
a = ",".join("abcd")
print(a)

# 양쪽 공백지우기
a = " hi "
print(a.strip())

# 문자열 바꾸기
a = "Life is too short"
print(a.replace("Life", "Your leg"))

# 문자열 나누기
a = "Life is too short"
print(a.split())


# 리스트 자료형
a = [1, 2, 3]
print(a)

# 리스트 슬라이싱
a = [1, 2, 3, 4, 5]
print(a[0:2])

# del 함수 사용해 리스트 요소 삭제
a = [1, 2, 3]
del a[1]

# 리스트에 요소 추가
a = [1, 2, 3]
a.append(4)

# 리스트 정렬
a = [1, 4, 3, 2]
a.sort()

# 리스트 뒤집기
a = [1, 4, 3, 2]
a.reverse()

# 위치 반환
a = [1, 2, 3]
print(a.index(3))

# 리스트에 요소 삽입
a = [1, 2, 3]
a.insert(0, 4)

# 리스트 요소 제거
a = [1, 2, 3, 1, 2, 3]
a.remove(3)

# 리스트 요소 끄집어내기
a = [1, 2, 3]
a.pop()

# 리스트에 포함된 요소 x의 개수 세기
a = [1, 2, 3, 1]
print(a.count(1))

# 리스트 확장
a = [1, 2, 3]
a.extend([4, 5])

# 튜플 자료형 : 튜플은 리스트와 비슷하지만 다른 점이 있다.
# 리스트는 [과 ]으로 둘러싸지만 튜플은 (과 )으로 둘러싼다.
# 리스트는 그 값의 생성, 삭제, 수정이 가능하지만 튜플은 그 값을 바꿀 수 없다.
a = (1, 2, 3)
print(a)

# 딕셔너리 자료형
a = {"name": "pey", "phone": "0119993323", "birth": "1118"}

# 딕셔너리 쌍 추가
a = {1: "a"}
a[2] = "b"

# 딕셔너리 요소 삭제
a = {1: "a", 2: "b"}
del a[1]

# 딕셔너리를 사용하는 방법
a = {"name": "pey", "phone": "0119993323", "birth": "1118"}
print(a.keys())
print(a.values())
print(a.items())
print(a.get("name"))
print(a["name"])

# 딕셔너리 key 리스트 만들기
a = {"name": "pey", "phone": "0119993323", "birth": "1118"}
print(a.keys())
for k in a.keys():
    print(k)

# value 쌍 모두 지우기
a = {"name": "pey", "phone": "0119993323", "birth": "1118"}
a.clear()

# 해당 key가 딕셔너리 안에 있는지 조사하기
a = {"name": "pey", "phone": "0119993323", "birth": "1118"}
print("name" in a)

# 집합 자료형
s1 = set([1, 2, 3])
s2 = set("Hello")

# 집합 자료형의 특징
# 1. 중복을 허용하지 않는다.
# 2. 순서가 없다(Unordered).

# 불 자료형
a = True
b = False
print(type(a))
