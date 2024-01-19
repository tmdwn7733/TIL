# 명령어(CLI, MYSQL 모두 사용가능)
실습파일: KDT/SQL
참고교재: 고양이사람
- SQL 고정 명령어는 대문자로, 내가 만든 이름은 소문자
    - 모두 소문자로 적어도 동작은 하나, Rule 을 지키자.
    - 띄어쓰기와 줄 바꿈은 적절히 잘
- DB는 띄어쓰기와 줄바꿈 신경 안끔
- `주석`(coments): '`--`' 
- 반드시 명령어 끝에는 세미 콜론(;) 적기

## CREATE DATABASE
`ctrl + enter` 명령문 실행

`SHOW DATABASES;` 현재 형성되어있는 DB를 보여줌

`CREATE DATABASE 'DB_name';` DB 생성

`DROP DATABASE 'DB_name';` DB 삭제

`USE 'DB_name';` DB에 접속. DB에 속한 테이블에 접근할때 작성해야함. 그러나 이미 접속이 되어있다면(MySQL Workbench의 nevigator에 DB 더블클릭) 따로 더 써줄 필요는 없음

## TABLE
`CREATE TABLE 'table_name' (
    속성 값
);` 테이블 생성

```SQL
CREATE TABLE cats (
    name VARCHAR(50),
    age INT
);
-- cats라는 테이블의 이름에 글자는 50개 까지만 받을꺼고 나이는 정수만 받을꺼야
```
`SHOW TABLES;` 현재 DB안에 존재하는 모든 테이블을 보여줌

`DESC 'table_name';` 테이블의 key, null, type, defalt를 설명

`DROP TABLE 'table_name';` 특정 테이블 삭제


## INSERT DATA
`INSERT INTO 'table_name' (컬럼1, 컬럼2) VALUES (값1, 값2);` 테이블에 데이터 삽입

```SQL
INSERT INTO dogs1 (name, bread, age)
VALUES
	('짱구', '요크셔', 6),
    ('소리','고리', 8);
-- 한번에 여러 데이터(ROW)를 삽입
```

`SELECT * FROM 'table_name';` 테이블 데이터 조회

`ALTER TABLE 'table_name' RENAME COLUMN '기존 컬럼명' TO '바꿀 컬럼 명';` 컬럼 명 변경

## NULL & DEFAULT
- 기존 속성에 아무것도 입력하지 않으면 기본값으로 NULL을 허락함
1. `NOT NULL` NULL을 허락하지 않는 것으로 데이터 입력시 공백 혹은 NULL이 있으면 데이터를 받지 않음
    - DESC TABLE할때 NULL 기본이 NO
    ```SQL
    -- NULL을 허락하지않음. 즉, 필수값
    CREATE TABLE dogs2(
	name VARCHAR(20) NOT NULL,
	age INT NOT NULL
    );
    ```
2. `DEFAULT '값'` NULL 대신 우리가 원하는 임의의 값으로 대신 지정할 수 있음
    - 하지만 해당 필드에 대한 기본값만 설정하는 것이지 필드가 NULL로 남겨질 수 있음
    - DESC TABLE할때 NULL 기본이 YES
    ```SQL
   CREATE TABLE dogs3(
	name VARCHAR(20) DEFAULT 'no name',
    age INT DEFAULT 0
    );
   ```
3. ⚡`NOT NULL DEFAULT '값'` 
   - 대부분의 데이터 베이스는 NOT NULL과 DEFAULT를 함께 사용함
   - NULL이 필드에도 들어오는 것을 방지할 수 있고 NULL값 대신 우리가 임의로 지정한 값으로 대신 나타낼 수도 있음
   - DESC TABLE할때 NULL 기본이 NO

## PRIMARY KEY(PK)
- PRIMARY KEY설정을 넣으면 자동으로 NOT NULL 설정이 들어감
- 그리고 꼭 `AUTO_INCREMENT`를 함께 지정해줘서 인덱스가 자동으로 오름차순으로 올라가 각 데이터가 고유의 값을 가질 수 있도록 해줘야함
```SQL
CREATE TABLE uniq_dogs (
	id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(20) NOT NULL DEFAULT 'no name',
	age INT NOT NULL DEFAULT 0
);
```

## CRUD
1. 테이블을 생성하고 데이터를 입력
2. 원하는 데이터를 조회
   - `SELECT name, breed FROM cats;` 특정 열 조회
   - `SELECT name FROM cats WHERE age=4;` WHERE을 지정해줘서 age가 4살인 고양이의 이름만 조회할 수 있음
   - `SELECT name AS '이름' FROM cats;` 특정 열의 이름을 바꿀 수 있음
3. 데이터 수정 및 삭제
   - `UPDATE cats2 SET age=age+1 WHERE name='Misty';` cats2 테이블에서 이름이 Misty의 나이를 1살 더 올려라
   - `DELETE FROM cats2 WHERE name='Egg';` 이름이 Egg인 데이터 삭제
   - (주의!) WHERE를 적지않으면 전체 수정 혹은 삭제가 될수 있음
     - `UPDATE dogs4 SET age=100;` dogs4 데이터에서 age 전부 100으로 수정
     - `SELECT * FROM cats2;` cats2 데이터 전체 삭제

## CONCAT & REPLACE & CHAR_LENGTH
1. `CONCAT` 문자열을 연결
   - `SELECT CONCAT(title, '!!!') FROM books;` title뒤에 문자열을 붙여줌
   - 한번에 요약해서 스트링으로도 만들 수 있음
    ```SQL
    SELECT CONCAT_WS('-', title, author_fname, author_lname) AS summary FROM books;
    ```
2. `REPLACE` 원하는 문자를 임의의 문자로 대체함
   - `SELECT REPLACE('Hello World', 'Hell', '****');` 첫번째 값안에서 두번째 값의 데이터를 세번째 값으로 대체함

3. `CHAR_LENGTH` 글자수 COUNT
   - CHAR도 있으나 다양한 언어를 표현할때는 CHAR_LENGTH가 잘 세어줘 그냥 처음부터 CHAR_LENGTH를 쓰는것이 편함

## DISTINCT & ORDER BY
1. `DISTINCT` 중복되지 않은값을 보여줌
   - `SELECT DISTINCT(author_lname) FROM books;`
   - 두개 이상의 값의 조합이 중복되지 않은 값도 보여줌
     - `SELECT DISTINCT author_lname, author_fname FROM books;`

2. `ORDER BY` 정렬 기준
   - 기본이 오름차순(ASC)
   - 내림차순은(DESC)
   ```SQL
   -- 재고 적은순
    SELECT * FROM books ORDER BY stock_quantity ASC;
    -- 재고 많은순
    SELECT * FROM books ORDER BY stock_quantity DESC;
   ```
   - 여러 컬럼 동시 진행도 가능
    ```SQL
    -- 이름이 같아보이지만 막상 ID를 보면 ID 순으로 정렬. 사실 별 티가 안남
    SELECT author_lname, released_year, title FROM books 
    ORDER BY author_lname;

    -- author_lname기준으로 정렬 만약 이름이 같으면 같은 이름안에서 released_year순으로 정렬
    SELECT author_lname, released_year, title FROM books
    ORDER BY author_lname, released_year;
    ```
    - 함수로 만든 가상의 컬럼도 정렬 가능
    ```SQL
    -- 즉, 풀네임의 오름차순으로 보여줌. 이것도 물론 같은 이름이면 ID가 먼저인 애가 앞에온다
    SELECT CONCAT(author_fname, ' ', author_lname) AS fullname FROM books
    ORDER BY fULLNAME;
    ```

## LIMIT & LIKE
1. `LIMIT` 결과의 갯수를 제한
   - 데이터가 너무 많을경우 로드하는데만 시간이 많이 소요될 수 있음. 이에, 어떻게 데이터가 나오는지 확인하기 위해 앞의 특정 갯수만 가져 올 수 있음
   - `SELECT * FROM books LIMIT 5;` 5개만 가져오기
   - 앞의 내용을 제외하고 뒤의 내용으 가져올 수 도 있음
    ```SQL
    -- 앞에 열개 빼고 뒤에 다섯개
    SELECT * FROM books LIMIT 10, 5;
    -- 물론 뒤에 100이라 적는다해도 100을 가져온다는게 아니라 남은 데이터만 가져옴
    SELECT * FROM books LIMIT 10, 100;
    ```

2. `LIKE` 특정 문자가 들어간 단어를 검색
   - **%** : 이 자리에는 0개부터 N개까지 들어올 수 있음
   - **_** : 이 자리에는 오직 한 글자만 올 수 있음. 즉, 빈칸뚫기로 __는 두글자임
   - 하지만 만약에 `%` 특수기호가 들어간 책을 찾으면?
     - `\`를 활용
     - `SELECT * FROM books WHERE title LIKE '%\%%'; ` %가 들어간 책제목 검색