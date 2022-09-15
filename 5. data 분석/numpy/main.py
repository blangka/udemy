import numpy as np

# 1차원 배열
data1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a1 = np.array(data1)
print(a1)

# 다 차원 배열
a2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a2)

# 범위를 지정해 배열 생성
# arr_obj = np.arange([start,] stop[, step])

print(np.arange(0, 10, 2))
print(np.arange(1, 10))
print(np.arange(5))

# 범위를 지정하지만 행렬 변화
b1 = np.arange(12).reshape(4, 3)
print(b1)
# 배열에 형태를 알기 위한것
print(b1.shape)

# linspace start부터 stop까지 num개의 배열을 생성한다 지정하지 않으면 50으로 간주한다.
print(np.linspace(0, np.pi, 20))

# 0이나 1로만 지정된 배열 생성
print(np.zeros(10))
print(np.zeros((3, 4)))
print(np.ones(5))
print(np.ones((3, 5)))

# 단위 행렬 n x n 인 정사각형에서 주 대각선은 1이고 나머지는 0인 행렬
print(np.eye(3))

# 배열의 데이터 타입변화 dtype='<U8' 의 의미는 유니코드 이며 최대 8개 라는 위미

print(np.array(["1.5", "0.62", "2", "3.141592"]))

# 문자 타입을 실수 타입으로 바꾸는 것
print(np.array(["1.5", "0.62", "2", "3.141592"]).astype(float))

# 난수 생성
print(np.random.rand())
print(np.random.rand(2, 3))

# 지정 범위 난수 생성
print(np.random.randint(1, 30))

# 배열 연산
arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([1, 2, 3, 4])

print(arr1 + arr2)

# 통계를 위한 연산
arr3 = np.arange(5)
print(arr3)

print([arr3.sum(), arr3.mean()])

# 누적합 & 곱
arr4 = np.arange(1, 5)
print(arr4.cumsum())
print(arr4.cumprod())

# 행렬곱
arr1 = np.array([0, 1, 2, 3]).reshape(2, 2)
arr2 = np.array([3, 2, 0, 1]).reshape(2, 2)
print(arr1.dot(arr2))

# 전치 행렬
print(np.transpose(arr1))
print(arr1.transpose())

# 역 행렬 (https://mathbang.net/567)
print(np.linalg.inv(arr1))

# 행렬식 (https://ko.wikipedia.org/wiki/%ED%96%89%EB%A0%AC%EC%8B%9D)
print(np.linalg.det(arr1))

# 인덱싱과 슬래이딩
# 배열을 다우다 보면 배열 요소를 이용해야 하는데 배열의 원소 선택하는것을 인덱싱, 범위를 지정해서 원소 선택하는 것을 슬라이싱

# 인덱싱
a1 = np.array([0, 10, 20, 30, 40, 50])
print(a1[0])
print(a1[[1, 3, 4]])

# 조건을 통한 인덱싱
print(a1[a1 > 20])

# 슬라이싱
print(a1[1:4])
print(a1[:3])
