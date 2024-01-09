# 파이썬 통계분석(numpy, pandas)
교재 : 누구나 파이썬 통계분석
> 사용 라이브러리
>> import pandas as pd

## 데이터(p.20)
1. csv 파일 읽어 df에 저장
   - .(현재 내 jupyter파일이 있는 곳)에서부터 시작해서 csv가 있는 위치로 경로파악후 기입
   - `index_col`을 지정하지 않으면 0부터 index가 지정됨
2. 원하는 열('악력') 출력
```python
# 1, 2 예시
import pandas as pd
df = pd.read_csv('./data/ch1_sport_test.csv', index_col= '학생번호')
df['악력']
```
- df`.shape`    
: (n,n)과 같은 형식으로 데이터프레임의 크기를 알 수 있음
- df.iloc[1]   
: 1번인 행에 대한 모든 열에 대한 정보를 보고싶을때

### 변수의 종류
|척도|예|대소관계|차이|비|
|-|-|-|-|-|
|명의 척도|학생번호|X|X|X|
|순서 척도|성적 순위|O|X|X|
|간격 척도|온도|O|O|X|
|비례 척도|키|O|O|O|

## 1차원 데이터의 정리(p.30)

### 대표값(3M)

1. **평균값(mean)**
    - 기본계산   
    : sum(scores) / len(scores)
    - numpy   
    : np.mean(scores)
    - pandas   
    : scores_df.mean()

2. **중앙값(median)**
    - 기본계산   
    : 정렬 후 복잡한 계산 필요
    - np와 pd는 정렬 필요 X
    - numpy   
    : np.median(scores)
    - pandas   
    : scores_df.median()

3. **최빈값(mode)**
   - pandas    
   : scores_df.mode()
   - Series의 mode 메서드 사용   
   : sample_series.mode()

#### 기타코드1 
- 소수점 이하 출력 제한
    1. 쥬피터   
    %precision 3   
    2. 직접 df 입력 제한    
    pd`.set_option('display.precision', 3)`
- df.head()    
: df의 처음 5행을 표시

### 산포도
얼마나 퍼져있는지의 정도

#### 편차(deviation)
각 데이터가 평균으로부터 어느 정도 떨어져 있는가를 나타내는 지표   
>자료값과 평균의 차이

* 편차의 평균은 항상 0!

```python
mean = np.mean(scores)
deviation = scores - mean 
```

#### 기타코드2
- 컬럼 추가하는 법
  - array와 같은 래퍼런스 타입애들은 .copy를 사용
```python
summary_df = scores_df.copy()
summary_df['편차'] = deviation  
```
- df.rename(columns = {'a':'b'}, inplace = True)   
: 열이름 변경(a -> b)
- df.describe()   
: 평균, 표준편차(분산), 최소, 최대, 4분위수까지 모든 자료값이 계산되서 나옴

#### 분산(Variance)
얼마나 흩어져 있는지 알려주는 수치

- 계산코드
  1. np.mean(deviation ** 2)    
  : 하지만 원데이터의 편차를 구해야한다는 번거로움이 있음 
  2. np.var(scores)    
  : np에서는 문제가 없지만 pd에서는 다른 결과값을 나탈낼 수 있음
  3. scores_df.var(ddof=0)   
  : pd에서 분산을 나타낼때 항상 `ddof=0`을 지정

#### 표준편차(Standard Deviation)
자료가 평균을 중심으로 얼마나 펼쳐져 있는지 나타낸 수치
> 분산의 제곱근 

- 계산코드
    1. np.sqrt(var)   
    : 하지만 분산을 구해야하는 번거로움이 있음
    2. `np.std(scores, ddof=0)`
    : 한번에 구하는 방법

#### 범위 & 4분위수 범위
1. np.max(scores) - np.min(scores)   
:  하지만 최대에서 최소값을 뺀 것으로 이상값에 약하다라는 단점을 가지고 있음

> 이에 조금더 세분화된 4분위수를 사용

2. 4분위수 범위(IOR, InterQuartile Range)   
: 전체 자료의 50%에 포함되어 있는 정도
```python
Q1 = np.percentile(scores, 25)
Q3 = np.percentile(scores, 75)
IQR = Q3 - Q1
```

### 정규화(Normalization)
데이터를 통일된 지표로 변환

1. 표준화(Z-score)
데이터에서 평균을 빼고 표준편차로 나누는 작업
    > z = (scores - np.mean(scores)) / np.std(scores)

    평균 = 0, 표준편차 = 1

2. ~~편차값(우리나라에서는 거의 사용안함)~~

### 시각화

#### 도수분포표(Frequency Distribution)
점수를 각 구간에 나눠 빈도수를 볼 수 있음

- 코드작성법
  1. 0부터 100까지의 점수를 계급수 10으로 분류     
     - 빈도(freq)만 필요하니 10단위로 나오는계급값은 _로 의미를 부여하지 않음   
  2. 0~10, 10~20, ... 이라는 문자열의 리스트를 작성    
  3. freq_class(계급)를 인덱스로 DataFrame을 작성
```python
# 1
freq , _ = np.histogram(english_scores, bins = 10, range=(0, 100))
# 2
freq_class = [f'{i} ~ {i+10}' for i in range(0, 100, 10)]
# 3
freq_dist_df = pd. DataFrame({'frequency':freq}, index=pd.Index(freq_class, name='class'))
```
- 계급값   
: 각 계급을 대표하는 값으로, 계급의 중앙값이 이용
> class_vlaue = [(i+(i+10))//2 for i in range(0, 100, 10)]
- 상대도수   
: 전체 데이터에 대해 해당 계급의 데이터의 차지 비율
>  rel_freq = freq / freq.sum()
- 누적상대도수   
: 해당 계급까지의 상대도수의 합
> cum_rel_freq = np.cumsum(rel_freq)
- 도수의 최대값이 속한 index   
> idxmax = freq_dist_df['frequency'].idxmax()
- idxmax를 idx로 가지는 row의  '원하는 열'의 값을 보고 싶을때    
> freq_dist_df.loc[idxmax, '원하는 열의 이름을 넣기']

#### 히스토그램(histogram)
도수분포표를 막대그래프로 나눈것
> import matplotlib.pyplot as plt   
> [참고]그래프가 notebook위에 표시되기 원하면 아래 코드 입력   
> %matplotlib inline

- 코드작성법
    1. 캔버스를 생성
       - figsize로 가로, 세로 크기를 지정
    2. 캔버스 위에 그래프를 그리기 위한 영역을 지정   
       - 인수는 영역을 1×1개 지정、하나의 영역에 그린다는 것을 의미
    3. 계급수를 10으로 하여 히스토그램을 그림
    4. X축에 레이블 부여
    5. y축에 레이블 부여
    6. X축을 0, 10, 20, ..., 100 눈금으로 구분
    7. Y축을 0, 1, 2, ...의 눈금으로 구분
    8. 그래프 표시

```python
# 1
fig = plt.figure(figsize=(10, 6))

# 2
ax = fig.add_subplot(111)

# 3
freq, _, _ = ax.hist(english_scores, bins=10, range=(0, 100))

# 4 ~ 5
ax.set_xlabel('score')
ax.set_ylabel('person count')

# 6
ax.set_xticks(np.linspace(0, 100, 10+1))

# 7
ax.set_yticks(np.arange(0, freq.max()+1))

# 8
plt.show()
```
---
상대도수의 히스토그램을 누적상대도수의 꺾은선 그래프와 그리는법 
```python
fig = plt.figure(figsize=(10, 6))
ax1 = fig.add_subplot(111)
# Y축의 스케일이 다른 그래프를 ax1과 동일한 영역에 생성 (X축은 공유한다.)
ax2 = ax1.twinx()

# 상대도수의 히스토그램으로 하기 위해서는, 도수를 데이터의 수로 나눌 필요가 있음
# 이것은 hist의 인수 weight를 지정하면 실현 가능
rel_freq, _, _ = ax1.hist(english_scores, bins=25, range=(0, 100))
cum_rel_freq = np.cumsum(rel_freq)
class_value = [(i+(i+4))//2 for i in range(0, 100, 4)]

# 꺾은선 그래프를 그림
# 인수 ls를 '--'로 하면 점선이 그려짐
# 인수 marker를 'o'으로 하면 데이터 점을 그람
# 인수 color를 'gray'로 하면 회색으로 지정
ax2.plot(class_value, cum_rel_freq, ls='-', marker='*', color='gray')
# 꺾은선 그래프의 눈금선을 제거
ax2.grid(visible=False)

ax1.set_xlabel('score')
ax1.set_ylabel('relative freq')
ax2.set_ylabel('cumulative rel freq')
ax1.set_xticks(np.linspace(0, 100, 25+1))

plt.show()
```
- 하지만 여기서 가중치는 .002로 모든 요인이 같은걸 볼 수 있음. 그래서 가중치가 있고 없고는 사실 본 그래프에서 큰 차이가 나타나지는 않음

#### 상자 그림
```python
fig = plt.figure(figsize=(5, 3))
ax = fig.add_subplot(111)
ax.boxplot(english_scores, labels=['english'])
plt.show()
```