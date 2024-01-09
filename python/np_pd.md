# numpy
행렬이나 대규모 다차원 `배열(ndarray)`을 쉽게 처리할 수 있도록 지원하는 파이썬 라이브러리

* 배열(array)의 특징
  1. 사이즈가 고정이다
  2. 바로 옆 주소에 존재함
  3. 맨 처음에 정수만 들어오겠다 하면 정수만 들어오고 실수만 들어오겠다 하면 실수만 들어와야함

* 리스트의 특징
  1. 사이즈가 가변이다
  2. 요소간 위치가 무작위다

> 그럼 왜 리스트를 바로 안 받고 배열을 쓰나?     
> 정답) 빠르고 기능이 많아 효율적임

- 항상 np라는 이름으로 임포트 해야함
> import numpy as np

* **브로드캐스트**   
마치 map처럼 array가 된 class에 2를 더할때 class안에 있는 모든요소에 각각 2가 더해짐. 이는 다른 연산자도 동일하게 수행됨 
```python
arr = [1, 2, 3, 4, 5]
arr + 2  # [3, 4, 5, 6, 7]
np.sqrt(arr) # array([1.        , 1.41421356, 1.73205081, 2.        , 2.23606798])
```
- arr`.shape` : 크기를 알수 있음
- arr`.dtype` : 속성을 알수 있음
- np`.linspace`(0, 3, 11) : start부터 end까지의 array를 생성하는 함수
- np`.random.randn(2, 3)` : 랜덤하게 아무 수를 추출
- 리스트를 array로 형변환
    1. 1차원
    ```python
    # python list
    data1 = [6, 3.4, 2, 0, 1]
    # np ndarray
    arr1 = np.array(data1)
    arr1
    ```
    2. 2차원
    ```python
    data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
    arr2 = np.array(data2)
    #      배열차원   배열 n*m
    arr2, arr2.ndim, arr2.shape
    ```
- arr`.ndim` : 차원확인
- np`.zeros`(n, n, n): 0을 원하는 차원으로 설정해서 나열   
- **range** 대응
  - np`.arange`(10)
  - np`.ones`(10) : 1을 나열
    - np`.ones_like`(l) : 똑같이 모양을 흉내내고 안에 값만 1로 치환 
  - np`.arange`(15)`.reshape`(3,5) : 0에서 14까지 범웨에서 3행 5열의 범위의 배열을 생성
- **형변환**
  - arr`.astype(np.float64)` : 정수타입으로 변환 
  - `실수 -> 정수로 변환할때` : 소수점은 모두 버림
```python
# 기타
# np.array 안에 있는 애들과 똑같은 형식으로 바꿔주세요. 느낌
float_arr = np.array([1.1])
str_arr.astype(float_arr.dtype)
```
- 산술연산: arr가 를 받을 때 각 위치에 해당되는 애들 끼리 연산됨

- **index**/**slicing**
  - 슬라이스 복사본 X 
  - 기존에서 필요한 부분만 다시 보여주기
  > 즉, 슬라이스는 복사가 아닌 Broadcating
  - 슬라이스로 복사본 만들기
    - copy_arr = arr[3:6]`.copy()`
  - 복사본과 원본이 다른걸 볼수 있음

- bool
  - 오직, array라서 가능
```python
names = np.array(['bob', 'joe', 'will', 'bob', 'will', 'joe', 'joe'])
names == 'bob'
array([ True, False, False,  True, False, False, False])
```
- row수와 index 배열의 개수가 맞다면 필터함수마냥 True인 애들만 남김
- false애들만 뽑기
  - `~`붙이기
```python
cond = names == 'bob'
data[~cond]
```
- Fancy Indexing
  - index 를 list로 넘기기
    ```python
     # 해당 index 순서대로 array를 재배치하여 제공
     arr[[4, 3, 0, 6]] 
     # 뒤의 순서대로 array를 재배치하여 제공
     arr[[-1, -3, -5]]
     ``` 

- arr`.T` : row/col 바꿈
  
## 수학 메서드/통계 메서드
1. arr.mean() : 전체 평균
2. np.mean(arr): 전체 평균
3. arr.sum(): 전체 총합
4. arr.sum(0) or arr.sum(axis=0): 각 열에 대한 합계
5. arr.sum(1) or arr.sum(axis=1): 각 행에 대한 합계

  
# pandas

   패널데이터와 데이터 어넬리틱스를 합친것으로 넘파이를 기반으로 만든것이 판다스.
   엑셀의 스프레드 시트와 넘파이의 배열 데이터 계산을 할수 있는 기능을 가지고 있음
   즉, `표(.csv) 데이터`를 처리하는데 특화되어있음