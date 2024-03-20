# linux
git bash에서 .ssh로 이동한 다음 aws 퍼블릭 코드(ssh -i "V-lab.pem" ubuntu@ec2-3-114-30-206.ap-northeast-1.compute.amazonaws.com)를 사용해서 ubuntu계정으로 시작을 해야함

## 설명 명령어
1. `man find`
   - 상세 메뉴얼
   - 특정 파일에 (> or >>)을 사용해 결과 내용을 입력할수 있음
2. `find -hlep(find -h, find --h)    `
   - 간략 메뉴얼
   - man find보다 엑기스만 보여주는 것으로 

## 파일시스템 명령어(무조건 외우기)
[리눅스 경로 표시방법]
- `/` : 루트입니다. 시스템의 시작 부분을 의미합니다.
- `~` : 현재 로그인한 유저의 `home` 경로입니다.
  - 내가사용하는 계정의 가장 상위 디렉토리
- `/` : 디렉토리 경로 상에 있는 경우 디렉토리를 구분하는 구분자의 역할을 합니다.
- `..` : 상위 디렉토리를 의미합니다.
- `.` : 현재 디렉토리를 의미합니다.
- `-` : 이전 위치를 의미합니다.
---
1. `pwd`
      - 현재 경로 확인
   - 실행 결과 : `/home/ubuntu`
        - ubuntu는 root을 대체하는 역할
        - 경로: root -> home -> ubuntu
        - 이때 사실상 home 위의 경로는 거의 건드리면 안됨
2. `ll(ls -al)`
   지정한 경로에 있는 모든 파일 및 디렉토리의 목록을 보여줍
   - 실행 결과 : `-rw-r--r-- 1 ubuntu multi     0 Mar 13 16:19 .sudo_as_admin_successful`
     - -rw-r--r-- : 디렉토리명
     - 1 : 디렉토리 안의 파일 개수
     - ubuntu : 사용 계정
     - 0 : 저장용량
     - .은 파일을 숨김처리함
3. `ls`
   - 간단한 목록 확인
4. `mkdir '디렉토리(폴더) 명'`
   - 디렉토리 생성
   - 숨겨진 디렉토리를 생성하려면 폴더명 앞에 .을 붙이기
   - `mkdir -p '폴더 명'` : 하위 디렉토리를 한꺼번에 생성하기 위해 -p 옵션을 넣음
5. `cd '디렉토리명'`
   - 디렉토리 이동
6. `rm '파일 명`
   - 파일 및 디렉토리 삭제
   - 다만 디렉토리를 삭제할때는 -r을 기입
     - `rm -r '디렉토리명'`
7. `chmod`
   - 파일 권한 변경하기
   - ~$ ll을 했을때 나타나는 디렉토리 목록에서 맨앞 10자리를 볼 수 있음
     - 권한 예시 : drwxrwxr-x
       1. `d` : 디렉토리를 의미합니다. 파일인 경우 `-`가 됩니다.
       2. `rwx` : 파일 소유자에 대한 권한을 의미합니다.
       3. `rwx` : 파일 소유자가 속한 그룹에 대한 권한입니다.
       4. `r-x` : 파일 소유자가 속하지 않은 그룹에 대한 권한입니다.
       - d를 제외한 앞쪽 세자리는 같은 그룹을 뒤쪽 6자리는 그룹에 대한 권한을 의미
   - 이진법으로 표시가 됨
     - rwx(읽기 4, 쓰기 2, 실행 1)
        - `---` : 0+0+0=0
        - `--x` : 0+0+1=1
        - `-w-` : 0+2+0=2
        - `-wx` : 0+2+1=3
        - `r--` : 4+0+0=4
        - `r-x` : 4+0+1=5
        - `rw-` : 4+2+0=6
        - `rwx` : 4+2+1=7
    - 만약 dir1 폴더에 대한 권한을 소유자는 읽기,쓰기,실행을 모두할 수 있고(rwx : 7), 같은 그룹내 사용자는 읽기와 쓰기만(rw- : 6), 다른 그룹내의 사용자는 실행에 대한 권한(--x : 1)을 모두 주려면 `chmod 761 '폴더명'`을 실행!
    - 하위 디렉토리까지 다 동일하게 주고 싶으면 `-R` 옵션도 함께 부여
      - `chmod -R 761 '폴더명'`

## 파일 관리 명령어
1. `&&`
   - 두개의 명령어를 동시에 실행 할 수 있음
     - 실행 예시 : `mkdir sample && cd sample`
       - sample파일을 만들고 이동하겠다
2. `touch '파일명'`
   - 비어있는 파일 만들기
3. `cat '파일명'`
   - 파일 내용 출력하기
4. `echo "메시지"`
   - 메시지 출력
   - 특정 파일에 (> or >>)을 사용해 메시지를 입력할수 있음
     - `echo "하이하이" >> newfile`
       - newfile이란 파일에 하이하이라는 메시지를 넣음
     - `>` 는 create or overwrite, `>>`는 create or append   
        - `>` 를 사용하면 내용이 덮어써지고, `>>`를 사용하면 내용을 아랫줄에 추가
5. `head '파일명'` or `tail '파일명'`
   - head 명령어는 파일의 내용의 앞 부분 부터 보여주며, tail은 뒷 부분을 보여줌
   - `-n` 옵션을 이용해 출력할 라인 수를 지정할 수 있음
     - 실행 예시: `head -n 20 '파일명'`   
        -> 위에서부터 20줄 보여줘
6. `mv '위치/파일명' '위치2/파일명'`
   - 파일 이동 및 이름변경
   - 이동 예시
     - `mv sample/newfile sample2/newfile`
   - 이름 변경 예시
     - `mv sample2/newfile sample2/gamja`
7. `cp`
   - 파일 복사
   - 복사하면서 이름도 새로 지정할 수 있음
   - 복사 예시
     - `cp sample2/gamja sample2/goguma`

## 파일 검색
1. `find`
   - 파일 이름을 이용해 찾기
   - 애스터리스크(*)를 이용해 패턴을 지정할 수 있음
   - 실행 예시: `find . -name "sam*"`
     - 파일이름이 sam이으로 시작하는 파일을 찾아줌
2. `grep`
   - 파일 이름 및 파일 내용을 이용해 찾기
   - find와 비슷한 역할을 하지만 find보다 폭 넓은 검색을 지원
   - 실행 예시: `grep -rn "sam*"`
     - 현재 위치에서 sma이라는 문자열이 들어간 파일과 파일 내용을 찾아줌
   - 실행 예시2: `grep -rn "[a-zA-Z]\+tion$" .`
     - 각 라인의 끝이 tion으로 끝나는 내용이 들어있는 파일을 정규식을 통해 찾아줌
3. `wich`
   - 환경 변수의 원래 경로 찾기
   - 만약 가상환경안에서 사용하는 파일을 찾으면
     - /home/ubuntu/miniconda3/envs/spark-env/bin/python
     - 위의 결과처럼 spark-env라는 가상환경안에 python을 찾아줌

## 시스템 명령어
1. `uname`
   - 현재 시스템 정보 알아보기
   - `-a`를 사용해 자세한 정보를 알아볼 수 있음
2. `ps`⭐⭐⭐⭐⭐
   - 프로세스 확인
   - 실행 결과
        ```
        PID TTY          TIME CMD
        1957 pts/1    00:00:00 bash
        3391 pts/1    00:00:00 ps
        ```
     - PID는 프로세스 고유의 아이디(프로세스는 램에 올라와있는 실행중인 것!)
3. `kill`⭐⭐⭐⭐⭐
   - 진행중인 프로세스를 강제로 프로세스를 죽여줌
   - `kill -9 "pid 숫자"`에서 -9는 가장 강력한 시그널
     - -9 시그널(SIGKILL)은 프로세스를 강제로 종료하겠다는 시그널
     - -9 시그널 이외에 -15 시그널(SIGTERM)도 많이 사용됩니다. SIGTERM은 보통 어플리케이션에서 종료 시그널을 받았을 때 현재 처리하고 있는 내용을 다 처리하고 종료하거나 특정 상황에서 강제 종료되는 상황 등을 막기 위해 사용
     - 즉, -9 시그널은 언제든지 강제 종료가 되기 때문에 어플리케이션이 작업 중이던 내용을 다 처리하지 못하고 종료되지만, -15 시그널은 개발자가 시그널을 처리하기 위한 로직(코드)을 구현할 수 있음
   

# 프로그램 설치
## 파이썬 및 주피터 노트북 개발환경 구축
[참고링크](https://radial-fighter-931.notion.site/Python-c219574fd69e431f8c5ce80490ebf4f2)
aws가 실행된 환경(ubuntu@ip-172-31-11-147:~$ )에서 실행
1. 미니콘다 설치 -> 아래 코드 실행
   - wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
2. 미니콘다 설치를 다하면 bash파일을 실행
   - bash Miniconda3-latest-Linux-x86_64.sh
   - 약관 동의가 나오는데 계속 엔터키 누르기(혹은 q누르면 맨밑으로 내려감)
   - yes/no 질문에 전부 yes 누르기
3. sourch를 통해 .bashrc불러오기
   - ubuntu@ip-172-31-33-75:~$ source ~/.bashrc
   - 실행 결과 아래와 같이 이름이 바뀜
     - (base) ubuntu@ip-172-31-11-147:~$
4. (base) ubuntu@ip-172-31-11-147:~$에서 python 위치 확인해보고 잘되었는지 확인
   - which python
5. 이제 juypyter Notebook 설치 하기전 가상환경 실행하기
   - (base) ubuntu@ip-172-31-11-147:~$ conda create -n spark-env python=3.8
     - yes/no에서 yes 누르기
6. 설치한 후 spark-env 실행
   - (base) ubuntu@ip-172-31-11-147:~$ conda activate spark-env
7. 6번을 실행하면 (spark-env) ubuntu@ip-172-31-11-147:~$ 으로 바뀜. 여기서 jupyter notebook 설치
   - pip install notebook==6
8. 파이썬 실행하기
   - (spark-env) ubuntu@ip-172-31-11-147:~$ python
8. 파이썬이 실행되면 >>>가 뜨는데 거기에 아래 코드 실행하기
   - ``` >>> from notebook.auth import passwd```
   - ``` >>> passwd()```
   - 비밀번호 입력하기
   - 비밀번호 설정을 완료하면 아래코드가 나오는데 메모해두기
     - sha1:90d53d84d759:e32d5cd277594a998216f02a1ee012f9114b4539
9. 파이썬 끄기 : `ctrl + D`
    - 파이썬 종료하면 다시 아래 이름으로 나와짐
      - (spark-env) ubuntu@ip-172-31-11-147:~$ 
10. 아래 코드 실행
    - jupyter notebook --generate-config
11. 10번이 성공하면 아래 코드 실행해서 파일을 열어주기
    - sudo vim /home/ubuntu/.jupyter/jupyter_notebook_config.py
      - 참고로 window10Rkwlsms
12. 파일이 열린것을 확인한 후 `i`를 입력해 INSERT 모드로 만들어주고 C = get_config()아래에 아래 코드 입력
    ```
    c.NotebookApp.password = u'argon으로 시작하는 비밀번호'
    c.NotebookApp.ip = 'EC2 내부 IP'
    c.NotebookApp.notebook_dir = '$your_notebook_root_dir_path'
    ```
    - 여기서 아래 처럼 몇몇 정보를 바꿔야함
      - argon으로 시작하는 비밀번호 = 과정 8번에 메모한 코드 넣기 
      - EC2 내부 IP = 내 인스턴스 프라이빗 IPv4 주소 넣기
      - 
    ```
    c.NotebookApp.password = u'sha1:90d53d84d759:e32d5cd277594a998216f02a1ee012f9114b4539'
    c.NotebookApp.ip = '172.31.11.147'
    c.NotebookApp.notebook_dir = '/home/ubuntu/working'
    ```
13. 다하면 esc버튼 누르고 :wq 입력해서 벗어나기
14. 아직 우린 working 파일이 없어서 만들어 주기
    - mkdir working
15.  jupyter notebook 서버를 실행
    - jupyter notebook --allow-root
      - 실행하다면 노란색 뭐가 뜨는데 그냥 무시 ㄱㄱ
16. 끝!

### 설치한 노트북 입력해보기
- 기존에는 노트북에서 실행해서 local/host888? 같은걸로 주피터노트북을실행을 했다면
- 이제는, 노트북서버를 ec2에 접속을 할 수 있게 퍼블릭 아이피, 포트번호를 사용
1. 구글 크롬 새창에 `퍼블릭 IPv4 DNS` + `:8888` 입력
2. 비밀번호 입력 하면 주피터 화면이 잘 나옴!

## 인스턴스 내용
- 보안
ec2에 접근하기 위해서는 .pem 파일이 필요하지만,
ec2에서 만든 서버에는 .pem이 없어도 접근할 수 있음

## Java 개발환경 구축
- 대부분의 빅데이터 툴이 Java기반으로 되어있어 해보는 것을 추천
- `(spark-env) ubuntu@ip-172-31-11-147:~$` 환경에서 시작!
1. 자바 설치전 업데이터 먼저해주기
   - sudo apt-get update
   - sudo apt-get upgrade
     - yes 입력해주기
2. OpenJDK 8 실행 설치
   - sudo apt-get install openjdk-8-jdk -y
3. `java -version`을 입력하여 자바가 잘 설치되었는지 확인
   - 아래 결과가 나오면 잘된거임
    ```
    openjdk version "1.8.0_362"
    OpenJDK Runtime Environment (build 1.8.0_362-8u372-ga~us1-0ubuntu1~20.04-b09)
    OpenJDK 64-Bit Server VM (build 25.362-b09, mixed mode)
    ```
4. `readlink -f $(which java)`를 입력해 실제 자바 설치 위치를 확인
   - which 함수를 사용해 java의 경로를 찾음
     - /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java
   - 이 경로를 복사해서 환경 변수에 등록하기
5. 환경변수를 등록하기 위해 `vim ~/.bashrc`를 실행
6. 새로운 창이뜨면 shift + g를 해서 맨아래칸으로가서 i를 입력해 INSERT환경으로 바꿔 아래 환경변수를 입력해주기 
    ```
    # JAVA_HOME
    export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre
    export PATH=$PATH:$JAVA_HOME/bin
    ```
   - JAVA_HOME이 환경변수로 대문자로해줌
     - 예를 들어 하둡을 깔면은 HADOOP_HOME
     - 스파크를까렴 SPARK_HOME으로 환경변수 입력
7. 입력후 `ESC`를 눌러 명령어 모드로  진입한 후 `:wq`를 누르고 나오기
8. 가상환경에서 `echo $JAVA_HOME`을 누르면 아무런 창이 뜨지않음. 이에 `source ~/.bashrc`를 입력해  (base) ubuntu@ip-172-31-11-147:~$의 환경으로 바꾼뒤 다시 `echo $JAVA_HOME`를 입력하면 자바 경로가 잘 설정된것을 볼 수 있음
    <p align="center">
      <img src="../이미지/Linux01.png">
   </p>
```
[번외]
echo는 단순히 출력을 하겠다는 명령어 이기 때문에 .bashrc에 기록된 내용 말고 다른 쪽에 있는 환경변수나 다른 값들도 확인하는 것이 가능합니다~!

그런데 기본적으로 대부분의 환경변수는 bashrc에 기록하기 때문에 echo로 보는 환경변수는 대부분 .bashrc에 있는 것이라고 생각하면 될 것 같아요!
```

## Visual Studio Code 연동하기
이건 충분히 강사님 설명잘되어 있어서 아래 링크 참고하기    
[참고](https://radial-fighter-931.notion.site/AWS-2b3e5feb815e45e5b799dd7e332d0db8#faff7bc84b8a40b08ada86084e12f112)

1. Remote - SSH, Remote -SSH: Editing Configuration Files 확장 모듈을 설치
2. 왼쪽 밑 >< 파란색 아이콘 클릭
3. connet to Host 클릭
4. configure SSH Hosts 클릭
5. 맨위 C:\Users\user\/ssh\config 클릭
6. config화면이 뜨면 기존에 있는 화면 지우고 새로 입력
   ```
   Host 커넥션이름(아무거나 지정해도됩니다. 단, 띄어쓰기는 하지마세요)
    HostName AWS Public IP 주소
    User ubuntu
    IdentityFile ~/.ssh/key파일이름.pem
   ```
   - 위의 내용을 아래처럼 입력
   ```
   Host AWS_MULTI
    HostName ec2-3-114-30-206.ap-northeast-1.compute.amazonaws.com
    User ubuntu
    IdentityFile ~/.ssh/V-lab.pem
   ```
   - 다하면 저장
7. 다시 왼쪽 밑 >< 파란색 아이콘 클릭
8. connet to Host 클릭
9. 새로 뜬 AWS_MULTI 클릭
10. 새로운 창이 뜨고 LINUX 클릭
11. 성공적으로 연결이 된 후 파일 목록에서 Open Folder를 눌러보면 다음 처럼 원격 연결된 ec2의 디렉토리 목록을 확인할 수 있음
12. 끝!

# 분산 시스템
> 여러대의 컴퓨터를 사용!
## 기본특징
1. Concurrency   
자원은 공유하면서, 리소스내에서 동시에 여러가지 작업을 수행합니다. 동시 실행 자원을 늘려서 처리량을 늘릴 수 있습니다.
2. No Global Clock   
시스템의 각 부분이 비동기식으로 동작합니다. 또한 어떤 한 부분의 상태 때문에 다른 곳에 Lock, Bottleneck 이 걸리면 안됩니다.
3. Independent Failure    
시스템의 한 부분의 실패가 전체 시스템에 영향(장애)을 주면 안됩니다.   
즉, 독립적!

## 분산 시스템의 고려 요소 
운영체제, HW 에 대한 임팩트가 크기 때문에, OS, HW 관계없이 일관된 개발을 하기 위한 언어를 선택
- Java가 가장 대표적임

# 빅데이터 엔지니어링의 개요
Hadoop이 제일 탄탄함.

실시간 데이터를 사용한다면 realtime data를 사용하는 tool을 사용하고
과거 데이터를 하용하려면 betch data를 사용하는 tool을 사용할 수 있음
    - 여기서 과거의 데이터라한다면 pandas라고도 할수 있음. 왜냐면 생각해보면 pandas도 csv와 같은 과거 데이터를 다루기에!
  
data lake는 가공이 되자 않은 데이터가 쌓아놓는것. 그래서 django자체가 데이터 레이크라 할 수 있음. 즉, 이렇게 정리가 안된 애들을 data warehouse에 분류, 정리를 해야함

data warehouse는 데이터의 최소한의 정리만 하는것으로 none값을 정리하거나 필요하면 join을 할 수 있음

다음이 상품화하는과정으로 이러헥 상품이 되는 애들이 모여있는 곳이 data mart임.

마지막으로 상품화가 된 데이터로 분석을 하고 이것저것 할 수 있은것!

그래서 사실 Spark 하나만으로 웬만한 툴은 다 대체할 수 있음. 짱짱맨!

요즘 하둡은 데이터 저장소이기에 툴간의 연결다리? 빅데이터 시스템을 하둡기반으로 구축하는 정도로만 다룸.
즉, 하둡을 해본적이 있냐라는 질문은 하둡기반응로 빅데이터 분석 프로젝트를 해봤냐라는 질문으로 생각하면 됨