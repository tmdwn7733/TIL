# Data Engineering

ta를 처리하는 기술
- 이론 : 전처리(Null, 스케일링) -> 엔지니어링
- 공학 : Bit Data 처리, 로그 처리, 실시간/배치 처리, 스케일링, pipeline. 구축
즉, 데이터엔지니어링은 DA(EDA)와 DS(Modelinf - ML, DL)을 서포트해주는 역할
> 다양한 DB를 다루고 깔고가는 것!

Web은 DE, DA, DS를 다할수 있는 기회의 장을 제공함

## 분산 시스템의 이해
### 컴퓨터의 진화
#### process on machine
- 1930년대 컴퓨터가 최초에 등장했을 때 기계가 사람이 수기로 해야할 일을 자동으로 대신 해줌   
    -> 이후 컴퓨터 장비의 크기가 작아지고, 명령어를 입력하는 방식이 고도화 되는 방식으로 발전이 이뤄짐
- 1940년대 폰노이만 아키텍처와 애니악 컴퓨터가 stored-program이 구현이 가능하는 등 큰 영향을 미침
- 1080년대는 IBM의 x86 아키텍처와 마이크로프로세서가 프로그램을 작성하고 구동하는 방식에 큰 영향을 미침

#### RPC(Remote Produre Call)
원격(Remot) 작업or명령어(Produer) 실행(Call)
- 즉, 컴퓨터 프로그램을 원격에서 호출할 수 있도록 하자는 아이디어
- Ip : 네트워크 주소
- Port : 중복될수 없는 서비스 번호

### AWS(Amazon Web Service)
다양한 대기업이 웹을 이용을 해서 클라우드 컴퓨팅 시스템을 제공(Ms -> Azure, gogle -> Gcp). 하지만 Amazon에서 제공하는 AWS가 제일 유명!
#### 클라우드 서비스
- 클라우드 서비스 등장 전 ->  On Promise 구조(서버실)
- 하지만 이러한 서버실은 대기업이 아니고서는 구비하기가 쉽지않음
- 대기업이 서버실이 필요한 기업에게 사용료를 받고 빌려주기 시작!

#### 집에 있는 나(클라이언트)는 어떻게 할까?
AWS를 사용한다는 전제하에 서울에 있는 나는 도쿄에 있는 AWS를 사용      
- IP와 Port를 사용해 AWS에 접속해야하는데, 이럴경우 해킹을 당하면 요금 폭탄을 당하는 무시무시한 경우가 생김. 그래서 ssh를 사용(이건 예전에 웹페이지 제작할때 돈더줬던 기능)

## 실습01_AWS환경 구축
1. V-lab.pem을 .ssh에 저장
2. [AWS](https://aws.amazon.com/ko/)접속
3. 로그인후 검색창에 EC2입력
4. 내가 받은 Name을 누르고 오른쪽클릭 -> 인스턴스 시작
5. 내가 받은 Name을 누르고 오른쪽 위 연결
6. ssh 클라이언트 클릭후 아래 예시 코드 복사
   `ssh -i "V-lab.pem" ubuntu@ec2-3-114-30-206.ap-northeast-1.compute.amazonaws.com`
   - 여기서 복사하면 root@ 라고 뜨는데, ubuntu로 바꾸기
7. gitbash 터미널에서 cd .ssh로 .ssh파일위치고 이동
8. 복사한 6번코드 붙여놓고 실행
   - 실행하면 ubunt@ip-172-31-11-147로 실행이 바뀜
9.  AWS에 MYSQL설치([노션참고](https://radial-fighter-931.notion.site/AWS-EC2-MySQL-71c3d27607154f7b837086ebf2caf371))
   - Yes/No 질문에서는 웬만하면 Yes
> 설치를 다하면 MY SQL은 도쿄에있는 AWS EC2에 있음    
> 그래서 Client격인 WorkBench를 연결해줌    
>> 이를 위해서는 IP, PORT, PEM파일 이 세가지가 필요함
10. WorkBench 실행 후 새파일 추가
    - Connection Method를 Standard TCP/IP over SSH로 해줌   
11. 인스턴스의 ID 확인해서 10에 집어넣기
    - private: 내부만
      - 인스턴스 안에서만 사용할 정도. 하지만 잘 사용은 안함
    - `public: 외부공개`
      - IPv4나 IPv4 DNS는 거의 똑같음. 
      - 아무거나 사용해도 ㄱㅊ지만 어떤 툴에서는 IP를 사용못하게함   
      -> 그래서 웬만하면 IPv4 DNS(IP 주소의 도메인)를 사용!
12. 다하고 Test Connection 누르고 성공한지 확인후 ok 실행!

# 데이터 베이스
[교재](https://radial-fighter-931.notion.site/01-c9dcd39bf0fe412a80d1f29725cbcfff)
- 프로그램을 이용해 간단하고, 정확하고, 빠르게 이러한 데이터를 입력시킬 수 있음. 이렇게 컴퓨터를 이용해 입력시킨 데이터를 관리할 수 있는 환경이 바로 데이터베이스

## DBMS(Database Management System)
- 데이터베이스를 관리하는 시스템
- 주의할점!
  - 데이터베이스는 보통 용도에 맞게 사용   
  예) 주소록을 위한 데이터베이스를 따로 만들고, 운동 선수의 기록 측정을 위한 데이터베이스를 따로 만든다. 물론 하나의 데이터베이스에 모든 데이터를 저장하는 것도 가능하나, 하나의 데이터베이스에 모든 데이터를 모아내게 되면 관련성 없는 데이터를 한 곳에 모아 놓는 꼴이 되어버리기 때문에 데이터베이스의 규모가 커지게 되면 관리하기가 힘들 수도 있다.
- Application과 Database
  - Application은 workbench!

## 데이터베이스와 테이블
서로간에 관계성이 없게 데이터베이스를 나눠야함
> 하지만, 요즘 유행은 MSA로 카카오톡처럼 각기다른 쇼핑, 채팅의 데이터베이스를 앱안에 한꺼번에 넣음

### 실습 02_데이터베이스 실습
[교재](https://radial-fighter-931.notion.site/02-f1bc182e4dd24f27a1a6a82a54d0a2a5)
- sql 시작할때 명령어: `mysql -u multi(username) -p`
  - 명령어를 실행하면 앞부분이 `mysql>`로 바뀜

## 테이블 구성
- 데이터베이스는 데이터들이 모여있을 하나의 바구니처럼 생각할 수 있음
  - 즉, 데이터베이스는 테이블들의 집합
- 테이블은 데이터의 `형식과 형태(스키마)`를 기술하고 그런 형태를 따르는 데이터 컬렉션(Records)을 담고있음
  - 데이터베이스 안에서 구조화된 형식으로, 관련된 데이터 컬렉션을 담고 있는 것이 테이블!
```
구조화된 형식(Structured Format)이란 데이터 컬렉션이 어떤 식으로 저장되어야 할지가 이미 지정된 데이터 형식을 의미합니다.

MySQL, PostgreSql, Oracle 등이 테이블을 사용하는 대표적인 DBMS입니다.

MongoDB, Redis, Cassandara 등 비구조화된 형식(Unstructured Format)의 데이터를 저장하는 데이터베이스도 존재합니다. 이러한 DBMS에는 구조화된 형식을 저장하기 위한 테이블을 사용하는 것이 아닌, Collection 같은 특별한 형태를 사용합니다.
```
 테이블들은 연관성이 없는 애들이 나올때까지 잘게 쪼개고 나중에 필요할때 합치던가 해야함

## 데이터 입력

### 실습03_데이터 입력
[교재](https://radial-fighter-931.notion.site/04-9de3e745c92b4e608a4283861fddbb63)

### NULL, NOT NULL
DESC cats 명령어를 입력하면 컬럼에 대한 정보가 나오는데, 

``` sql
mysql> DESC cats;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| name  | varchar(50) | YES  |     | NULL    |       |
| age   | int         | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
```
여기서 NULL 의 YES는 => NULL을 허용한다는 의미!
- 이처럼 NULL이 들어오는걸 허용안하고 싶을땐 아래처럼 NO라고 지정해주면 됨!
```sql
mysql> CREATE TABLE cats2(
	name VARCHAR(50) NOT NULL,
	age INT NOT NULL
);

mysql> DESC cats2;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| name  | varchar(50) | NO   |     | NULL    |       |
| age   | int         | NO   |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
```
- 혹은 DEFAULT를 지정해 줘서 아무런 값을 주지않으면 대체단어를 자동으로 부여하는 수식을 써줘도 ㄱㅊ!
```sql
mysql> CREATE TABLE cats3 (
	name VARCHAR(50) DEFAULT "고양이이름",
	age INT DEFAULT 9999
);

mysql> SELECT * FROM cats3;
+-----------------+------+
| name            | age  |
+-----------------+------+
| 고양이이름      |    3 |
+-----------------+------+
```
- 그렇다고 디폴트값을 지정한다고 해서 NULL을 절대 못넣는건 아님. 이때문에 아래조건처럼 강력한 제지를 해 줄 수 있음

```sql
mysql> CREATE TABLE cats4 (
	name VARCHAR(50) NOT NULL DEFAULT "고양이이름",
	age INT NOT NULL DEFAULT 9999
);

mysql> INSERT INTO cats4 VALUES();

mysql> SELECT * FROM cats4;
+-----------------+------+
| name            | age  |
+-----------------+------+
| 고양이이름      | 9999 |
+-----------------+------+
```
> 그렇다고 해서 NOT NULL 과 DEFAULT를 항상 같이 넣는거는 아님! 상황을 보고 작성해야함!

## 기본키
### 실습 04_기본키


## 데이터 유형
INT, TINYINT, BIGINT의 경우 사실 INT를 거의 사용하는데 그래도 내가 넣는 숫자의 범위를 보고 크다싶으면 TINYINT를 사용!

### DECIMAL
실수를 가장 잘 표현함

### FLOAT, DOUBLE
decimal처럼 아주 미세하게 소수점을 처리하기는 어렵지만 대신 용량차지가 적음
- 강사님 개인적인 의견으로 DOUBLE을 사용하는 걸 추천. 하지만 속도가 느려도 상관없고 실수표현을 사용하고 싶으면 DECIMAL을 사용

## 날짜와 시간 데이터 다루기
이 챕터의 경우에는 그냥 외우는 걸 추천

## 집계
데이터 분석이란? 데이터를 확인하는 과정
하지만 데이터가 너무 많음. 그래서 종류별로 데이터를 모아 요약을 해서 종류별로 한개의 데이터가 나옴
- 즉, 집계(集計)란  문자 그대로 데이터를 어떤 기준을 토대로 모아서 계산(요약)힘

### Group By
- 집계자체가 안되기 때문에 표현 할 수 가 없음. 그래서 그룹바이에 없는 컬럼이라서 생각하면 안됨
- 즉, SELECT 절에 그룹이 된 컬럼명, 그룹별 집계된 데이터만 올 수 있음

- 다중구문은 첫번째 그룹이 만들어지고 그 그룹내에서 두번째 조건으로 새로운 그룹이 만들어 지는것

### HAVING
WHERE이 집계전에 범위 조건을 만들어 주는 것이라면
집계의 결과에 대해서 새로운 조건을 제시할때 사용. 그래서 SELECT 다음에 진행되는 것

## Join
개발자들은 cross join을 무조건 피해야함. 왜냐면 모든 경우에 대한 경우를 작성하기 때문 데이터를 보여줘야하는 개발자의 경우에는 cross join을 피하라함
- 그러나, 분석가의 경우는 잘 사용해야함
  - 필요없어보이는 데이터가 나중에는 엄청난 역할을함
> 관례?
>> from절에는 pk를 가지고 있는 테이블을 두기

## Window Functions
윈도우 함수는 그룹 혹은 윈도우 안의 모든 행에 대해 결과를 산출
Group by가 reduction이 생긴따면 윈도우함수는 reduction없이 집계해줌

- PARTITION BY vs GROUP BY
  - 둘다 ~별로 비슷하지만()
  - partition은 부서별 평균을 구하고 모든 행에 넣어라
  - group은 부서별 평균을 구하고 각 그룹별 평균만 보여줘라!


# 실제 데이터를 AWS에 연동해서 WORK BENCH로 구현해보기
> 실제 SQL로 데이터 분석할때 데이터를 모은 사람들(예, 통계청 공무원)이 전문가가 아니라 데이터가 깔끔할 수 없음
>> 즉, 컬럼에 집계의 기준이 들어있는 경우 집계가 불가능!!

- 다른사람의 SQL을 읽을때 방법
  1. FROM절을 먼저 읽기
   - 안에 새로운 쿼리가 있다면 서브쿼리! 
   - 서브쿼리도 FROM부터 읽기



```sql
(SELECT (tmp1.idx) AS LVL1 FROM (SELECT 1 as idx UNION SELECT 2 UNION SELECT 3) tmp1) LVL1,
             (SELECT (tmp2.idx) AS LVL2 FROM (SELECT 1 as idx UNION SELECT 2 UNION SELECT 3 UNION SELECT 4 UNION SELECT 5 UNION SELECT 6 UNION SELECT 7 UNION SELECT 8 UNION SELECT 9 UNION SELECT 10 UNION SELECT 11) tmp2) LVL2
```
- 집계에 대한 기준(~별)을 만드는 테이블
- 즉, 오른쪽으로 쭉 나열된 데이터들을 ~별, ~별로 세로로 표현해 주고 있음(melting 과정!)
- (사진)에서 볼수 있은 것처럼 오른쪽 데이터가 더 분석하기 편함
- 첫번째 코드는 성별 코드 테이블

빅데이터 허들자체가 낮아짐.. Hive(SQL) & Spark(SQL + DF)
특히 요즘은 Spark에서 많이 사용함. EDA도 여기서 다룸

