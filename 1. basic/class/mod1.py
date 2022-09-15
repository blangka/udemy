# 모듈 만들기
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


# import 할때 나오지 않고 해당 파일을 실행했을때만 나오게 하는 방법
if __name__ == "__main__":
    print(add(1, 4))
    print(sub(4, 2))
