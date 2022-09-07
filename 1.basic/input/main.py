# 간단하게 입력 받은 다음에 출력하는 예제
# print("hello " + input("what is your name?"))

# a = input("how old are you? ")
# print("you are " + a + " years old")

# 문자열 띄어 쓰기
print("hello", "world")

# 파일 읽고 쓰기
f = open("새파일.txt", "w")
f.close()

f = open("새파일.txt", "w")
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)

f = open("새파일.txt", "r")
line = f.readline()
print(line)

f = open("새파일.txt", "r")
while True:
    line = f.readline()
    if not line:
        break
    print(line)
f.close()


f = open("새파일.txt", "r")
lines = f.readlines()
for line in lines:
    print(line)
f.close()

f = open("새파일.txt", "r")
data = f.read()
print(data)
f.close()

with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")
