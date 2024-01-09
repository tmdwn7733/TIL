## 명령어(CLI, MYSQL 모두 사용가능)
- SQL 고정 명령어는 대문자로, 내가 만든 이름은 소문자
    - 모두 소문자로 적어도 동작은 하나, Rule 을 지키자.
    - 띄어쓰기와 줄 바꿈은 적절히 잘
- DB는 띄어쓰기와 줄바꿈 신경 안끔
- `주석`(coments)dms '`--`' mplus ! 파이썬 # 역할.
- 반드시 명령어 끝에는 세미 콜론(;) 적기

`ctrl + enter` 명령문 실행

`SHOW DATABASES;` 현재 세계관을 보여달라

`CREATE DATABASE test;` DB 생성

`DROP DATABASE test;` DB 삭제

`USE pet_shop;` 펫샵에 접속한다의 정도

```SQL
CREATE TABLE cats (
    name VARCHAR(50),
    age INT
);
-- cats라는 테이블의 이름에 글자는 50개 까지만 받을꺼고 나이는 정수만 받을꺼야
```
`SHOW TABLES;` 현제 DB안에 존재하는 모든 테이블을 보여달라

`DESC cats;` 특정 테이블 설명

`DROP TABLE cats;` 특정 테이블 삭제

```SQL
INSERT INTO dogs1 (name, bread, age)
VALUES
	('짱구', '요크셔', 6),
    ('소리','고리', 8);
-- 한번에 여러 데이터(ROW)를 삽입
```

`SELECT * FROM dogs1;` 테이블 데이터 조회

`ALTER TABLE dogs1 RENAME COLUMN bread TO breed;` 컬럼 명 변경