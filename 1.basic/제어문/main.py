# 제어문
# if 조건문:
money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

pocket = ["paper", "cellphone", "money"]

# while 조건문:
treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")

# for 변수 in 리스트(튜플, 문자열):
test_list = ["one", "two", "three"]
for i in test_list:
    print(i)

a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print(first + last)

# for와 range를 사용한 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print(i * j, end=" ")
    print("")
