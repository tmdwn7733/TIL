# python_intro
`연산자 좌우는 기본적으로 한칸씩 띄어써야함`   
`ctrl + 엔터` : 실행   
`#` or `''' '''` : 주석   
`00` : restart   
-> 인풋때문에 멈춰서 못찾을때 위 커널에서 interrupt kernel(ii), restart kernel(00) 누르기   


### `종류`
  - *Value* 타입(근본) -> 단일타입
      - 숫자 -> 연산
      - 문자 -> 연산
      - T/F -> 연산
      - None
 - *Ref* 타입_컨테이너
   - 리스트
   - 튜플   
     레인지랑 비슷하지만 수정이 안됨
   - 레인지
   - 딕셔너리
   - 셋


## 기초 문법(Syntax)
### `주석(Comment)`

* 한 줄 주석은 `#`으로 표현합니다. 

* 여러 줄의 주석은 
    1. 한 줄 씩 `#`을 사용해서 표현하거나,
    2. `"""` 또는 `'''`(여러줄 문자열, multiline string)으로 표현할 수 있습니다.
    (multiline은 주로 함수/클래스를 설명(docstring)하기 위해 활용됩니다.)


[주석에 대한 아티클](https://insight.infograb.net/blog/2023/08/16/good-code-annotation/)
    
개발은 혼자 하는게 아니기 때문. 남을 위해서 개발 혹은 같이 일하고 싶은 사람이라는 것은 남을 배려하는 사람이라는 것

### `코드 라인`
* 파이썬 코드는 '1줄에 1문장(statment)'이 원칙입니다.

* 문장(statement)은 파이썬이 실행 가능(executable)한 최소한의 코드 단위입니다. 

* 한 줄로 표기할때는 `;`을 작성하여 표기할 수 있습니다.   
  `But` 기본적으로 파이썬에서는 `;`을 작성하지 않습니다.

* 줄을 여러줄 작성할 때는 역슬래시`\`를 사용하여 아래와 같이 할 수 있다.  
  ```python
  print('hello \
  world')
  ```
* `[]` `{}` `()`는 `\` 없이도 가능합니다.
  ```python
  [
    1,
    2,
    3,
    4
      ]

## 변수

이름에 대한 얘기

### `할당 연산자(Assignment Operator): "="`

* 변수는 `=`을 통해 할당(assignment) 됩니다. 

* 해당 데이터 타입을 확인하기 위해서는 `type()`을 활용합니다.

* 해당 값의 메모리 주소를 확인하기 위해서는 `id()`를 활용합니다.
* e1_같은 값을 동시에 할당할 수 있습니다.   
    `파이썬에서만 가능!`

* e2_다른 값을 동시에 할당 가능합니다.
```python
e1: 
x = y = 1
x, y =1

e2:
x, y = 1, 2
```
* 이를 활용하면 서로 값을 바꾸고 싶은 경우 임시변수 스왑 혹은 연산을 통해 가능함
  
### `식별자(Identifiers)`

파이썬에서 식별자는 변수, 함수, 모듈, 클래스 등을 식별하는데 사용되는 이름(name)입니다. 

* 식별자의 이름은 영문알파벳(대문자와 소문자), 언더스코어(_), 숫자로 구성됩니다.
* 첫 글자에 숫자가 올 수 없습니다.
* 길이에 제한이 없습니다.
* 대소문자(case)를 구별합니다.
* 아래의 키워드는 사용할 수 없습니다.   
    * 정 원하면 아래 키워드에 새로운 이름을 부여하고 싶으면 부여할수는 있음. 그러나 그렇게 하면 아래 키워드가 가지고 있는 기능을 상실하기에 del을 사용해 삭제하고 다시 기능을 활용해야함.   
[파이썬 문서](https://docs.python.org/ko/3/reference/lexical_analysis.html#keywords)

```
False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield
```

## 데이터 타입

- **숫자**(Number) 타입
- **문자열**(String) 타입
- **참/거짓**(Boolean) 타입

### `숫자 타입`
####  (1) `int` (정수, ingteger)

모든 정수는 `int`로 표현됩니다.

Python3에서는 `long` 타입은 없고 모두 `int` 타입으로 표기 됩니다.

* 보통 프로그래밍 언어 및 Python2에서의 long은 OS 기준 32/64비트입니다.
* Python3에서는 모두 int로 통합되었습니다.

* 8진수 : `0o` / 2진수 : `0b` / 16진수: `0x` 로도 표현 가능합니다.    
컴퓨터는 원래 이진법으로 나온얘기라 십진법 제외 이진법의 확장만 있음

```python
bn = 0b10
on = 0o10
dn = 10
hn = 0x10
```

#### (2) `float` (부동소수점, 실수, floating point number)

실수는 `float`로 표현됩니다. 

다만, 실수를 컴퓨터가 표현하는 과정에서 부동소수점을 사용하며, 항상 같은 값으로 일치되지 않습니다. (floating point rounding error)

이는 컴퓨터가 2진수(비트)를 통해 숫자를 표현하는 과정에서 생기는 오류이며, 대부분의 경우는 중요하지 않으나 값을 같은지 비교하는 과정에서 문제가 발생할 수 있습니다.

* e를 사용하여 컴퓨터식 지수를 사용할 수 있음   
```python
print(314e-2)
print(123e3)
```
* 실수의 연산   
  -  `round()` 는 0~4는 내림, 5는 동일하게 작동하지 않고 반올림 방식에 따라 다름
  - `==`는 같다라는 기호, `=`는 할당을 하려는 기호
  - `math.isclose()` 를 이용해서 a와 b의 값이 같은지 확인할수 있음
  ```python
  import math
  math.isclose(3.5-3.12, .38
  ```
 
### `문자열(String) 타입`
#### 기본 활용법

* 문자열은 Single quotes(`'`)나 Double quotes(`"`)을 활용하여 표현 가능합니다.

    - 작은따옴표: `'"큰" 따옴표를 담을 수 있습니다'`

    - 큰따옴표: `"'작은' 따옴표를 담을 수 있습니다"`

    - 삼중 따옴표: `'''세 개의 작은따옴표'''`, `"""세 개의 큰따옴표"""`


* 단, 문자열을 묶을 때 동일한 문장부호를 활용해야하며, `PEP-8`에서는 **하나의 문장부호를 선택**하여 유지하도록 하고 있습니다. 
(Pick a rule and Stick to it)
* INPUT -> 무조건 문자열(STRING)
* 문자열 안에 문장부호(`'`, `"`)가 사용될 경우 이스케이프 문자(`\`)를 활용 가능
```python
print('철수가 말했다. \'안녕?\'')
```
* 여러줄에 걸쳐있는 문장은 다음과 같이 표현 가능합니다.    
  - PEP-8에 따르면 이 경우에는 반드시 `"""`를 사용하도록 되어 있다.
```python
print('''안녕
힘들다
숙취''')
```
* 문자열은 + 연산자로 이어붙이고, * 연산자로 반복시킬 수 있습니다.
  
#### 이스케이프 시퀀스
문자열을 활용하는 경우 특수문자 혹은 조작을 하기 위하여 사용되는 것으로 `\`를 활용하여 이를 구분합니다. 

|<center>예약문자</center>|내용(의미)|
|:--------:|:--------:|
|\n|줄 바꿈|
|\t|탭|
|\r|캐리지리턴|
|\0|널(Null)|
|\\\\ |`\`|
|\\'|단일인용부호(`'`)|
|\\"|이중인용부호(`"`)|

* print 함수의 end 옵션에도 이스케이프 문자를 사용할 수 있음
```python
print('안녕', end='\t')
print('하세요')
```   
* print 함수의 end 옵션의 기본은 \n
* end 옵션은 이스케이프 문자열이 아닌 다른 것도 가능
* end에 다른 문자열도 가능
  
#### `String interpolation(매우 중요하다고 언급함)`

* [`str.format()` ](https://pyformat.info/)

* [`f-strings`](https://www.python.org/dev/peps/pep-0498/) : 파이썬 3.6 이후 버전에서 지원
```python
ver1. 
'제 이름은 {}, 점수는 {} 입니다.'.format(name, score)
 
ver2. 
f'제 이름은 {name}, 점수는 {score} 입니다.'

ver3. 
print(f'''제 이름은 {name}, 
점수는 {score} 입니다.''')
```
### `참/거짓(Boolean) 타입`

파이썬에는 `True`와 `False`로 이뤄진 `bool` 타입이 있습니다.

비교/논리 연산을 수행 등에서 활용됩니다.

다음은 `False`로 변환됩니다.
```
0, 0.0, (), [], {}, '', None
```
- False에 가까운 아이들
    - 비어있다(0)
    - 없다(None)의 뉘앙스
- True는 위를 제외한 모든 것이라 생각하면 편함 

* `None`타입은 우리가 쓰는 것보다 파이썬이 쓰는 것으로 우리에게 아무것도 줄수 없을때 NoneType으로 반환해서 줌

### `형변환(Type conversion, Typecasting)`

파이썬에서 데이터타입은 서로 변환할 수 있습니다.

1. 암시적 형변환(Implicit Type Conversion)   
사용자가 의도하지 않았지만, 파이썬 내부적으로 자동으로 형변환 하는 경우입니다.
아래의 상황에서만 가능합니다.   
   * bool
   * Numbers (int, float, complex)

2. 명시적 형변환(Explicit Type Conversion)   
위의 상황을 제외하고는 모두 명시적으로 형변환을 해주어야합니다.

   * string -> intger  : 형식에 맞는 숫자만 가능
   * integer -> string : 모두 가능   
   
   암시적 형변환이 되는 모든 경우도 명시적으로 형변환이 가능합니다.

   * `int()` : string, float를 int로 변환
   * `float()` : string, int를 float로 변환   
     * float 3.5는 int로 변환이 가능합니다.
     *  하지만 소수점을 버림(내림)으로 해서 반환함
   * `str()` : int, float, list, tuple, dictionary를 문자열로 변환

    `list()`, `tuple()` 등은 다음 챕터에서 배울 예정

## 연산자(Operator)
### `산술 연산자`
Python에서는 기본적인 사칙연산이 가능합니다. 

|연산자|내용|
|----|---|
|+|덧셈|
|-|뺄셈|
|\*|곱셈|
|/|나눗셈|
|//|몫|
|%|나머지(modulo)|
|\*\*|거듭제곱|

- 나눗셈 (`/`) 은 항상 float를 돌려줍니다.
- 정수 나눗셈 으로 (소수부 없이) 정수 결과를 얻으려면 `//` 연산자를 사용

### `비교 연산자`
여기서 나오는 트루와 폴스는 새로운 값으로 태어나는 거지 이게 맞다 틀리다라고 인정해주는게 아님

우리가 수학에서 배운 연산자와 동일하게 값을 비교할 수 있습니다.

|연산자|내용|
|----|---|
|`<`|미만|
|`<=`|이하|
|`>`|초과|
|`>=`|이상|
|`==`|같음|
|`!=`|같지않음|
|`is`|객체 아이덴티티|
|`is not`|부정된 객체 아이덴티티|

### `논리 연산자`

|연산자|내용|
|---|---|
|a and b|a와 b 모두 True시만 True|
|a or b|a 와 b 모두 False시만 False|
|not a|True -> False, False -> True|

우리가 보통 알고 있는 `&` `|`은 파이썬에서 비트 연산자

* 파이썬에서 and는 a가 거짓(F)이면 a를 리턴하고, 참(T)이면 b를 리턴합니다.   
  -  즉, false값을 찾으면 바로 그값은 반환함
* 파이썬에서 or은 a가 참(T)이면 a를 리턴하고, 거짓(F)이면 b를 리턴합니다.

### `단축평가`
* 첫 번째 값이 확실할 때, 두 번째 값은 확인 하지 않습니다.
* 조건문에서 뒷 부분을 판단하지 않아도 되기 때문에 속도가 향상됩니다.

>True and True and False and True면 False가 나옴

```python
'a' and 'b' # b 반환
'a' or 'b' # a 반환
```

- `and` 는 둘 다 True일 경우만 True이기 때문에 첫번째 값이 True라도 두번째 값을 확인해야 하기 때문에 'b'가 반환됩니다.
- `or` 는 하나만 True라도 True이기 때문에 True를 만나면 해당 값을 바로 반환합니다.
```python
'a' and 10 and True and 0 and 4 and 3.14 and 'asdf' 
# 0 반환

0 or '' or False or '0' or None or [] or () or {} 
# '0' 반환
```
### `복합 연산자`

복합 연산자는 연산과 대입이 함께 이뤄집니다. 

가장 많이 활용되는 경우는 반복문을 통해서 갯수를 카운트하거나 할 때 활용됩니다.

|연산자|내용|
|----|---|
|a += b|a = a + b|
|a -= b|a = a - b|
|a \*= b|a = a \* b|
|a /= b|a = a / b|
|a //= b|a = a // b|
|a %= b|a = a % b|
|a \*\*= b|a = a ** b|

* 좌항 우항의 기준의 값이 같을때만 사용 가능
```python
a = 1
a = a + 1
# a += 1
print(a)


b = 3
# b *= 4
b = 3 * 4
print(b)
```

* 복합연산자는 아래예시때 사용이 많이 됨   
    - 0으로 할당된 변수 cnt를
    - 반복문 while 을 이용하여 5회 반복하는데
    - 반복하는 동안 cnt를 print로 출력하고 cnt에 1씩 더해봅시다.
    - 단, cnt 를 더할때는 복합연산자를 사용해봅시다.
```python
cnt = 0
while cnt < 5:
    print(cnt)
    cnt += 1
```

### `기타 주요 연산자`

#### Concatenation

* 숫자가 아닌 자료형은 `+` 연산자를 통해 합칠 수 있음
  * 숫자끼리 더하면 add라는 의미가 되고 문자끼리 더하면 연결(concatanation?)의 의미가 됨

#### containment Test
* `in` 연산자를 통해 요소가 속해있는지 여부를 확인할 수 있습니다.

#### Identity
* `is` 연산자를 통해 동일한 object인지 확인할 수 있습니다. (OOP 파트에서 다시 학습)

#### Indexing/Slicing
* `[]`를 통한 값을 접근하고, `[:]`을 통해 슬라이싱할 수 있습니다.`0부터 시작을 함`

### `연산자 우선순위`

0. `()`을 통한 grouping
1. Slicing
2. Indexing
3. 제곱연산자`**`
4. 단항연산자`+`, `-` (음수/양수 부호)
5. 산술연산자`*`, `/`, `%`
6. 산술연산자`+`, `-`
7. 비교연산자, `in`, `is`. `not`
9. `and` 
10. `or`

[파이썬 문서](https://docs.python.org/ko/3/reference/expressions.html#operator-precedence)


# 컨테이너(Container)
여러 개의 값을 저장할 수 있는 것(~~객체~~)

- 시퀀스(Sequence)형: 순서가 있는(ordered) 데이터
- 비 시퀀스(Non-sequence)형: 순서가 없는(unordered) 데이터

## 시퀀스(sequence)형 컨테이너
`시퀀스`는 데이터가 순서대로 나열된(ordered) 형식을 나타냅니다. 

* **주의! 순서대로 나열된 것이 `정렬되었다(sorted)`라는 뜻은 아닙니다.**

* 특징
1. 순서를 가질 수 있습니다
   여기서 말하는 순서가 1234가 아닌 3412처럼 있어도 ~번째 위치에 있다 라는 것을 의미


3. **특정 위치의 데이터를 가리킬 수 있습니다.**

* 종류   
파이썬에서 기본적인 시퀀스 타입은 다음과 같습니다.

  * 리스트(list)
    
  * 튜플(tuple)

  * 레인지(range)

  * *문자형(string)*

  * *바이너리(binary)* : 따로 다루지는 않습니다.

### `리스트(list)`

<center><img src="https://user-images.githubusercontent.com/18046097/61180421-fe90ae80-a650-11e9-8211-d06f87756d05.png", alt="list figure"/></center>

**활용법**
```python
[value1, value2, value3]
```

리스트는 대괄호`[]` 및 `list()` 를 통해 만들 수 있습니다.

값에 대한 접근은 `list[i]`를 통해 합니다.
* 리스트/튜플 은 변수명을 복수형으로 만든다.
* , 뒤에 띄어쓰기 필수

### `튜플(tuple)`
**활용법**
```python
(value1, value2)
```

튜플은 리스트와 유사하지만, `()`로 묶어서 표현합니다.

그리고 tuple은 수정 불가능(불변, immutable)하고, 읽을 수 밖에 없습니다.

직접 사용하기 보다는 파이썬 내부에서 다양한 용도로 활용되고 있습니다.

* 변수의 값을 swap하는 코드 역시 tuple을 활용하고 있습니다.
* 변수명이 single_tuple인 하나의 요소(값)로 구성된 tuple   
    * 하나의 요소(값)로 구성된 tuple은 값 뒤에 쉼표를 붙여서 만듭니다.   
    -> single = (1, )

### `레인지(range())`
`range` 는 숫자의 시퀀스를 나타내기 위해 사용됩니다.
`연속된 정수만 표현함`

기본형 : `range(n)` 


> 0부터 n-1까지 값을 가짐


범위 지정 : `range(n, m)` 

> n부터 m-1까지 값을 가짐

범위 및 스텝 지정 : `range(n, m, s)`

> n부터 m-1까지 +s만큼 증가한다

### 시퀀스에서 활용할 수 있는 연산자/함수

시퀀스는 순서가 있는 애들
|operation|설명|
|---------|---|
|x `in` s	|containment test|
|x `not in` s|containment test|
|s1 `+` s2|concatenation|
|s `*` n|n번만큼 반복하여 더하기
|`s[i]`|indexing|
|`s[i:j]`|slicing|
|`s[i:j:k`]|k간격으로 slicing|
|len(s)|길이|
|min(s)|최솟값|
|max(s)|최댓값|
|s.count(x)|x의 개수|

## 비 시퀀스형(Non-sequence) 컨테이너
> 순서가 없다라는 거보다는 idex(숫자) 접근이 안된다 정도로 보는게 좋음

- 세트(set)

- 딕셔너리(dictionary)

### `세트(set{})`
`set`은 순서가 없고 중복된 값이 없는 자료구조입니다.(e.g. 벤다이어그램)

* `set`은 수학에서의 집합과 동일하게 처리됩니다. 

* `set`은 중괄호`{}`를 통해 만들며, 순서가 없고 중복된 값이 없습니다.

* 빈 세트를 만들려면 `set()`을 사용해야 합니다. (`{}`로 사용 불가능)

* 활용 가능한 연산자는 차집합(`-`), 합집합(`|`), 교집합(`&`)입니다.

  * 하지만 어떤 데이터와 쓰이냐에 따라 연산자의 활용이 달라질수 있음

#### 활용법
```python
{value1, value2, value3}
```
* `set`을 활용하면 `list`의 중복된 값을 손쉽게 제거할 수 있습니다.
* 단, `set`으로 변환하는 순간 순서를 보장할 수 없습니다.
* 정렬상에 순서가 있을순 없음. 그냥 얘네가 선택해서 준거로 중복을 제거 했다 정도로만 인식 -> `But! 리스트는 순서가 있음`

### `★(중요)딕셔너리(dictionary{:})`
`dictionary`는 `key`와 `value`가 쌍으로 이뤄져있습니다.


<center><img src="https://user-images.githubusercontent.com/18046097/61180427-1405d880-a651-11e9-94e1-1cc5c2a2ff34.png"></center> 

#### 활용법

```python
{Key1:Value1, Key2:Value2, Key3:Value3, ...}
```

* `{}`를 통해 만들며, `dict()`로 만들 수 있습니다.
  * set과 헷갈릴수는 있지만 우선 dic은 :이 들어가 있어서 충분히 구분히 가능하고 빈공간도 dic만 가능
* `key`는 **변경 불가능(immutable)한 데이터**만 가능합니다. (immutable : string, integer, float, boolean, tuple, range)
    * 95%가 string임. 그리고 int(4%)와 튜플(1%)은 코테때나 나옴. 사실상 99% string임
* `value`는 `list`, `dictionary`를 포함한 모든 것이 가능합니다.
* dictionary에 중복된 key는 존재할 수가 없습니다.   
  * 랜덤으로 하나가 날라감
* 중괄호 쓰는 셋과 딕션은 순서가 없는애들이라 매서드를 사용해서 확인해야함    
  * `매서드`를 활용하여 key, calue, item을 확인할수 있음   
    * 특징으로 앞에 .(점)이 찍혀있음
    * .key(), .values(), .items()
    * items는 튜플로 반환해서 나옴

```python
# dict 변경을 조금 유심히 봐야함.

d = {'a': 1, 'b': 2}

# dict의 value 조회를 원하면 key를 넣어야함
d['a']

# dict의 존재하지 않는 key 로 Value를 조회 
#d['c'] # key error

# dict 존재하는 key -> Value 변경
d['a'] = 100
print(d)

# dict 존재하지 않는 key  => key-value 추가
d['c'] = 3
print(d)
```

### 컨테이너형 형변환
파이썬에서 컨테이너는 서로 변환할 수 있습니다.

<img width="708" alt="typecasting" src="https://user-images.githubusercontent.com/18046097/61180466-a6a67780-a651-11e9-8c0a-adb9e1ee04de.png">

* 다른건 해보면 당연하게 느껴지지만 다만 dict은 반대로 되는 경우가 있음   
* 왜냐면 없는걸 만들진 못해도 있는걸 버리는 건 쉬워서 key만 남음

```python
# dictionary를 형변환 해봅시다.

d = {'a': 1, 'b': 2}

str(d) # "{'a': 1, 'b': 2}"
list(d) # ['a', 'b']
tuple(d) # ('a', 'b')
set(d) # {'a', 'b'}
range(d) # X
```

### 데이터의 분류
> `mutable` vs. `immutable`

데이터는 크게 변경 가능한 것(`mutable`)들과 변경 불가능한 것(`immutable`)으로 나뉘며, python은 각각을 다르게 다룹니다.

* 노션의 `복제`와 `링크 복사`의 개념과 비슷한것 같음

#### (1) 변경 불가능한(`immutable`) 데이터
벨류타입 애들이 변경불가능하고 튜플도 변경불가능함. 
* 리터럴(literal)

    - 숫자(Number)
    - 글자(String)
    - 참/거짓(Bool)

* range()

* tuple()

* frozenset()

#### (2) 변경 가능한(mutable) 테이블
* list
* dict
* set

## 정리_컨테이너(Container)
<center><img src="https://user-images.githubusercontent.com/18046097/61180439-44e60d80-a651-11e9-9adc-e60fa57c2165.png", alt="container"/></center>    


# 제어문(Control flow)
[파이썬 문서](https://docs.python.org/ko/3/tutorial/controlflow.html)


이 경우, **코드 실행의 순차적인 흐름을 제어**(Control Flow)할 필요가 있습니다.

이러한 순차적인 코드의 흐름을 제어하는 것을 제어문이라고 하고, 제어문은 크게 **조건문**과 **반복문**으로 나눌 수 있습니다. 

제어문을 통해 다음과 순서도(Flow Chart)를 코드로 표현할 수 있습니다.

<center> 
    <img src="https://user-images.githubusercontent.com/18046097/61180553-25e87b00-a653-11e9-9895-7976d7204734.png", alt='if flowchart'/>
</center>
  
```python
a = 5

if a > 5:
    print('5 초과')
else:
    print('5 이하')

print(a)
```

## 조건문
### `if` 조건문의 구성
`if` 문은 반드시 **참/거짓을 판단할 수 있는 조건**과 함께 사용이 되어야합니다.
활용법

- **문법**

```python
if <expression>:
    <코드 블럭>
else:
    <코드 블럭>
```

- **예시**

```python
if a > 0:
    print('양수입니다.')
else:
    print('음수입니다.')
```
* `expression`에는 일반적으로 참/거짓에 대한 조건식이 들어갑니다.
* if 뒤에 `false`면 밑에꺼가 `True`면 위에거가 출력됨

* **조건**이 **참**인 경우 `:` 이후의 문장을 수행합니다.

* **조건**이 **거짓**인 경우 `else:` 이후의 문장을 수행합니다.

* 여러 개의 `elif` 부가 있을 수 있고(없거나), `else`는 선택적으로 사용합니다.

#### 주의사항
* 이때 반드시 **들여쓰기**를 유의해야합니다. 
    - 파이썬에서는 코드 블록을 자바나 C언어의 `{}`와 달리 **들여쓰기**로 판단하기 때문입니다.
* 앞으로 우리는 [PEP 8](https://www.python.org/dev/peps/pep-0008/#indentation)에서 권장하는 **4spaces**를 사용합니다. or `tab`
<center>
    <img src="https://user-images.githubusercontent.com/18046097/61180564-3a2c7800-a653-11e9-9fba-d60d2688ed3a.png", alt="if style"/>
</center>

### `elif` 복수 조건

2개 이상의 조건을 활용할 경우 `elif <조건>:`을 활용합니다.
<center>
<img src="https://user-images.githubusercontent.com/18046097/61180560-3993e180-a653-11e9-8263-79bd7bc6eed7.png", alt="elif">
</center>
* if, elif, else 문을 활용함
  
```python
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')
```
### `중첩` 조건문(Nested Conditional Statement)

조건문은 다른 조건문에 중첩될 수도 있습니다.

> 예시   
> 95점 이상이면, "참 잘했어요"도 함께 출력해주세요.

```python
score = int(input('점수를 입력하세요 : '))

if score >= 90:
    print('A')
    if score >= 95:
        print('참 잘했어요.')
elif score < 90 and score >= 80:
    print('B')
elif score < 80 and score >= 70:
    print('C')
elif score < 70 and score >= 60:
    print('D')
else:
    print('F')

```

### `조건 표현식`(Conditional Expression)

* 조건 표현식은 일반적으로 조건에 따라 값을 정할 때 활용됩니다.

* **삼항 연산자(Ternary Operator)**라고 부르기도 합니다.

---

**활용법**

```python
true_value if <조건식> else false_value

1 if [] else 3
# 3으로 결과값이 나오는데 이말은 중간의 값이 false이기에 else의 값인 false가 나오고 만약 1같은 true값이면은 if의 값인 1의 값이 나옴.
```

## 반복문(Loop Statement)
* while
* for

### `while` 반복문

`while` 문은 조건식이 참(`True`)인 경우 반복적으로 코드를 실행합니다.
if는 일회성으로 끝내는 거라면 while은 조건이 True라면 계속 반복

#### 활용법
- **문법**

```python
while <조건식>:
    <코드 블럭>
```

- 예시
`
```python
while True:
    print('조건식이 참일 때까지')
    print('계속 반복')
```

#### 주의사항
* `while` 문 역시 조건식 뒤에 콜론(`:`)이 반드시 필요하며, 이후 실행될 코드 블럭은 **4spaces**로 **들여쓰기**를 합니다.
* **반드시 종료조건을 설정해야 합니다.**


<br>
<center>
    <img src="https://user-images.githubusercontent.com/18046097/61180567-3ac50e80-a653-11e9-9f12-39c404f4be30.png", alt="">
</center>
<br>
<center>
    <img src="https://user-images.githubusercontent.com/18046097/61180568-3ac50e80-a653-11e9-9960-ba15137290a6.png", alt="while"/>
</center>

```python
a = 0
while a < 5:
    a += 1

print('끝')
```
### `for` 문

`for` 문은 시퀀스(string, tuple, list, range)를 포함한 순회가능한 객체(iterable)의 요소들을 순회합니다.   

while이 수동이라면 for은 자동

---

#### 활용법
- **문법**

```python
for <임시변수> in <순회가능한데이터(iterable)>:
    <코드 블럭>
```

- **예시**

```python
for menu in ['김밥', '햄버거', '피자', '라면']:
    print(menu)
```
<center>
    <img src="https://user-images.githubusercontent.com/18046097/61180565-3a2c7800-a653-11e9-806a-28838248de31.png", alt="">
</center>

```python
menus = ['삼겹살', '아구찜', '방어']

for memu in menus:
    print(menus)
```
![for animation](https://user-images.githubusercontent.com/18046097/61180563-3a2c7800-a653-11e9-8a7a-c7d6e6b30141.gif)

* `for` 문에서 요소 값에 다른 값을 할당해도 다음 반복구문에 영향을 주지 않습니다.

* 다음 요소 값에 의해 덮어 씌워지기 때문입니다.

```python
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num)
    num = 1
```

### 리스트(list) 순회에서 index의 활용하기

#### (1) `range(리스트의 길이)`
`range()`와 순회할 list의 길이를 활용하여 index를 조작 가능합니다.
> 0부터 리스트의 길이 만큼의 범위를 순회하면서 인덱스 숫자를 출력하는 for 문을 작성해봅시다.
lunch = ['짜장면', '초밥', '피자', '대방어회']

```python
for i in range(len(lunch)):
    print(lunch[i])
```
> 순서를 함께 출력   
> 출력 예_   
> 1번째 메뉴: 짜장면   
> 2번째 메뉴: 초밥   
> 3번째 메뉴: 피자   
> 4번째 메뉴: 대방어회
```python
for idx in range(len(lunch)):
    menu = lunch[idx]
    print(f'{idx+1}번째 메뉴: {menu}')
```

#### (2) Enumerate()
인덱스(index)와 값(value)을 함께 활용 가능합니다.

> `enumerate()`를 활용하면, 추가적인 변수를 활용할 수 있습니다.
- `enumerate()`는 [내장 함수](https://docs.python.org/ko/3.6/library/functions.html) 중 하나이며, 다음과 같이 구성되어 있습니다.
>
> <center>
    <img src="https://user-images.githubusercontent.com/18046097/61180561-3993e180-a653-11e9-9558-085c9a0ad65d.png", alt="enumerate">
</center>

* enumerate는 index 값을 같이 꺼내줌
* enumerate 를 for에서 돌리면 튜플이 나오므로, 즉, 처음에 임시변수를 할당해 쪼개서 넣으면 튜플이 할당되서 알아서 나옴.

```python
for idx, menu in enumerate(lunch, start=1): # 숫자를 1부터 카운트 할 수도 있음. 많이 사용하니 체크!
    print(idx, menu)
```
* 왜 for문에서 index가 중요할까?

```python
numbers = [1, 2, 3]

# numbers 안바뀜
for num in numbers:
    print(num)
    num *= 2

print(numbers)
print()

#numbers 바뀜
for idx in range(len(numbers)):
    print(numbers[idx])
    numbers[idx] *= 2

print(numbers)

# 하지만 첫번째로 하는 경우에는  기존값의 변경이 되지 않음. 즉, 원본 값이 변경됨됨
```

### `반복제어`(break, continue, for-else)
코테를 제외한 거의 안씀

#### (1) `break` 

반복문을 종료합니다.

* `for` 나 `while` 문에서 빠져나갑니다.

#### (2) `continue`

`continue`문은 continue 이후의 코드를 수행하지 않고 *다음 요소부터 계속(continue)하여* 반복을 수행합니다.
*  break가 전체 종료라면 continue는 해당 회차만 종료

#### (3) `else`
else는 완주메달로 break가 실행되지않아 끝까지 완주했을때 메달이 걸림. 그래서 else가 실행됨.
> 'break' 가 있을때만 'else'를 고려

끝까지 반복문을 실행한 이후에 실행됩니다.
- 반복에서 리스트의 소진이나 (`for` 의 경우) 조건이 거짓이 돼서 (`while` 의 경우) 종료할 때 실행됩니다. 
- 하지만 반복문이 **`break` 문으로 종료될 때는 실행되지 않습니다.** (즉, `break`를 통해 중간에 종료되지 않은 경우만 실행)

# 함수(function)
> 가독성, 재사용성, 유지보수

## 요약

1. 정의(define) 과 호출(call)
2. in & out
3. out (return)
    - 리턴값은 단 하나의 값
    - return 키워드를 만나면 그 자리에서 함수 종료
    - return 키워드가 없으면 코드 끝나고 None 을 반환
    - return 만 있고 그 뒤에 아무말 없으면 그 자리에서 종료하고 None 을 반환
    - print 는 리턴 없는(None) 함수
4. in (parameter(x) > 매개변수 or 정의파트 / argument > 전달인자 or 호출파트)c
   - 있을수도 있고 없을수도 있다
   - 기본적으로 위치(자리)에 맞춰 들어간다
   - 정의할 때는 기본값(default value) 세팅 가능
   - 실행할 때는  위치 안맞추고 키워드로 실행 가능
  > 인자의 경우 위치가 중요한데 만약 위치 안맞출거면 정의를 해줘야함. 하지만 정의를 해줄거면 =붙은거를 맨뒤에 넣어줘야함

   - 여러개를 묶어서 받을 수 있다
        - 값들만 받으면 func(1, 2, 3)  => def func(*args) 처럼 튜플로 묶어서 받을 수 있다.
        - 값과 이름을 같이 받으면 func(a=1, b=2, c=3) => def func(**kwargs) 처럼 딕셔너리로 묶어서 받을 수 있다.

## 종류

<center>
    <img src="https://user-images.githubusercontent.com/18046097/61181739-2984fd80-a665-11e9-991b-f2f058397a69.png", alt="built_in">
</center>

[파이썬 문서](https://docs.python.org/ko/3/library/functions.html)

## 스코프(scope)

함수는 코드 내부에 스코프(scope)를 생성합니다. 함수로 생성된 공간은 `지역 스코프(local scope)`라고 불리며, 그 외의 공간인 `전역 스코프(global scope)`와 구분됩니다.   
스코프 = 범위, 영역

> 파이썬은 블럭스코프가 아니고 함수 스코프다.

* **전역 스코프(`global scope`)**: 코드 어디에서든 참조할 수 있는 공간
* **지역 스코프(`local scope`)**: 함수가 만든 스코프로 함수 내부에서만 참조할 수 있는 공간
  
```python
# global과 local의 예시

재석 = '유'

def 집1():
    재석 = '김'
    print(재석)
집1() # 우리집 재석이 김재석이 찾는거니?

def 집2():
    print(재석)
집2() # 우리집엔 재석이가 없네? 글로벌을 가져오쟈

print(재석) # 그냥 글로벌을 가져오자
```

* **전역 변수(`global variable`)**: 전역 스코프에 정의된 변수
* **지역 변수(`local variable`)**: 로컬 스코프에 정의된 변수

### scope 요약 
1. 코드가 함수 정의 외부에 있다. -> Global
2. 코드가 함수 정의 내부에 있다. -> Local
3. 함수는 호출하면, Scope를 만들며, 종료되면 Scope는 사라진다.
4. Local에서 Global 참조는 가능하다. 반대는 불가능
5. Local과 Global에 같은 이름(변수, 함수 등)이 있다면, 함수 내부에서는 Local을 더 우선시 한다.

### 변수의 수명주기(lifecycle)

변수의 이름은 각자의 `수명주기(lifecycle)`가 있습니다.

* **빌트인 스코프`(built-in scope)`**: 파이썬이 실행된 이후부터 영원히 유지


* **전역 스코프`(global scope)`**: 모듈이 호출된 시점 이후 혹은 이름 선언된 이후부터 인터프리터가 끝날 때 까지 유지


* **지역(함수) 스코프`(local scope)`**: 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지 (함수 내에서 처리되지 않는 예외를 일으킬 때 삭제됨)

## 이름 검색(resolution) 규칙

[파이썬튜터사용 추천](https://pythontutor.com/visualize.html#)

파이썬에서 사용되는 이름(식별자)들은 이름공간(namespace)에 저장되어 있습니다.

아래와 같은 순서로 이름을 찾아나가며, `LEGB Rule` 이라고 부릅니다.

그래서 만약에 print에 이름을 지어주면 그건 글로벌이 되기때문에 나중에 빌트인이 되는 함수인 print의 기능을 쓰지 못함

* `L`ocal scope: 함수


* `E`nclosed scope: 특정 함수의 상위 함수 


* `G`lobal scope: 함수 밖의 변수 혹은 import된 모듈


* `B`uilt-in scope: 파이썬안에 내장되어 있는 함수 또는 속성
    * 우리가 안만들었는데 사용할수 있으면 빌트인(e.g. print())

```
1. `print()` 코드가 실행되면


2. 함수에서 실행된 코드가 아니기 때문에 `L`, `E` 를 건너 뛰고,


3. `print`라는 식별자를 Global scope에서 찾아서 `print = 'hi'`를 가져오고, 


4. 이는 함수가 아니라 문자열이기 때문에 `not callable`하다라는 오류를 내뱉게 됩니다.


5. 우리가 원하는 `print()`은 Built-in scope에 있기 때문입니다.
```
* 기본적으로 함수에서 선언된 변수는 Local scope에 생성되며, 함수 종료 시 사라집니다.
* 해당 스코프에 변수가 없는 경우 LEGB rule에 의해 이름을 검색합니다.
    * 변수에 접근은 가능하지만, 해당 변수를 수정할 수는 없습니다.
    * 값을 할당하는 경우 해당 스코프의 이름공간에 새롭게 생성되기 때문입니다.
    * **단, 함수 내에서 필요한 상위 스코프 변수는 인자로 넘겨서 활용합니다.** (클로저 제외)
* 상위 스코프에 있는 변수를 수정하고 싶다면 global, nonlocal 키워드를 활용 가능합니다.
    * 단, 코드가 복잡해지면서 변수의 변경을 추적하기 어렵고, 예기치 못한 오류가 발생합니다.
  
## 재귀함수(팩토리얼, 피보나치)
재귀 함수는 함수 내부에서 자기 자신을 호출 하는 함수를 뜻합니다.

알고리즘을 설계 및 구현에서 유용하게 활용됩니다.

### 팩토리얼 계산
> 팩토리얼은 1부터 n 까지 양의 정수를 차례대로 곱한 값이며 `!` 기호로 표기합니다. 예를 들어 3!은 3 * 2 * 1이며 결과는 6 입니다.
>
> `팩토리얼(factorial)`을 계산하는 함수 `fact(n)`를 작성하세요. 
>
> n은 1보다 큰 정수라고 가정하고, 팩토리얼을 계산한 값을 반환합니다.

$$
\displaystyle n! = \prod_{ k = 1 }^{ n }{ k }
$$

$$
\displaystyle n! = 1*2*3*...*(n-1)*n
$$

---
```python
# 재귀를 이용한 팩토리얼 계산
def factorial(n):
    if n == 1:
        return 1 # base case로 재귀함수에서 꼭 필요함. 없으면 무한 굴레에 빠짐
    return n * factorial(n-1)
```
### 반복문과 재귀함수

```python
factorial(3)
3 * factorail(2)
3 * 2 * factorial(1)
3 * 2 * 1
3 * 2
6
```

* 두 코드 모두 원리는 같습니다! 


1. 반복문 코드
    - n이 1보다 큰 경우 반복문을 돌며, n은 1씩 감소합니다. 
    - 마지막에 n이 1이면 더 이상 반복문을 돌지 않습니다.
  
  
2. 재귀 함수 코드
    - 재귀 함수를 호출하며, n은 1씩 감소합니다. 
    - 마지막에 n이 1이면 더 이상 추가 함수를 호출하지 않습니다.

* 재귀함수는 기본적으로 같은 문제이지만 점점 범위가 줄어드는 문제를 풀게 됩니다.

* 재귀함수를 작성시에는 반드시, `base case`가 존재 하여야 합니다. 

* `base case`는 점점 범위가 줄어들어 반복되지 않는 최종적으로 도달하는 곳을 의미합니다. 

* 재귀를 이용한 팩토리얼 계산에서의 base case는 **n이 1일때, 함수가 아닌 정수 반환하는 것**입니다.
* 자기 자신을 호출하는 재귀함수는 알고리즘 구현시 많이 사용됩니다.
* 코드가 더 직관적이고 이해하기 쉬운 경우가 있습니다. 
* 팩토리얼 재귀함수를 [Python Tutor](https://goo.gl/k1hQYz)에서 확인해보면, 함수가 호출될 때마다 메모리 공간에 쌓이는 것을 볼 수 있습니다.
* 이 경우, 메모리 스택이 넘치거나(Stack overflow) 프로그램 실행 속도가 늘어지는 단점이 생깁니다.
* 파이썬에서는 이를 방지하기 위해 1,000번이 넘어가게 되면 더이상 함수를 호출하지 않고, 종료됩니다. (최대 재귀 깊이)

### 피보나치수열
첫째 및 둘째 항이 1이며 그 뒤의 모든 항은 바로 앞 두 항의 합인 수열입니다. 

(0), 1, 1, 2, 3, 5, 8

> 피보나치 수열은 다음과 같은 점화식이 있습니다. 
>
> 피보나치 값을 리턴하는 두가지 방식의 코드를 모두 작성해주세요.
>

$$
\displaystyle F_0 = F_1 = 1
$$

$$
F_n=F_{n-1}+F_{n-2}\qquad(n\in\{2,3,4,\dots\})
$$

1) `fib(n)` : 재귀함수

2) `fib_loop(n)` : 반복문 활용한 함수

---

```python
# 재귀를 이용한 코드 fib()
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)

# 반복문(for문)을 이용한 코드 fib_loop()
def fib_loop(n):
    # 실제 피보나치 수열을 쭉 저장
    result = [0, 1]
    for _ in range(n-1):
        result.append(result[-1] + result[-2])
    return result[n]
```

# 데이터 구조(.method())
* dir 함수로 문자열이 가지고 있는 메소드를 확인   
**dir(string) or dir(list)
**

## 문자열(String)

> string에서는 아래 세가지가 가장 많이 쓰인다.
> 1. split
> 2. replace
> 3. join

1. 조회/탐색   
   - .find(x)   
   : x의 첫번째 위치를 반환. 없으면, -1 반환
   - .index(x)    
   : x의 첫번째 위치를 반환. 없으면, 오류반환
2. 문자열 변경
   - .replace(old, new[, count])   
   : 바꿀 대상 글자를 새로운 글자로 바꿔서 반환   
   : count를 지정하면 해당 갯수만큼만 시행   
   - .strip([chars])   
   : 특정한 문자를 지정하면, 양쪽을 제거하거나 왼쪽을 제거(lstrip), 오른쪽을 제거(rstrip), 지정하지 않으면 공백을 제거거
   - .split([chars])   
   : 문자열을 특정한 단위로 나누어 리스트로 반환
   - 'separator(! or '')'.join(iterable)   
   : 특정한 문자열로 만들어 반환   
  반복가능한(iterable) 컨테이너의 요소들을 separator(구분자)로 합쳐(join()) 문자열로 반환
   - .capitalize() : 앞글자를 대문자로 만들어 반환
   - .title() : 어포스트로피나 공백 이후를 대문자로 만들어 반환
   - .upper() : 모두 대문자로 만들어 반환
   - .lower() : 모두 소문자로 만들어 반환
   - .swapcase() : 대 <-> 소문자로 변경하여 반환
   - 기타 문자열 관련 검증 메소드 : 참/거짓 반환
     - .isalpha(), .isdecimal(), .isdigit(), .isnumeric(), .isspace(), .isupper(), .istitle(), .islower()

## 리스트(List)
변경 가능하고(mutable), 순서가 있고(ordered), 순회 가능한(iterable)

> list는 아래 세개만 거의씀
> 1. append
> 2. sort 
> 3. pop 


1. 값 추가 및 삭제
   - .append(x) : x리스트에 값 추가 
   - .extend(iterable)   
   : 리스트에 iterable(list, range, tuple, string**[주의]**) 값을 추가  
   ```python
    cafe.append(['coffeenie'])
    # 출력 ['coffeenie']
    cafe.extend(['coffeenie'])
    # 출력 'coffeenie'
    cafe.extend('coffeenie')
    # 글자 하나씩 쪼개져서 출력됨
    ```
   
   - .insert(i, x)   
   : 정해진 위치 i에 값을 추가
     - 마지막 위치는 len함수 이용
   - .remove(x)   
   : 리스트에서 값이 x인 것을 삭제
   - .pop(x)   
   : 정해진 위치 i에 있는 값을 삭제하며, 그 항목을 반환   
   : i가 지정되지 않으면 마지막 항목을 삭제하고 되돌려줌

    ```python
    numbers = [1, 2, 3, 4, 5, 6]
    last = numbers.pop()
    numbers, last
    # 결과값 = ([1, 2, 3, 4, 5], 6)
    ```
  
     - .clear()   
     : 리스트의 모든 항목을 삭제

2. 탐색 및 정렬
   - .index(x) : x값을 찾아 해당 ind값을 반환
   - .count(x) : 원하는 값의 개수를 반환
   - .sort() : 정렬
     - 내장함수 sorted()와는 다르게 원본을 변형시키고 **None**을 리턴함
     - .sorted() : 내장함수로 return값이 있음
   - .reverse() : 반대로 뒤집음(정렬 X)

3. 리스트 복사   
: 새로운 변수를(x) 생성해서 원본 리스트를 저장
   - 얕은 복사(shallow copy)   
   복사본을 수정해도 원본은 수정되지 않음
     - slice 연산자 사용[:] -> b = a[:]
     - .copy() 활용
   - 깊은 복사(deep copy)   
   복사본을 수정하면 원본도 수정됨
     - from copy import deepcopy
     - deepcopy(x)

## List Comprehension
> 코테풀때 꼭 필요한 내용
> 
List Comprehension은 표현식과 제어문을 통해 리스트를 생성합니다.

여러 줄의 코드를 한 줄로 줄일 수 있습니다.

### 활용법

```python
# for문으로 세제곱을 작성하는 법
numbers = range(1, 11)
cubic_list = []

for num in numbers:
    cubic_list.append(num ** 3)
    
print(cubic_list)

# List comprehension을 활용
cubic_list = [num**3 for num in numbers]
cubic_list

# 즉, for를 기준으로 뒤에를 순회하면서 앞에있는걸로 채워나가겠다.
```
---
### List Comprehension + 조건문
조건문에 참인 식으로 리스트를 생성

### 활용법

```python
# for문으로 세제곱을 작성하는 법
even_list = []

for num in range(1, 11):
    if num % 2 == 0:
        even_list.append(num) 

even_list #246810

# List comprehension을 활용
even_list = [num for num in range(1, 11) if num % 2 == 0]
even_list

# 즉, for를 기준으로 뒤에를 순회하면서 앞에있는걸로 채워나가겠다.
```
## 데이터 구조에 적용가능한 Built-in Function
순회 가능한(iterable) 데이터 구조에 적용가능한 Built-in Function

> iterable 타입 - `list`, `dict`, `set`, `str`, `bytes`, `tuple`, `range`

### (1) map(function, iterable)
* 순회가능한 데이터 구조(iterable)의 모든 요소에 function을 적용한 후 그 결과를 돌려준다. 

* return은 `map_object` 형태이다.
#### 활용법
```python
numbers = [1, 2, 3]
list(map(str, numbers))
# ['1', '2', '3']
''.join(map(str, numbers))
# '123'
```
### (2) filter(function, iterable)
* iterable에서 function의 반환된 결과가 `True` 인 것들만 구성하여 반환합니다.

* `filter object` 를 반환합니다.
#### 활용법
```python
# 홀수를 판별하는 함수가 있습니다.
def odd(n):
    return bool(n % 2)

# 홀수인 요소만 뽑기
list(filter(odd, [1, 2, 3, 4, 5, 6, 7]))

# list comprehension 적용_def 함수 필요
[num for num in range(10) if is_odd(num)]

# lamda 식에 저장하는법
list(filter(lambda n: bool(n%2), [1, 2, 3, 4, 5, 6, 7]))
```
### (3) zip(*iterables)
* 복수의 iterable 객체를 모아(`zip()`)줍니다.
* 결과는 튜플의 모음으로 구성된 `zip object` 를 반환합니다.

## ★Lambda 표현식
간단한 함수의 경우, 짧게 줄여 쓸 수 있습니다.
기존의 정의한 함수를 람다표현식으로 바꾸는 방법
1. 맨 앞에 `lambda` 라고 적는다.
2. `def` 와 함수 이름과 소괄호까지 지운다.
3. 엔터와 `return`도 지운다.

람다 표현식으로 바꿀 함수는 아래 조건을 만족해야 합니다.
1. 매개변수가 1개 이상이어야 한다.
2. `return` 구문 포함 한줄이어야 한다.

### 활용법
```python
# 기명 함수
def cube(n):
    return n ** 3

cube(10)

# 익명 함수
(lambda n: n ** 3)(10)

# 기명 리스트
n = [1, 2, 3]
# 익명 리스트
[1, 2, 3]

list(map(cube, n))
list(map(lambda n: n ** 3, [1, 2, 3]))
```
## 세트(set)
변경 가능하고(mutable), 순서가 없고(unordered), 순회 가능한(iterable)

1. 추가 및 삭제
   - .add(elem) : elem을 세트에 추가
   - .update(*ohers) : 여러 값을 추가
   - .remove(elem)   
   : elem을 세트에서 삭제    
   : 없으면 KeyError 발생
   - .discard(elem)    
   : elem을 세트에서 삭제    
   : 없어도 에러가 발생 안함
   - .pop() : 임의의 원소를 제거해 반환
  
## 딕셔너리(Dict)
변경 가능하고(mutable), 순서가 없고(unordered), 순회 가능한(iterable)

 `Key: Value` 페어(pair)의 자료구조

1. 조회
   - .get(key[, default])     
   : key를 통해 value를 가져옴   
   : 절대 KeyError가 발생하기 않음   
   : default는 기본적으로 None 
2. 추가 및 삭제
   - .pop(key[, defalut])    
   : key가 딕셔너리에 있으면 제거하고 그 값을 반환    
   : 그렇지 않으면 default를 반환   
   : default가 없는 상태에서 딕셔너리에 없으면 KeyError가 발생
   - .update()    
   : 값을 제공하는 key, value로 덮어씀

###  `for`를 활용하는 4가지 방법
> ★우리의 입장에선 .key()와 .items()만 사용함.

```python
# 0. dictionary 순회 (key 활용)
for key in dict:
    print(key)
    print(dict[key])


# 1. `.keys()` 활용
for key in dict.keys():
    print(key)
    print(dict[key])
    
    
# 2. `.values()` 활용
# 이 경우 key는 출력할 수 없음
for val in dict.values():
    print(val)

    
# 3. `.items()` 활용
for key, val in dict.items():
    print(key, val)

```
### Dict comprehension

`iterable`에서 `dict`를 생성할 수 있습니다.

```python
{키: 값 for 요소 in iterable}

dict({키: 값 for 요소 in iterable})

# key는 각 숫자, value는 각 숫자를 3제곱하는 값
cubic = {x: x ** 3 for x in range(1, 8)}

# 메서드를 사용한 활용법
{'-' + k : v for k, v in blood_types.items()}
```

### Dict comprehension + 조건
> {키: 값 for 요소 in iterable if 조건식}
```python
dusts = {'서울': 72, '인천': 82, '제주': 29, '동해': 45}
# 예시 1
{k: v for k, v in dusts.items() if v > 80 }
# 예시 2
{k: ('나쁨' if v > 80 else '보통') for k, v in dusts.items() }
```

# OOP
결국 프로그래밍 속에서 현실세계를 반영하고 싶었던 것. 

- 객체(Object)
- 객체지향프로그래밍(Object Oriented Programming)
- 클래스(Class)와 객체(Object)

## 객체(Object)

* 세상에 존재하는 모든것들.즉, 파이썬들을 구성하는것들이 객체들간의 상호작용으로 막 수성되고 결과가 나오고 하니까 무언가가 나옴. 코드를 짜는 행위가 객체지양 행위라 할 수 있음음
  * 하지만 인스턴스라는 말이 나온 이유가 정수, 불리언, 스트링 같은 예시를 들기 위해 나온 것 1이 int의 인스턴스임   
    > 예시) 커피를 사기위해 나라는 객체가 직원이라는 객체가 상호작용해서 커피라는 객체를 받는데 여기서 인스턴스는 종류을 말하는 것으로 문이 문이라는 종류고 나와 직원은 호모사피엔스라는 종으로 예라 할 수 있음

- Python에서 **모든 것은 객체(object)**입니다.

- 모든 객체는 **타입(type), 속성(attribute), 조작법(method)**을 가집니다.

- 객체(Object)의 특징
    1. **타입(type)**: 어떤 연산자(operator)와 조작(method)이 가능한가? 
    2. **속성(attribute)**: 어떤 상태(데이터)를 가지는가?
    3. **조작법(method)**: 어떤 행위(함수)를 할 수 있는가?

### 타입(Type)과 인스턴스(Instance)

| type         | instance                 | 
| -------------| ------------------------ | 
| `int`        | `0`, `1`, `2`            |
| `str`        | `''`, `'hello'`, `'123'` | 
| `list`       | `[]`, `['a', 'b']`       | 
| `dict`       | `{}`, `{'key': 'value'}` | 

* 타입   
공통된 속성(attribute)과 조작법(method)을 가진 객체들의 분류
* 인스턴스(Instance)   
  파이썬에서 모든 것은 객체이고, 모든 객체는 특정 타입의 인스턴스
```python
a = 10
b = 20
# a, b 는 객체
# a, b 는 int 타입(type)의 인스턴스
```
* 메서드(Method)   
  특정 객체에 적용할 수 있는 행위(behavior)
    - <객체>.<메서드>()

## 객체 지향 프로그래밍(Object-Oriented Programming)

* __init_
태어날때 일회성이 아니라 기능을 만들어주는것

.붙은건 속성

우린 지금 태어남에 대해 얘기를 함.
1과 같은 내장자료말고 우리가 만드는 자료를 말함.
__init__과 같은 함수를 활용해서 태어나게 해주고 __del__을 사용해서 죽여버림

dsfsdafasdfasddfadf