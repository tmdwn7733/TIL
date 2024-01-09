# django
프레임워크는 프랜차이즈처럼느낌 내가 쓰기는 편하지만 제약이 있음
라이브러리는 원하는 것만 꺼내옰수 있어 자유도는 높지만 프레임워크처럼 쉽지는 않음

준비물
1. gitbash 설치
   - pip install django : django를 사요하기 위해 필요한것
   - pip install django_extensions : Django 프로젝트에 대한 확장 모듈 모음
     - 대신 settings에 꼭 'django_extension'를 넣어줘야함
2. vs코드 extensions 설치: 
   - Django(Baptiste Darthenay) 
   - SQLite Viewer(Florian Klampfe)

- 앱을 만들면 바로바로 해야할 일
  1. touch urls.py : 앱안에 urls 파일만들기
  2. mkdir -p templates/form : 앱안에 templates 폴더와 그안에 form이라는 폴더 하나 더 만들기(-p가 parent로 templates라는 파일이 없어도 같이 만들수 잇음)
  3. cd templates/form으로 이동해 필요한 .html 문서 만들기

## 기본 문법(project : 00_INTRO)
1. 새로운 프로젝트 시작시 `django-admin startproject <project_name>` git에 작성
   - intro는 총무(master app)고 manage는 집사
   - 이름이 마음이 안들어도 자동으로 설치된 파일명은 변경 불가능
   - 하지만, 밖에 뜨는 프로젝트명은 변경 가능
2. 마스터 폴더의 settings 내용
   - installed_apps를 제일 많이 사용
   - middleware : 요청이 들어왔을때 정수기 필터 역할을 함
   - templates : html문서를 다루는 내용. django가 html문서를 읽을때 항상 templates를 먼저 살펴봄
   - wsgi_application : wsgi파일안에 application관련내용
   - root_urlcof : 최상단 url 설정 -> urls 파일
   - auth_password_validators = 비밀번호 설정할때 유효한 애들(1234와 같은 비번 못쓰도록)만 쓸수 있도록 설정
   - time_zone : 시간 기준 설정
   - usf_I18n : 국제화
   - LANGUAGE_CODE : 원하는 언어설정(ko-kr)
3. 프로젝트 영업개시전 프로젝트 폴더(00_INTRO)안에 들어와서 `python manage.py` 스크립트 뭐가 있는지 보기
4. staticfiles안에있는 runserver사용 `python manage.py runserver` 실행후 하단에 나온 서버링크 클릭   
[참고]서버를 설치할때 너무 최신은 오히려 독일수 있음. django는 .2버전이 안정적임([로드맵](https://www.djangoproject.com/download/))


## 고정된 url로 app과 master 연동하기(project : 00_INTRO)
app을 master에 포워딩하는 방식   
실습파일 : home, utils, recap

> 연동 순서 
>> master urls <-> app urls <-> app views <-> templates의 html
1. 새로운 앱(app) 시작 : `python manage.py startapp <app_name : home>`
2. intro.settings에 installed_apps에 `home` 등록(출생신고)
3. App(home) 폴더안에 url.py 파일 만들기
4. master url 작업
   - `from django.urls import path, include` 가 필요
   - path('home/', include('home.urls')) : home의 url에 연동하기
5. App url 작업
   - `from django.urls import path, include` 필요
   - `from . import views` : 현재 home.urls의 파일이 들어간 폴더내에 views파일을 불러오는 것
   - urlpattersn = [] 는 필수
     - [] 안에 home에서 연동해서 나갈 경로를 새로 지정해주기
   - views 뒤에 views안에 있는 함수와 연동하기 위해 views.함수명 작성해주기
6. App views 작업
   - `from django.http import HttpResponse` : views 파일에서 바로 보여줄 경우 사용
   - `from django.shortcuts import render` : html의 파일을 불러오기 위해 필수
   - html을 불럭오기 위해서 app 폴더 내에 templates의 폴더를 만들고 여기에 html 파일을 만들기
     - 주의! html의 명이 중복되면 다른 app의 하위 templates에 있는 html을 가져옴    
      -> 왜냐면 master.settings 안에 installed_apps에 app이 등록된 순서대로 먼저 확인함   
      -> 이를 해결하려면 templates안에 새로운 폴더를 생성하고 html 파일을 옮겨줌. 그리고 views에 새로 생성한 `폴더명/파일명.html`로 경로를 설정해주면 됨   
      -> 폴더명은 App명과 통일해 주는게 좋음
   - 새로운 함수 계산이 필요한 경우에 필요 라이브러리는 views 파일에 작성하기
   - 함수를 작성한 경우 render뒤에 딕셔너리로 작성해서 계산 값 넣기
     - render 함수의 3번째 인자가 context 라는 이름으로 정의되어 있는데, context는 반드시 dict 만 들어올 수 있도록 만들어져 있기  때문 
     - render 함수 자체의 특성이라 어쩔수가 없음 
7. .html 작업
   - 최종 화면에 보여줄 모습을 .html로 작성해서 보여줌
   - `django Template Language(DTL)` : 원래 {{}}는 html에서는 아무런 효과가 없지만 django에서는 특수문법으로 적용됨
     - {{  }} => print(출력)
     - {%  %} => 논리 : if 문 혹은 for문등 논리력으로 작성 


## 고정된 url이 아닌 사용자가 url에 남기는 데이터로 브라우저 조회(project : 01_USER_INPUT)
> url/한승주/ 처럼 사용자가 url 한승주라는 값을 넣었을때 그 값을 활용하는 방식    

실습폴더 : var_routing

1. 마스터 폴더안에 templates 폴더 생성
2. templates 폴더 안에 base.html 파일 생성
3. html의 중복된 head값을 base.html에 만들어서 `{% block content %}{% endblock content %}`를 body 안에 기입
4. 마스터의 settomgs.py에서 TEMPLATES의 DIRS를 `[BASE_DIR/'templates']`로 지정 
   - 그래야 App안에 말고 Master 안에 있는 templates 파일도 조회함
5. APP안에 Templates의 html파일에서 아래처럼 확장자를 연결하고 내용 집어넣기
   - `{% extends "base.html" %}` : base.html을 가져와서 쓸거야라는 의미 
  
    ```html
    {% extends "base.html" %}

    {% block content %}

    내용 집어넣기

    {% endblock content %}
    ```

## html간 자료를 주고 받기(project : 01_USER_INPUT)
실습파일: form, utils
> 두개의 html 파일을 활용!   
> 한 브라우저에 사용자가 값을 입력하면 자동으로 다른 브라우저로 연동되어 사용자가 입력한 데이터의 값을 사용해서 보여주는 방식
   <p align="center">
   <img src="../이미지/django01.png">
   </p>

1. 새로운 앱 생성뒤 master settings에 등록
2. 앱안에 urls.py 생성
3. 생성된 앱에 templates폴더를 만들고 앱이름과 같은 폴더 하나더 생성 
4. 앱 이름과 같은 폴더내에 input.html output.html 문서 만들기
5. master urls 작업 
6. app urls 작업    
-> 여기까진 기존방식과 동일
---
7. views & html 작업 
   - input.html에 사용된 id의 name ->  views.py에서 request.get에 저장
   - views.py에서 값으로 사용된 자료 key ->  ouput.html에 사용해 브라우저에 표시
   - id : 브라우저안에서만 사용html과 css에서만 사용
   - name : 서버에서 사용
   > id가 title이면 for의 라벨이 title이 되는것이고 name의 title이 views에서 쓸 key값
<p align="center">
<img src="../이미지/django02.png">
</p>

### 기타 
- `input.html`에서 `type` 설정을 잘해야함.
  - text냐 number에 따라서 사용자가 문자열만 혹은 숫자만 입력하게 할 수 있음
- `view.py`에 output을 담당하는 함수(def)를 조작하면 input에서 제공한 값을 다양하게 활용할 수 있음
- inpurt에서 내용을 보내면 output에서 request에 내용이 저장됨
- `<form action="/form/pong/" method="">` 여기서 아무말도 쓰지 않으면 기본값 get으로 method가 지정
- `placeholder="안내메세지"` : 입력창안에 안내메세지를 넣을 수 있음
- `required` : 사용자가 공란으로 제출 못하게 막을수 있음(필수사항)
> 주의! : 사용자가 입력한 값은 무조건 문자열로 받음. 그러니 views에서 받은 값의 형변환이 필요함

### 보안
1. method="GET" : 별거 아님. 대충해되 됨. 보안걱정 없음. 별 위험이 없다고 django는 믿고있음   
  vs
2. method="POST" : GET보다는 별거 있고 서버가 바뀔수 있음. 보안 걱정 있음으로 위험이 있다고 django는 믿고 있음
   - 경찰서에 급하게 들어가면 경찰이 자연스럽게 신분증을 요청하는 것처럼 의례 형식? 같음
   - 보안절차(CSRF)
   - input.html의 method를 POST로 바꾸면 views.py에 request.post에 데이터가 저장됨
   - `{% csrf_token %}`을 input.html에 꼭 설정해줘야함

## 데이터베이스 저장(02_MODEL)
실습파일 : hospital
우리가 데이터베이스를 쓰기 시작한 후부터 두가지 세상이 있음.
- python - Django 세계 : python only
- DB(RDBMS) 세계 : sql only
  - ORM(Object-Relational Mapping) : o(객체_파이썬), R(관계지향_sql)   
   번역기 같은 것으로 파이썬으로 작성한 언어가 SQL로 번역됨. 덕분에 장고를 쓸때 SQL언어를 하나도 안쓰고 사용할수 있음
  - 우선 SQLite3로 sql 경량화버전을 사요하지만 나중에 더 높은 수준의 프로그램으로 갈아 끼울수 있음
  
   <p align="center">
   <img src="../이미지/django03.png">
   </p>

1. 테이블에 대응하는 모델 클래스 생성 작업
   - 새로 생성된 앱의 models.py에 테이블을 그릴 클래스를 생성
2. 컬럼에 대응하는 필드 클래스 변수 설정 작업
   - models.Model클래스는 많은 정보를 가지고 있음
   - charfield의 경우 길이 정보를 확실하게 기입해야함
> 한줄요약 : model.py은 테이블을 정리하기 위해 쓰는것
1. 해당 프로젝트를 runserver하면 db.sqlite가 생성됨
   - db.sqlite가 우리가 만든 테이블이 sql형식으로 세팅되어서 나올 곳
2. python manage.py makemigrations `<app_name>`
   - 테이블을 넘기기 위해서 스캐치를 먼저보기 위한 작업
   - 앱안에 migrations이 생성됨
   - 아직 테이블이아니라서 0001_initial.py로 스캐치를 확인할수 있음
     - id :  환자들을 구분할수 있는 확실한 키를 django가 자동으로 만들어줌
3. python manage.py migrate `<app_name>`
   - 스캐치를 보니 마음에 들어서 이제 테이블로 최종 생성
4. pip install django_extensions 설치후 settings에 'django_extension'를 넣어줌
5. 모든 장소에서 하는 일들은 터미널 즉, manage.py를 통해서 실행됨
   - 파이썬은 직접 실행, 간접실행이 있으며 직접실행의 경우 python manage.py shell_plus를 입력해 터미널에서 직접입력해야만 실행할 수 있음. 
   - 즉, `if __name__ == '__main__':`밑에 적는애들은 runserver로 작동해도 전혀 인지하지 않음

### CRUD( C => R => U => D )
개발자들에게 가장 중요한 개념 네 가지   
유저들의 입력 정보(예를 들면, 로그인 정보, 클릭 정보 등)를 데이터베이스에 추가해서 ‘이 유저는 여성복을 좋아하는구나’처럼 요청한 데이터를 내놓는 것이 Create 개념

1. **Create**(생성)
   - 개발자들이 데이터를 직접 작성하지는 않음. 유저들이 다양한 정보 넣어주는 것
   1. 가장 일반적인 방법    
   각 column값 직접 설정해 행을 채우기
      ```pyhon
      p1 = Patient()
      p1.name = '한한한'
      p1.age = 20
      p1.weight = 67.3
      p1.height = 175.2
      p1.mbti = 'ESFP'
      P1.save()
      ```
   2. 채워서 저장(2STEP)   
   p2 = Patient(name='한환자', age=23, weight=52.3, height=162.0, mbti='ESTP')   
   p2.save()
   3. 한번에 채워서 저장(3STEP)   
   p3 = Patient.objects.create(name='한환자', age=23, weight=52.3, height=162.0, mbti='ESTP')
   - 주의! 1과 3은 꼭 .save()를 해야만 테이블에 저장됨

2. **Read**(조회)
   - CRUD에서 개발자들이 사실상 95%는 조회에 힘을씀
   1. 전체 조회 : Patient.objects.all()
   2. 단일 조회 : p4 = Patient.objects.get(name='연습')
      - 이름/나이 조회 등 다양하게 조회가능 : p4.name, p4.age
   3. 조건 조회 : django의 특수문법
      - 나이가 25 이상인 사람들 : Patient.objects.filter(age__gte=25)
      - 키가 170보다 작은 사람들 : Patient.objects.filter(height__lt=170)
   > 사실 가장 확실하게 데이터를 조회할 수 있는건 **id**로 조회하는것
   > 그러나 파이썬에는 id라는 함수가 있으니 그냥 **pk**라는 말을 사용
   > (예시) p4 = Patient.objects.get(pk=4)

3. **Update**(수정)
   - 한명을 고르고 수정하고 저장하면 끝
   ```python
   p1 = Patient.objects.get(pk=1)
   p1.age =40
   p1.weight += 10
   p1.save()
   ```

4. **Delete**(삭제)
   - 한명을 고르고 삭제하면 끝
   - save 필요없고 되돌릴수도 없음 신중하게 해야함
   - 한번 배정된 id는 삭제되면 두번 다신 못씀. 건너띄고 새로 배정됨
   ```python
   p2 = Patient.objects.get(pk=2)
   p2.delete()
   ```

