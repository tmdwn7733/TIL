# Web
준비물: vs코드에서 open in browser(TechER) 설치하기
공부하기 좋은 자료: [poiemaweb](https://poiemaweb.com/html5-syntax), [codecademy](https://www.codecademy.com/courses/learn-html/lessons/html-document-standards/exercises/indentation-html)

- UI   
사용자와 사용되는 무언가의 상호작용   
우리(사용자)가 컴퓨터 코드작성을 위해 소프트웨어의 VSCODE, 혹은 하드웨어의 키/마/모(사용되는 것)의 상호작용

- Client(요청)    
  - 컴퓨터: 내가 쓰고 있는 컴퓨터
  - SW: 크롬, 사파리, edge, opera 등과 같은 브라우저

- Server(응답)
  - 컴퓨터: 우리가 볼일이 거의 없는 데이터 센터같은 것
  - SW: 요청이 단계별 소프트웨어를 거치고 핵심로직을 담당하는 소프트웨어에서 처리됨
    - django(python)    
    핵심 소프트웨어를 만들고 관리하는것을 도와주는 것     
    파이썬에서 django말고 Flask, FastAPI도 있지만 django를 가장 많이 사용함     
    기타로 Spring(Java), Node(Express, Koa)(JavaScript), laravel(DHP), Ruby on Rails(Ruby)


> 즉 웹서비스는 정보공간(web)에서 일어나는 클라이언트의 요청와 서버의 응답을 제공하는 서비스

## HTML(Hyper Text Markup Language)
자리와 구조를 정해주는 것
> 웹 페이지를 작성하기 위한 역할 표시 언어

1. Hyper Text  
하이퍼는 초월하다 할때의 초로 호들갑 떠는 단어   
   - 기존의 텍스트   
   우리가 원하는 정보를 찾으려면 목차랑 페이지가 없든 있든 첫페이지부터 순차적으로 넘어가면서 찾아야함.    
   한마디로 선형적인 정보탐색을 할수밖에 없음
   - 하이퍼텍스트   
   우리가 원하는 정보를 언제 어디에서든 볼수 있도록 함
   **하이퍼링크**를 타고 링크를 타고 정보를 확인함

하지만 사람들이 자기 멋대로 만들수 있기에, 약속을 서로 했고 이게 바로 HTTP(S)라 할 수 있음

2. Markup(표시)
markup과 markdown은 사실 같으 일은 하는 것이만, 하이퍼텍스트의 마크업이 개발된지 오래되어 마크다운이 나중에 나올때 우리 쉽게 쓸수 있도록 간략하게 정리하자로 개발된것

마크업은 제목을 제목이라고 표시함.

3. Language(언어)   
   약속

### 구조
1. HTML은 elements로 구성됨
2. elements는 opening tag, content, closing tag로 이뤄짐
3. 태그내에 다른 태그를 배치하는 계층 구조로 이뤄지며, 요소가 다른 요소 내에 포함되어 있으면 해당 요소의 하위요소로 간주됨
4. 속성을 사용하여 element의 태그를 확장시킬 수 있음. 
   - 속성은 opening tag에 추가되는 콘텐츠
   - 정보제공, 스타일 변경까지 다양한 방법으로 사용됨
5. 요소 자체만으로는 어떠한 의미를 가지고 있지 않지만 전역 속성을 사용해 스타일링을 위해 요소들을 그룹화하고나 속성값을 공유하는데 유용하게 사용되는 요소들도 있음
   - `<div>`와 `<span>`은 매우 ㅂ슷하지만, `<div>`는 블록 타입, `<span>`은 인라인 타입
6. 이미지와 비디오도 불러올 수 있음. 이미지가 opening tag만 사용한다면 비디오는 이미지와 달리 closing tag도 필요함
7. 새로운 html 파일은 항상 `<!DOCTYPE html>`으로 시작하고 `<head>`인 메타데이터(웹에 직접 표시되지 않는 페이지에 대한 정보)와 `<body>`(우리가 쓰는 문서의 내용으로 body 내의 콘텐츠만 화면에 표시될 수 있음)로 이뤄짐
8. `<a href=""></a>`를 활용하여 외부링크 뿐만아니라 내부에서 작성한 html 문서끼리 연계도 가능함
9. `<a><img></a>`를 활용하여 이미지 클릭시 새로운 창으로 넘어가는 요소도 삽입가능
10. 페이지 양이 많은 경우 동일한 페이지 대상에 id를 부여하여 링크를 클릭하면 자동으로 스크롤 될수 있게 지정할 수 있음

### 문법
1. html은 소문자 대문자 상관없음
2. 들여쓰기도 있든 없든 상관없음
3. ctrl + entre: 해드 밑에 바로 글을 쓸 수 있음
4. html에서 작성할때 반듯이 쌍따옴표("") 작성
5. alt + B : 우리가 작성한 html의 문서를 브라우저로 열수 있음
6. 수정을 하고난뒤 저장뒤 브라우저를 새로고침누르면 수정됨
7. 엔터를 쳐도스페이스바 한개로만 적용됨
8. ctrl + / : 주석
9. ! + tab : 자동으로 서식을 만들어줌
10. p + tab: 빈 문단을 하나 넣음
11. li*n : 곱하기 연산자를 활용해서 한번에 여러개를 만들 수 있음


* 실습파일: 00_intro.html
  - `<!doctype html>` : 지금부터 html을 시작하겠다라는 의미
  - `<a>, </a>`: 오프닝, 클로징. 클로징은 오프닝을 만들면 자동으로 생성되며 모든 글은 오프닝과 클로징 사이에 있어야함
  - `<head>` : 메타데이터(데이터에 대한 정보를 제공하는 데이터)를 기입
  - `<meta charset="utf-8">` : 가장 많이 쓰이는 문자열을 숫자열로 치환
  - `<title>00 intro to html</title>` : 문서에 대한 제목을 입력_탭 제목
  - `<body>` : 우리가 쓰는 문서의 내용으로 body 내의 콘텐츠만 화면에 표시될 수 있음
  
* 실습파일: 01_heading
  - `<html lang="en">` : 영어로 작성한 html
  - `<meta name="viewport" content="width=device-width, initial-scale=1.0">` : 화면에서 보일때 가로길이는 모니터의 가로고 초반확대비율을 1.0으로 하겠다.
  - h1(1~6) + tab : Heading으로 총 6단계의 수준으로 제목을 기입할 수 있음

* 실습파일: 02_content
  - `<lorem>` : 문단 안에 의미없는 글을 넣어 시각적인 자룔르 보여줌
  - `<br>` : 각 문장 사이 줄 바꿈
    - 시조나 주소를 쓸때처럼 정말 필요한 부분에만 쓰임
  - Semantic (의미를 갖는)
    - 검색엔진에서도 이 애들을 더 중요하게 봄
    - `<strong>강조1</strong>` : 강조해주세요 하니 굵어진 것
    - `<em>강조2</em>` : 강조해주세요 하니 기울어진 것
  - Non Semantic (의미가 없는)
    - 겉보기에만 지시, stiling. 문서에서 어떤 역할도 없고 그냥 굵고 기울어진게 다. 즉, CSS를 사용해서 굵게 만들거나 STRONG을 사용해서 강조
    - `<b>굵게</b>` : **굵게** -> 겉보기에만 굵어져라
    - `<i>이텔릭</i>` : *이텔릭* -> 겉보기에만 기울어져라
  - `<pre></pre>` : 있는 그대로 모습 보여줌

* 실습파일 : 03_link
  - a + tab : `<a href=""></a>` 생성
    1. 기본링크 생성
       - 구글로 가려면 <a href="https://google.com">GOOGLE</a>을 클릭하세요
    2. 새탭에서 열기
       - <a href="https://naver.com"target="_blank">Naver</a>
    3. 비어있는 링크 열기
       - <a href="#">목적지 미정</a>이지만 우선 링크 생성

* 실습파일 : 04_link
    1. 순서 있는 리스트
       - `<ol></ol>` : 순서있는 칸 만들기
       - `<li></li>` : 번호 있는 리스트 생성
       - ol과 li 섞어서 같이 쓸수도 있음
    2. 순서 없는 리스트
       - `<ul></ul>` : 순서없는 칸 만들기
       - `<li></li>` : 번호대신 서식 표시가 나타남
  
* 실습파일 : 05_table
  - `<thead> -> <tr> -> <th>` : 열 이름 지정
  - `<tbody> -> <tr> -> <td>` : 행 값
  - `<style></style>` : 구조를 정했으면 꾸밀수 있음
    - border: 테두리선
    - width: 가로 폭
    - border: 행의 테두리 선 지정
    - padding:  내부 콘텐츠와 테두리(border) 사이의 여백을 지정
    - text-align: 텍스트 정렬
    - border-collapse: 테이블의 테두리 병합

* 실습파일 : 06_media
  1. img + tab : 이미지 불러오기
    - src="" : 이미지 주소 가져오기
    - alt="" : 시각장애인이 웹에 접근하기 편하게 그림에 대한 설명을 넣어줌. 그럼 시각장애인이 그림을 못봐도 그림 설명을 들어서 문맥을 이해할 수 있음. 혹은 그림이 사라져도 그림에 대한 설명이 남아 있어서 이해할수 있음. 또한 alt 속성은 SEO(검색 엔진 최적화)에서도 중요한 역할을 함
    - `<img src="" alt="">`
  2. 비디오 불러오기
    - iframe으로 가져오는 경우가 정말많음
    - 유투브 -> 공유 -> 퍼가기 -> ifame 복사 

* 실습파일 : 07_form
- form + tab : 양식만들기
  - `<form action="" method=""></form>`
  - ""안에 나중에 데이터를 보낼 목적지 URL을 적기
  - method에서 post 할지 get 할지 확인해야함
- `<div></div>` : 블록 수준(block-level)의 컨테이너 요소로, 페이지를 여러 섹션으로 나눔
  - html의 요소를 그룹화하는데 유용해 동일한 스타일을 적용할 수 있음
- `<label for=""></label>` : 해당 이름 넣기
- `<input type="text">` : 해당 값 양식 설정하기
  - 값 양식 예시
    - text : 모든 문자, 숫자 입력가능
    - password : 숫자를 가림
    - number : 숫자만 입력하게 함
    - email : @ 입력 필수
    - `<textarea name="" id="" cols="30" role="10"></textarea>` : 단답말고 길게 적을때 사용
    - submit : 제출 버튼으로 표시
- input에게 id를 부여하고 부여한 id를 label for=""의 ""에 넣으면 레이블과 폼 요소가 서로 연결되어 있음

## CSS
구조화된 html을 스타일링 해주는 것
원래는 같은 html의 내에서 정보와 스타일링이 같이 있었으나 오히려 정보 접근에 혼란을 줄수 있어 분업을 시작함

### 구조

* 실습파일: 00_intro.html & style.css
  1. 문장 하나하나 style 지정(inline)
     - 하지만 문장이 100개면 다 해야한다는 단점이 있어서 앞으로 쓸일이 없음
  2. head안에 style 지정
     - 얘도 class를 지정해주는 번거로움이 있지만 style을 바꿀때 한번에 바꿀수 있다는 장점이 있음
     - class를 사용하여 문단 안에 몇몇 부분만 설정할수도 있음 
     - id도 쓸수 있는데 거의 class를 사용함
  3. 별도의 css파일로 분리
     - 파일이 커지고 style도 많아지면 파일을 따로분리해서 적용시킴
     - link + tab 사용 필수: `<link rel="stylesheet" href="">`

* 실습파일: 01_selector.html
  - 원하는 style별 class를 지정하여 body에 class를 기입해주면 다양한 style을 지정할 수 있음
  - body의 각 p에 각 style의 class를 순서대로 넣을 필요는 X

* 실습파일: 02_units.html
  1. 크기단위
     - `px`는 절대값
       - 예전에는 브라우저의 크기가 거의 통일되어 있어서 상관없었으나 요즘은 좀 달라졌음. 이에 16px이 젤 무난하다는 결과가 있어 브라우저 기본값으로 설정됨
     - `em과 %`는 상대값
       - 브라우저의 기본값 대비 모바일 기기 혹은 웹페이지로볼 때 요소들이 자동으로 조정됨
     - `rem` : 루트 em으로 폰트크기를 기준으로 브라우저의 기본값 상대적인 크기를 키우고 싶을때 자주사용함
       - 내 컴퓨터의 200% 키워야지 = 2rem
     - `viewport` : 화면의 크기를 기준으로 화면을 조절하는 것으로 반응형 웹디자인에서 사용함. 즉, 아 내 컴퓨터의 절반만 쓰고 싶다 싶으면 50vw
     - `margin` : 여백지정
     - `vh` : 현재 뷰의 높이를 기준으로 요소 크기 설정
     - `vw` :  현재 뷰의 너비를 기준으로 요소 크기 설정
     - `text-align` : 텍스트 정렬
       - 참고로 **block 안에서 정렬이 가능**하지만 iline 영역에서는 중앙정렬해도 선의 영역에서만 나타나 우리가 보기에는 의미가 없음. 즉 block 단위에서 텍스트 정렬을 지정해야함    
      <p align="center">
      <img src="../이미지/web1.png">
      </p>

  2. 다양한 컬러 및 투명도 : [color](https://poiemaweb.com/css3-units) 참고

* 실습파일: 03_boxmodel.html
  - HTML 요소는 Box 형태의 콘텐트(Content), 패딩(Padding), 테두리(Border), 마진(Margin)로 구성됨
  - 하나의 값을 주면 동서남북으로 들어감
  - 물론, 쪼개서도 넣을수 있음
      - top, right, bottom, left 개별 지정
      - margin(시계방향)적용 
      - margin n * n : 상하, 좌우 값 다르게 지정
  1. 콘텐트(Content) : 책
  2. 패딩(Padding) : 책상 테두리
      - 책이 책상에 딱 맞을수도 있기에 별도의 패딩값을 지정하지는 않으나, 책상의 크기를 키우고 싶으면 패딩의 값을 크게 주면됨 
  3. 테두리(Border) : 책상의 경계선
  4. 마진(Margin) : 책상 밖의 영역(aka 결계?로 뚫고 들어올 수 없음)
  - 박스를 오른쪽으로 이동시키려면 magin left 값을 더 주고 밑으로 이동시키려면 margin top값을 더줘야함

* 실습파일: 04_display.html
  - css는 결국 면(blocl)과 선(inline)으로 이뤄짐
  1. bolck 레벨 요소
     - 항상 새로운 라인에서 시작함. 왜냐면 화면 크기 전체의 가로폭을 차지(width: 100%)
     - 계층구조일 경우 자식요소는 부모요소의 공간을 모두 사용   
      (요소 예) div, h1 ~ h6, p, ol, ul, li, hr, table, form
  2. iline 레벨 요소
     - 새로운 줄을 시작하지 않아도 사용가능(abcd가 새로울줄에서 시작할 일이 없음)
     - width, height, margin-top margin-bottom 프로퍼티를 지정 X 
     - inline 레벨 요소 뒤에 공백(엔터, 스페이스 등)이 있는 경우, 정의하지 않은 space(4px)가 자동 지정
     - inline 레벨 요소 내에 block 레벨 요소를 포함할 수 없음. 선안에 면 못넣는 다고 생각하셈    
     (요소 예) span, a, strong, img, br, input, select, textarea, button + 별말없이 작성한 글
  1. iline-block 레벨 요소
     - block과 inline 레벨 요소의 특징을 모두 가짐
     - inline 레벨 요소와 같이 한 줄에 표현되면서 width, height, margin 프로퍼티를 모두 지정
  2. flex 레벨 요소
     - 새로운 요소로 레이아웃
* 실습: https://flexboxfroggy.com   
**Flexbox** : Flexbox는 최신 웹을 위해 제안된 기존 레이아웃보다 더 세련된 방식의 새로운 것에 관련하여 CSS3의 레이아웃 방식
  - 주축(좌->우)과 교차축(위->아래)으로 설정
  - 요소를 보고 주축방향이 가로로 갈지 세로로 갈지 확인
  - 주축이 flxe-direction에 의해 가로 혹은 세로에 설정되면 교차축은 자동으로 설정됨
  - 1~3은 박스채 이동, 4~5는 박스안 하나의 요소만 ㅣ동

1. justify-content(주축 이동) : 가로선 상에서 정렬
   - flex-start: 요소들을 컨테이너의 왼쪽으로 정렬합니다.
   - flex-end: 요소들을 컨테이너의 오른쪽으로 정렬합니다.
   - center: 요소들을 컨테이너의 가운데로 정렬합니다.
   - space-between: 요소들 사이에 동일한 간격을 둡니다.
   - space-around: 요소들 주위에 동일한 간격을 둡니다. -> 요소를 포함해 동그란 원을 그릴때 박스안에 동일한 원이 크기르 차지함

2. align-items(교차축 이동) : 세로선 상에서 정렬
   - flex-start: 요소들을 컨테이너의 꼭대기로 정렬합니다.
   - flex-end: 요소들을 컨테이너의 바닥으로 정렬합니다.
   - center: 요소들을 컨테이너의 세로선 상의 가운데로 정렬합니다.
   - baseline: 요소들을 컨테이너의 시작 위치에 정렬합니다.
   - stretch: 요소들을 컨테이너에 맞도록 늘립니다.

3. flex-direction(기본 주축방향 반대로 설정) : 정렬할 방향 지정
   - row: 요소들을 텍스트의 방향과 동일하게 정렬합니다.
   - row-reverse: 요소들을 텍스트의 반대 방향으로 정렬합니다.
   - column: 요소들을 위에서 아래로 정렬합니다.
   - column-reverse: 요소들을 아래에서 위로 정렬합니다

4. order 
   - 원하는 요소를 지정한 뒤 원하는 자리로 보내기

5. align-self : 지정된 align-itmes 값을 무시하고 개별 요소에 적용할 수 있는 또 다른 속성
   - flex-start: 요소를 컨테이너의 꼭대기로 정렬합니다.
   - flex-end: 요소를 컨테이너의 바닥으로 정렬합니다.
   - center: 요소를 컨테이너의 세로선 상의 가운데로 정렬합니다.
   - baseline: 요소를 컨테이너의 시작 위치에 정렬합니다.
   - stretch: 요소를 컨테이너에 맞도록 늘립니다.

6. flex-wrap : 요소들을 한 줄 또는 여러 줄에 걸쳐 정렬
   - nowrap: 모든 요소들을 한 줄에 정렬합니다.
   - wrap: 요소들을 여러 줄에 걸쳐 정렬합니다.
   - wrap-reverse: 요소들을 여러 줄에 걸쳐 반대로 정렬합니다.


8. align-content : 여러 줄 사이의 간격을 지정
   - 한 줄만 있는 경우, align-content는 효과를 보이지 X
   - flex-start: 여러 줄들을 컨테이너의 꼭대기에 정렬합니다.
   - flex-end: 여러 줄들을 컨테이너의 바닥에 정렬합니다.
   - center: 여러 줄들을 세로선 상의 가운데에 정렬합니다.
   - space-between: 여러 줄들 사이에 동일한 간격을 둡니다.
   - space-around: 여러 줄들 주위에 동일한 간격을 둡니다.
   - stretch: 여러 줄들을 컨테이너에 맞도록 늘립니다.

7. flex-flow
   - flex-direction와 flex-wrap의 인자를 한번에 받아사용

### Bootstrap
  - CDN 링크 가져오기
    - bs 데이터는 미국에 있어서 가져오는데 시간이 걸릴수 있음. 이에 한국에서 사용할때 가까운 곳에서 쓸수 있도록 확장자를 만들어서 배포함
    - class로 되어있어서 만개가 넘는 css를 사용할 수 있음
  - div + .원하는 class명 + tab : div랑 class를 한번에 만들어주는 init
  
* 실습파일 : 00_intro.html
    - 카드를 넣고 각 카드들 사이의 간격을 벌리고 싶을때 
flex 사용
      - ms -> s = start : 언어 시작기준에서 간격띄우기(사우디어면 오른쪽이 시작지점)
      - me -> e = end : 언어 종료지점에서 간격띄우기(사우디어면 왼쪽이 종료지점)
    - hr : 수평선 작성

* 실습파일: 01_grid.html(bootstrap사이트 - layout - Breakpoints, Containers, Grid)
  - bootstrap에서 가장중요한게 grid 시스템이라 할 수 있음. 물론 grid가 boot말고 다른것도 있지만 boot의 grid를 사용함
  - flexbox의 격자 시스템(12칸이 기준으로 12가 약수가 많아 기준값으로 지정됨)
  - class="col" : 격자를 쓰는 코드
    - col만 쓰면 균등분배가 되며 class="col"이 여러개면 자동으로 12를 있는 수만큼 나눠서 크기를 균등 분배함. 
    - 물론 class="col-4"로 해당 class는 4칸으로 쓰겠다.
    - 반응형으로 만들기 -> col-12 col-md-6를 쓰면 반응형으로 화면 크기에 따라서 자동으로 크기를 늘이고 줄여줌
  - 한번에 모든 요소를 사이즈에따라 균등하게 나타나는 구조로도 작성할 수 있음 
    - 부모요소(row)옆에 `row-cols-1 row-cols-sm-2 row-cols-md-3 row-cols-lg-4 row-cols-xl-6` 작성
    - row-cols-* 클래스는 각 화면 크기에 따라 열(column)의 수를 설정함. 예를 들어, row-cols-1은 가장작은 화면 크기에서 열을 1개로 설정하고, row-cols-sm-2는 다음으로 작은 화면 크기(sm)에서는 열을 2개로 설정하는 것을 의미
  - container : 양옆에 여백을 주는것

  - Available breakpoints은 각 기기의 사이즈를 대충나타내주면서 반응형이 각 사이즈에 맞춰서 나올수 있도록 코드를 줌
    - extra small : mobile/ Small : mobile 가로/ Medium : 태블릿/ Large : 노트북/ Extra large : 데스크탑/ Extra extra large : 대형모니터
순으로 사이즈를 대충 표현함. 

* 실습파일 : practice 
> class안에 내가 원하는 디자인 clss 넣기만 하면 됨
1. navebar
   - d-flex : flexbox의 레이아웃을 적용
   - justify-content-between : 바 내부 요소간 거리를 동일한 간격으로 분포
   - bg-body-tertiary : 네비게이션 바의 배경색을 지정
   - sticky-top : 상단고정
   - fs-5 : 폰트 사이즈
   - fw-bold : 볼드체 적용
   - text-decoration-none : 폰트 밑줄 제거
   - text-dark : 폰트 색상 검정
   - mx-2 : 요소간 간격사이 벌리기

2. header
   - container : 사이즈에 따라서 양쪽 여백을 줌

3. section
   - container: 사이즈에 따라 양쪽 여백 줌. 젤 상단에 줘야 하위요소들에 속성값이 해당됨
   - text-center: 중앙정렬
   - py-5: 상하 패딩공간 5주기
   - fw-bold : 폰트 볼드체
   - bg-dark : 백그라운드 어둡게
   - text-white : 폰트 하얗게
   - row : row안에 넣은 하위요소에 카드들을 넣어야함. 그래야 동일한 값이 같은 카드에 적용됨
   - col : row 밑에 넣지만 카드들위에 넣어야 grid 시스템의 영향을 받음
   - card : 카드 양식넣기
   - card-imag-top: 카드(부모요소)에 맞춰서 이미지(자식요소) 사이즈가 맞춤됨
   - card-body : 밑에 내용 넣기
   - row-cols-1 : 엄청 작은 화면일때는 한개
   - row-cols-sm-2 : 그다음은  두개
   - row-cols-md-3 : 그다음 사이즈는 세개씩
   - row-cols-lg-4 : 그다음 큰 사이즈에서는 4개씩
   - my-2 : col 옆에 적어야함. 이것도 마진을 줄수 있지만 각 카드마다 하나씩 넣어줘야함
   - gutter(g-3) : row 옆에 적어야함. 그래서 한번에 줄수 있음
   - btn btn-primary : 파란색 버튼으로 바꾸기

4. footer(여기선 boot제공말고 그냥 해보기)
   - shop.css 코드 새로 작성 -> width 3rem: 가로폭 3rem 고정
   - d-flex : footer 자체를 플렉스 박스로 만들수 있음
   - justify-content-center : 가운데로 모으기
   - bg-Secondary : 컬러 이름(회색)
   - p-5 : 패딩을 줘서 하단 창 크게 만들기
   - mt-3 : 위에 카드와 떨어트리고 싶음
