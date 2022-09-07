# 함수
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


print(add(1, 4))
print(sub(4, 2))


# 튜플
def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result


result = add_many(1, 2, 3)

print(result)

# 딕셔너리
def print_kwargs(**kwargs):
    print(kwargs)


print_kwargs(a=1)
print_kwargs(name="foo", age=3)


# 함수 결과 값은 언제나 하나다.
def add_and_mul(a, b):
    return a + b, a * b


result = add_and_mul(3, 4)
print(result)

# 초기값 미리 설정하기
def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이 %d" % old)
    if man:
        print("남자")
    else:
        print("여자")


say_myself("임채홍", 3)

# global 명령어 사용하기
p = 1


def vartest():
    global p
    p = p + 1


vartest()
print(p)
print(1)
