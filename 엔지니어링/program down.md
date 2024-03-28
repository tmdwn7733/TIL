
# 프로그램 설치

```
(base) ubuntu@ip-172-31-11-147: 시작방법
1. git bash에서 .ssh로 이동
2. aws 퍼블릭 코드(ssh -i "V-lab.pem" ubuntu@ec2-3-114-30-206.ap-northeast-1.compute.amazonaws.com)를 사용해서 ubuntu계정으로 시작을 해야함
```

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
    ```XML
    c.NotebookApp.password = u'argon으로 시작하는 비밀번호'
    c.NotebookApp.ip = 'EC2 내부 IP'
    c.NotebookApp.notebook_dir = '$your_notebook_root_dir_path'
    ```
    - 여기서 아래 처럼 몇몇 정보를 바꿔야함
      - argon으로 시작하는 비밀번호 = 과정 8번에 메모한 코드 넣기 
      - EC2 내부 IP = 내 인스턴스 프라이빗 IPv4 주소 넣기
    ```XML
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
    ```Bash
    openjdk version "1.8.0_362"
    OpenJDK Runtime Environment (build 1.8.0_362-8u372-ga~us1-0ubuntu1~20.04-b09)
    OpenJDK 64-Bit Server VM (build 25.362-b09, mixed mode)
    ```
4. `readlink -f $(which java)`를 입력해 실제 자바 설치 위치를 확인
   - which 함수를 사용해 java의 경로를 찾음
     - /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java
   - 위 경로를 복사해서 환경 변수에 등록하기
5. 환경변수를 등록하기 위해 `vim ~/.bashrc`를 실행
   - 환경변수 등록은 어떤 창에 있어도 실행해도 ㄱㅊ
6. 새로운 창이뜨면 shift + g를 해서 맨아래칸으로간 뒤 i를 입력해 INSERT환경으로 바꿔 아래 환경변수를 입력해주기 
    ```XML
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
      <img src="../이미지/program down01.png">
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


## Haddop
`(base) ubuntu@ip-172-31-11-147:~$` 환경에서 시작
### 하둡 설치하기
   1. `wget https://dlcdn.apache.org/hadoop/common/hadoop-3.2.4/hadoop-3.2.4.tar.gz`
      - `ls`로 다운 잘됐는지 확인(결과물에 hadoop-3.2.4.tar.gz 이가 있어야함)
   2. `tar xvfz hadoop-3.2.4.tar.gz` : 압축해재하는 기능
   - `ls`로 확인(hadoop-3.2.4)
   3. `vim ~/.bashrc`로 들어가서 환경변수 등록해주기
      - 가장 아래에 들어가서(shift+G) 아래 코드 입력해주기
         ```XML
         export HADOOP_HOME=/path/to/hadoop-3.2.4
         export PATH=$PATH:$HADOOP_HOME/bin
         ```
         - 여기서 /path/to/는 본인 컴퓨터상의 환경으로 새로 입력
         ```XML
         export HADOOP_HOME=/home/ubuntu/hadoop-3.2.4
         export PATH=$PATH:$HADOOP_HOME/bin
         ```
   - `ESC`를 누르고 `:wq`로 저장후 나오기
   - `echo $HADOOP_HOME`로 잘 저장되었는지 확인하기
### ssh로그인 설정하기
   - ssh를 왜설정하나?
     - A컴퓨터에서 B컴퓨터에 접근할때 ssh(열쇠)를 사용해 자물쇠를 따는것
     - 키박스에 키를 넣어둬 이걸 가지고 있는 사람이 자동문마냥 통과 할수 있도록 해줌
   - `ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa`로 키를 생성
   - `ls ~/.ssh/`로 authorized_keys, id_rsa, id_rsa.pub 이 세개가 나오는지 보기
   - `cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys`로 키를 키박스에 넣어두기
   - `chmod 0600 ~/.ssh/authorized_keys`로 이컴퓨터에서만 읽고, 쓰기만 할수 있게 해주기
   - 다하면 `ssh localhost`를 해서 잘 통과되는지 확인하기
     - yes/no질문에 yes로 하기
     - `exit`로 해서 나오고 다시 `ssh localhost`하면 바로 들어가는 것을 볼 수 있음
   - 끝!
   - 참고로 `w`를 하면 내가 어디이고 어떤 상태인지 볼 수 있음

### 하둡 설정하기
   1. `cd $HADOOP_HOME/etc/hadoop/`로 폴더로 들어가기
   2. `ls`로 파일들 잘 있는지 확인
   3. core-site.xml 설정
      - `vim $HADOOP_HOME/etc/hadoop/core-site.xml`를 입력해 네임노드를 띄울 서버만 지정
      - 아래 코드를 맨 아래에 입력하기
      - AWS 퍼블릭코드 수정 필요함
      ```XML
      <configuration>
      <configuration>
         <property>
                  <name>fs.defaultFS</name>
                  <value>hdfs://ec2-3-114-30-206.ap-northeast-1.compute.amazonaws.com:9000</value>                   
         </property>
      </configuration>
      </configuration>
      ```
      - 다하면 `:wq`로 저장후 나오기
   4. hdfs-site.xml 설정
      - `vi $HADOOP_HOME/etc/hadoop/hdfs-site.xml`를 입력해 hdfs에 관련된 설정들을 작성
      - 아래 코드로 입력
      - 이때 내 AWS 퍼블릭 아이디 집어넣는거랑, 경로 조심하기
      ```XML
      <configuration>
         <property>
            <name>dfs.replication</name>
            <value>1</value>
         </property>
         <property>
            <name>dfs.namenode.name.dir</name>
            <value>/home/ubuntu/hadoop-3.2.4/dfs/name</value>
         </property>
         <property>
            <name>dfs.datanode.data.dir</name>
            <value>/home/ubuntu/hadoop-3.2.4/dfs/data</value>
         </property>
         <property>
            <name>dfs.namenode.http-address</name>
            <value>ec2-3-114-30-206.ap-northeast-1.compute.amazonaws.com:9870</value>
         </property>
      </configuration>
      ```
   5. `cd ~`를 하고 홈으로 나오기
   6. `mkdir -p $HADOOP_HOME/dfs/name`로 파일생성
   7. `mkdir -p $HADOOP_HOME/dfs/data`로 파일생성
   8. `ls $HADOOP_HOME/dfs`로 data랑 name 파일 만들어 졌는지 확인
   9. yarn-site.xml 설정
      - `vi $HADOOP_HOME/etc/hadoop/yarn-site.xml`
      - 아래코드 넣기. 
      - AWS 퍼블릭코드 수정 필요함
         ```XML
            <property>
               <name>yarn.nodemanager.aux-services</name>
               <value>mapreduce_shuffle</value>
            </property>
            <property>
               <name>yarn.nodemanager.env-whitelist</name>
               <value>JAVA_HOME,HADOOP_COMMON_HOME,HADOOP_HDFS_HOME,HADOOP_CONF_DIR,CLASSPATH_PREPEND_DISTCACHE,HADOOP_YARN_HOME,HADOOP_HOME,PATH,LANG,TZ,HADOOP_MAPRED_HOME</value>
            </property>
            <property>
               <name>yarn.resourcemanager.webapp.address</name>
               <value>ec2-3-114-30-206.ap-northeast-1.compute.amazonaws.com:8088</value>
            </property>
            <property>
               <name>yarn.nodemanager.webapp.address</name>
               <value>ec2-3-114-30-206.ap-northeast-1.compute.amazonaws.com:8042</value>
            </property>
         ```
   10. mapred-site.xml 설정
      - `vi $HADOOP_HOME/etc/hadoop/mapred-site.xml`
      - 아래코드 수정없이 삽입
         ```XML
            <property>
               <name>mapreduce.framework.name</name>
               <value>yarn</value>
            </property>
            <property>
               <name>mapreduce.application.classpath</name>
               <value>$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/*:$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/lib/*</value>
            </property>
               <property>
                     <name>yarn.resourcemanager.webapp.address</name>
                     <value>0.0.0.0:8088</value>
               </property>
               <property>
               <name>mapreduce.jobhistory.webapp.address</name>
               <value>0.0.0.0:19888</value>
            </property>
         ```
   11. hadoop-env.sh 설정
      - `vim $HADOOP_HOME/etc/hadoop/hadoop-env.sh`
      - 아래 코드 그냥 맨 아래에 삽입
         ```XML
         JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre
         ```

### HDFS 실행
   1. `hdfs namenode -format`실행해서 포멧진행!
   2. `$HADOOP_HOME/sbin/start-dfs.sh`로 하둡실행! 그냥 외우기⭐⭐⭐
   3. `jps`를 실행해서 네임노드와 데이터노드, 세컨더리 네임노드가 정상적으로 실행됐는지 확인
      - 아래처럼 나오면 끝! 나와야함
         ```Bash
         11136 NameNode
         11641 Jps
         11532 SecondaryNameNode
         11295 DataNode
         ```
   4. 나의 `AWS퍼블릭아이디 DNS:9870`을 구글 탭에 입력하면 hdfs의 web ui도 볼 수 있음
      - 하둡을 관리하고 요약을 보고싶으면 이페이지 만한게없음
        - :9864
        Data Node_실무자들을 한번에 볼수 있음
        - Utilities > Logs
          - 노드별로 로그가 계속 쌓이는데, 무슨 에러인지 정보가 다 담겨있음
          - `IOException`이 Java에서 에러표시를 나타내는것으로 생각하면 에러찾기가 수월함

### YARN 실행
1. `$HADOOP_HOME/sbin/start-yarn.sh`실행
2. `jps`를 실행해서 ResourceManager랑 NodeManager가 잘뜨는지 확인
3. 리소스 매니저를 위한 UI도 따로 제공
   - `AWS퍼블릭아이디 DNS:8088`을 구글탭에 입력
   - 작업하다 잘 안되면, Resource를 많이봄

### JobHistroyServer 실행
1. `mapred --daemon start historyserver`실행
2. `jps`를 실행해서 JobHistoryServer확인
3. 작업 내역을 확인할 수 있는 UI를 확인
   - `AWS퍼블릭아이디 DNS:19888`

### 맵리듀스 예제 실행
구글탭 세개(9870, 8088, 19888)모두 키고 진행!
1. 원주율 구하는 `hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.2.4.jar pi 16 10000`코드 실행!
2. 9870에서 Utilites를 보면 log가 있는데, 이때 이 로그를 통해서 각 프로세스의 과정과 오류를 다 확인할 수 있음
3. 8088을 재실행하면 새로운 작업이 보임.
   - 왼쪽 Finished를 누르면 어떤 어플리케이션이 실행됬는지 정보를 볼 수 있음
4. 19888도 재실행해 작업을 세부적인 작업내역을 볼 수 있음

### 프로세스를 종료
- 실행과정: 
  1. dfs(`$HADOOP_HOME/sbin/start-dfs.sh`) 
  2. yarn(`$HADOOP_HOME/sbin/start-yarn.sh`) 
  3. js(`mapred --daemon start historyserver`)
- 끄는과정: 실행과정 반대!
  1. js(`mapred --daemon stop historyserver`)
  2. YARN(`$HADDOP_HOME/sbin/stop-yarn.sh`)
  3. dfs(`$HADDOP_HOME/sbin/stop-dfs.sh`)
- 만약에 이런 과정이 귀찮다면 `$HADOOP_HOME/sbin/stop-all.sh`코드로 한번에 삭제후 `mapred --daemon stop historyserver`를 실행하면 아무것도 없는 걸 볼 수 잇음

### 하둡 자체적으로 삭제
`rm -r hadoop-3.2.4`

## HDFS

### HDFS CLI 환경 실습
1. (base) ubuntu@ip-172-31-11-147:~$ 상태로 시작
2. dfs, yarn 모두 실행하기
3. `hdfs dfs -mkdir /user/ubuntu/test` 실행
   - ⭐만약 실행이 안되면 `hdfs dfs -mkdir -p /user/ubuntu/test` 실행!
4. 이제 /user/ubuntu 가 hdfs상 home이라 할 수 있음
4. `hdfs dfs -ls .`를 실행해서 test가 잘나오는지를 확인
5. 데이터베이스 다운
   - `mkdir datasource`
   - `mkdir datasource/employees`
   - `cd datasource/employees/`
   - `wget wget https://raw.githubusercontent.com/mhso-dev/data-eng/main/employees`를 다운받으면 employees.csv파일이 다운받아짐
6. `cd ~`로 홈으로 나오기
7. `hdfs dfs -put /home/ubuntu/datasource/employees/employees /user/ubuntu/test/employees`를 실행하면 hdfs에 파일이 잘 올라간것을 확인
   - 띄어쓰기를 기준으로 앞에는 local의 경로 뒤에는 hdfs의 경로임
   - 이렇듯 뒤에 경로를 따로 지정해주지않으면 그냥 home에 들어가짐. 주의!
7. `hdfs dfs -ls /user/ubuntu/test`로 잘 들어갔는지 확인
8. 파일 내리기는법
   - `hdfs dfs -ls /user/ubuntu/test`

## Sqoop
### 테스트 데이터베이스 다운
1. 데이터세트부터설치
   ```Bash
   wget https://github.com/datacharmer/test_db/releases/download/v1.0.7/test_db-1.0.7.tar.gz
   tar xvfz test_db-1.0.7.tar.gz
   ```
2. `cd test_db` 를 이용해 디렉토리의 위치를 옮겨주기
3. 데모 데이터를 mysql에 적제하기
   - `mysql -u$mysql_user_name -p$mysql_user_password < employees.sql`
   - 해당 내용을 나의 정보로 채우면 아래와 같음
   - `mysql -umulti -p1111 < employees.sql`

### Sqoop 다운로드 및 설치
1. `cd ~`로 나오기
2. `wget http://archive.apache.org/dist/sqoop/1.4.7/sqoop-1.4.7.bin__hadoop-2.6.0.tar.gz`로 다운
3. `tar zxvf sqoop-1.4.7.bin__hadoop-2.6.0.tar.gz`로 압축해제
4. 디렉토리 이름변경해주기
   - `mv sqoop-1.4.7.bin__hadoop-2.6.0 sqoop-1.4.7`
   - `ls`로 이름 잘 바꼈는지 확인
5. 환경변수 설정해주기
   - `vi ~/.bashrc`로 이동
   - 맨아래에 아래 코드 입력해주기
      ```XML
      # SQOOP_HOME
      export SQOOP_HOME=/home/ubuntu/sqoop-1.4.7
      export PATH=$PATH:$SQOOP_HOME/bin
      ```
   - 저장후 나오기
6. 잘 설정 됐는지 확인
   - `source ~/.bashrc`와 `echo $SQOOP_HOME`를 실행
   - 결과에 /home/ubuntu/sqoop-1.4.7라 뜨면 잘 된것!
 
### 커넥터 다운로드
아래내용 다운로드
```
wget https://repo.maven.apache.org/maven2/mysql/mysql-connector-java/8.0.21/mysql-connector-java-8.0.21.jar
mv mysql-connector-java-8.0.21.jar $SQOOP_HOME/lib
```

### Sqoop -> HDFS(import)
1. SQOOP은 더이상 새로운 버전을 지원하지 않기에 꼭 아래라이브러리를 다운받고 Sqoop라이브러리에 추가
   - `wget https://dlcdn.apache.org//commons/lang/binaries/commons-lang-2.6-bin.tar.gz`
   - `tar zxvf commons-lang-2.6-bin.tar.gz`
   - `mv ~/commons-lang-2.6/commons-lang-2.6.jar $SQOOP_HOME/lib`
2. 스쿱을 이용해 RDBMS에 있는 데이터를 하둡에 적재
      ```Bash
      $SQOOP_HOME/bin/sqoop import \
      --connect 'jdbc:mysql://ec2-3-114-30-206.ap-northeast-1.compute.amazonaws.com/employees?useUnicode=true&serverTimezone=Asia/Seoul' \
      --username multi \
      --password 1111 \
      --query 'SELECT e.emp_no, e.birth_date, e.first_name, e.last_name, e.gender, e.hire_date, d.dept_no FROM employees e, dept_emp d WHERE (e.emp_no = d.emp_no) AND $CONDITIONS' \
      --target-dir /user/ubuntu/sqoop/employees \
      --split-by e.emp_no
      ```

### HDFS -> Sqoop(export)
사실상 Sqoop은 거의 사용하지 않는 추세고 안에 경로도 다 입력해야한다는 번거로움때문에 추출하는 과정은 더 사용안함


## Flume
(base) ubuntu@ip-172-31-11-147:~$ 상태에서 진행

### Apache Flume 설치와 설정
1. 라이브러리 다운후 이름 설정하기
   - `wget https://archive.apache.org/dist/flume/1.9.0/apache-flume-1.9.0-bin.tar.gz`
   - `tar xvfz apache-flume-1.9.0-bin.tar.gz`
   - `mv apache-flume-1.9.0-bin flume-1.9.0`
2. 환경설정 들어가서 플롬 환경 변수 추가
   - `vi ~/.bashrc`
   - 마지막 줄에 아래코드 넣기
      ```XML
      # FLUME_HOME
      export FLUME_HOME=/home/ubuntu/flume-1.9.0
      export PATH=$PATH:$FLUME_HOME/bin
      ```
3. 나와서 아래 코드진행
   - `source ~/.bashrc`
   - `echo $FLUME_HOME`
   - 결과는 /home/ubuntu/flume-1.9.0 이렇게 나와야함

### Agent 설정하기1(netcat source)
1. `cd $FLUME_HOME/conf`로 이동
2. `vim sample-agent-socket.conf` 입력
3. 새로운 파일이 열리면 아래 코드 그대로 넣기
   ```XML
   # Source, Sink, Channel 설정
   socket_sample_agent.sources = socket_sample_source
   socket_sample_agent.sinks = socket_sample_sink
   socket_sample_agent.channels = socket_sample_channel

   # Source 설정. netcat을 통해 소켓으로 입력받는 Source를 생성
   socket_sample_agent.sources.socket_sample_source.type=netcat
   socket_sample_agent.sources.socket_sample_source.bind=localhost
   socket_sample_agent.sources.socket_sample_source.port=44445

   # Sink 설정. 데이터를 최종적으로 logger에 입력
   socket_sample_agent.sinks.socket_sample_sink.type = logger

   # Channel 설정. 버퍼 방식을 memory로 설정함. 파일로도 가능!
   socket_sample_agent.channels.socket_sample_channel.type = memory
   socket_sample_agent.channels.socket_sample_channel.capacity = 1000
   socket_sample_agent.channels.socket_sample_channel.transactionCapacity = 100

   # Source와 Sink를 채널과 이어줌
   socket_sample_agent.sources.socket_sample_source.channels = socket_sample_channel
   socket_sample_agent.sinks.socket_sample_sink.channel = socket_sample_channel
   ```
   - 코드 설명
     - #Source, Sink, Channel 설정 : 우리가 넣은대로 진행이됨
     - #Source 설정. netcat을 통해 소켓으로 입력받는 Source를 생성 : 소켓에서 입력한 내용을 Source로 보냄. 그 소켓은 localhost의 44445번포트에 띄어질것
     - #Sink 설정. 데이터를 최종적으로 logger에 입력
     - 한개의 채널은 무조건 한개의 sink만 사용할수밖에 없음. 

### Agent 설정하기2(directory source)


## AWS
인스턴스 들어가서 아래 세개를 거의다룸
1. 인스턴스
   1. 인스턴스 시작 누르기
   2. 이름: 아무거나 입력(단, 영어와 숫자 하이픈(-), 언더바(_)만 가넝)
   3. 퀵스타트만 사용하면 됨
      - 아마존, 우분투 등이 있지만 초보자 입장에서 가장 사용하기 좋은게 우분투!
   4. 우분투 클릭을 하면 버전을 선택할 수 있음
      - 최신버전(22.04)하면 복습을 못함
      - 이에, 두번째꺼 20.04를 선택해야함
   5. 인스턴스 유형: 컴퓨터 하드웨어를 정하는 것으로 숫자가 크면 클수록 비싸고 좋은것
      - 보통 i3 large를 많이 사용(대략 한달에 18만원 정도가 나옴)
   6. 키페어: .pem파일 발급
      - 우린 지금 아무것도 없는데 인스턴스 유형을 할때 키페어 생성하면됨
      - 사람들마다 여러방식이 있는데, 인스턴스를 만들때마다 키페어를 생성하거나 그냥 모든 인스턴스를 하나의 키페어를 사용함
   7. 네트워크 설정
      - 기존 보안그룹 선택을 하면 아무것도 없어서 처음엔 그룹 생성 누르면 됨
      - 이것두 마음대로 선택하셈
   8. 스토리지 구성
      - 100GB로 설정
      - 만약 데이터가 많이 크지 않다 적당하게 쓸거다하면 20이나 50기가로 하면됨
   9. 끗!
2. 보안그룹
   
3. 탄력적 IP

## EFK
`(base) ubuntu@ip-172-31-11-147:~$`에서 시작

### Fluentd로 로그 파싱하고 보내기
#### fluentd 설치하기
1. Fluentd 설치
   ```
   sudo apt update
   sudo apt install build-essential -y
   ```
2. Ruby gem 설치
   ```
   sudo apt install rubygems -y
   sudo apt install ruby-dev -y
   sudo gem install fluentd --no-doc
   sudo gem install etc json oj webrick
   ```
3. fluentd directory 세팅
   - `fluentd --setup ./fluent`
4. fluentd 테스트
   - 아래 코드를 실행하면 새로운 서버 log가 실행됨
     - `fluentd -c ./fluent/fluent.conf -vv &`
   - 아래 코드를 실행하면 .test 나오는거 확인
     - `echo '{"json":"message"}' | fluent-cat debug.test`
5. Process종료
   - `pkill -f fluentd`

#### 실습용 log generator
1. Log Generator 설치
   - `mkdir loggen && cd loggen`
   - `wget https://github.com/mingrammer/flog/releases/download/v0.4.3/flog_0.4.3_linux_amd64.tar.gz`
3. (base) ubuntu@ip-172-31-11-147:~/loggen$ 에서 ls해서 아래 결과가 나오는지 확인
   - flog_0.4.3_linux_amd64.tar.gz
4. 압축 풀기
   ```
   tar -xvf flog_0.4.3_linux_amd64.tar.gz
   ./flog --help
   ```
5. ls해서 flog가 나오는 지 확인
6. Log 생성
   - `./flog -f json -t log -s 1m -n 1000 -o json-1.log -w &`
7. 이어서 log-1.json 파일을 복사
   - `cp json-1.log json-2.log`
   - `cp json-1.log json-3.log`
8. vi 에디터로 json-2.log 들어가기
   - `vi json-2.log`
   - `:`를 입력하면 명령어를 칠수 있음. 여기서 날짜 변경하기
   - `:%s/25\/Mar/24\/Mar/g`
9. json-3.log도 하기
   - `vi json-3.log`
   - `:%s/25\/Mar/23\/Mar/g`
10. apache log 만들기
   - 만약 나중에 json 형태로 바꾸지 않으면 이 아파치 모양으로 받음
   - `./flog -f apache_common -t log -s 1m -n 1000 -o apache-1.log -w &`
11. 이어서 apache-1.log 파일을 복사해 apache 2, 3만들기
   - `cp apache-1.log apache-2.log`
   - `cp apache-1.log apache-3.log`
12. `ls`를 통해 잘 있는지 확인
13. 아파치도 json처럼 날짜 바꿔주기

#### Fluentd로 로그 파일 읽기
- 로그로 필요한 정보를 아래처럼 등록해 할 수 있음
   <p align="center">
      <img src="../이미지/program down02.png">
   </p>

##### json 형식의 로그를 수집
- 대부분 특히 초보자들은 json로그의 형식을 따름
1. `vi fluent-json.conf`를 이용해 fluent 폴더 내 설정파일 생성
2. 아래 코드를 설정에 입력
      ```XML
      <source>
            @type tail
            tag log.json.*
            path /home/ubuntu/loggen/json-*.log
            pos_file positions-json.pos
            read_from_head true
            follow_inodes true

            <parse>
                     @type json
                     time_key datetime
                     time_type string
                     time_format %d/%b/%Y:%H:%M:%S %z
            </parse>
      </source>

      <match log.json.**>
            @type stdout
      </match>
      ```
3. 작성 완료후 아래 명령어를 실행
   - `fluentd -c ./fluent-json.conf -vv`

##### regex형식의 로그파일(아파치로 하는 경우)
- 정규식을 사용하기에 정규식을 확인하기(https://regex101.com/)
1. `vi fluent-regex.conf`를 이용해 fluent 폴더 내 섯정파일 생성
2. 아래 코드를 설정에 입력
      ```XML

      <source>
      @type tail
      tag log.apache.*
      path /home/ubuntu/loggen/apache-*.log
      pos_file positions-apache.pos
      read_from_head true
      follow_inodes true
      <parse>
         @type regexp
         expression /^(?<client>\S+) \S+ (?<userid>\S+) \[(?<datetime>[^\]]+)\] "(?<method>[A-Z]+) (?<request>[^ "]+)? (?<protocol>HTTP\/[0-9.]+)" (?<status>[0-9]{3}) (?<size>[0-9]+|-)/
         time_key datetime
         time_format %d/%b/%Y:%H:%M:%S %z
      </parse>
      </source>

      <match log.apache.**>
      @type stdout
      </match>
      ```
   - json형식과 달리 태그가 다름
3. 아래 명령어를 이용해 실행
   -`fluentd -c ./fluent-regex.conf -vv `

#### 필터링 하기
- 어떠한 특정한 값을 제거할 때 사용
- 로그 수집을 할 수 있도록 해보기
- 필터를 하면 position이 새로 생성됨
1. `vi fluent-regex.conf`에 새로 설정
   - 아래 코드 입력
      ```xml
      <source>
      @type tail
      tag log.json.*
      path home/ubuntu/loggen/json-*.log
      pos_file positions-json.pos
      read_from_head true
      follow_inodes true

      <parse>
         @type json
         time_key datetime
         time_type string
         time_format %d/%b/%Y:%H:%M:%S %z
      </parse>
      </source>

      <source>
      @type tail
      tag log.apache.*
      path home/ubuntu/loggen/apache-*.log
      pos_file positions-apache.pos
      read_from_head true
      follow_inodes true
      <parse>
         @type regexp
         expression /^(?<client>\S+) \S+ (?<userid>\S+) \[(?<datetime>[^\]]+)\] "(?<method>[A-Z]+) (?<request>[^ "]+)? (?<protocol>HTTP\/[0-9.]+)" (?<status>[0-9]{3}) (?<size>[0-9]+|-)/
         time_key datetime
         time_format %d/%b/%Y:%H:%M:%S %z
      </parse>
      </source>

      <filter log.**>
      @type grep
      <exclude>
         key status
         pattern /^[2][0-9][0-9]/
      </exclude> 
      #  <regexp>
      #    key status
      #    pattern /^[1345][01235][0-9]/
      #  </regexp>
      </filter>

      <match log.**>
         @type stdout
      </match>
      ```
2. 저장하고 나오기
3. ls를 해보면 positions가 있음 이에 기존의 positions을 없애줘야 다시 실행할수 있음
   - `rm psitions-*`
     - positions의 역할은 읽은 위치 정보를 기억함
     - 즉, 일반적으로 Fluentd는 로그 파일을 읽은 후 해당 파일의 상태(읽은 위치 등)를 추적하기 위해 이러한 포지션 파일을 사용. 따라서 Fluentd가 재시작되거나 다시 실행될 때도 마지막으로 읽은 위치에서 계속해서 로그를 읽을 수 있어 다읽은 경우 아무것도 나타나지 않는걸로 보임. 
     - 포지션 파일은 Fluentd가 실행되는 동안 생성되며, 필요할 때마다 업데이트됨. 만약 이전 포지션 파일이 더 이상 필요하지 않은 경우나 재시작 후 모든 로그 파일을 다시 읽어야 할 때는 해당 포지션 파일을 삭제한뒤 실행함면 다시 새로 생성됨!
4. 실행해보기
   - `fluentd -c ./fluent-regex.conf -vv `
- "filter"는 순서가 중요합니다. 만약 "match"보다 뒤에 오면 해당 "match"에는 적용되지 않습니다. "filter"끼리도 선언된 순서대로 적용됩니다.

### Opensearch(Elasticsearch)로 로그 저장하기
#### Opensearch 설치하기
- 엘라스틱서치는 파일안쪽의 텍스트를 빨리 찾아주는 기능
- 서치를 할때 RAM에서 가져오는게 HDD에서 가져오는것보다 훨빠름. 다만, 시작할때 통으로 가져오는 것이기에 용량이 크면은 조금 느려질 수 있음
- (base) ubuntu@ip-172-31-11-147:~/fluent$에서 하기
1. Opensearch 설치하기
   ```
   sudo apt update
   sudo apt install build-essential -y
   ```
2. `cd ~`로 홈으로 나오기
3. Opensearch 다운로드 및 환경 설정
   ```
   wget https://artifacts.opensearch.org/releases/bundle/opensearch/2.4.0/opensearch-2.4.0-linux-x64.tar.gz
   tar -xvf opensearch-2.4.0-linux-x64.tar.gz
   ```
4. 환경변수 등록
   - `vi ~/.bashrc`
   - 맨 아래 OPENSEARCH_HOME 등록
      ```
      # OPENSEARCH_HOME 
      export OPENSEARCH_HOME=/home/ubuntu/opensearch-2.4.0
      export PATH=$PATH:$OPENSEARCH_HOME/bin
      ```
   - 저장하고 나와서 `source ~/.bashrc`실행
   - `echo $OPENSEARCH_HOME`를 실행해서 잘 설치되었는지 확인

##### OpenSearch 시스템 세팅
이건 하지않음. 나중에 우린 스파크도 할거라서 그냥 참고용으로만 보기. 만약에 나중에 엘라스틱서치전용으로 컴퓨터를 하면은,, 하던가 정도?

##### 설정
(base) ubuntu@ip-172-31-11-147:~$에서 하기
1. opensearch.yml 파일을 열어주기
   - `vi $OPENSEARCH_HOME/config/opensearch.yml`
2. 네트워크 호스트와 OpenSearch 모드를 single-node로 설정
   1. Network안에서 network.host만 새로지정해주기
     - `network.host: 0.0.0.0`
       - 0.0.0.0의 의미는 어디서든 접근할 수 있음
   2. Discovery에서 맨아래 아래코드 넣기
     - `discovery.type: single-node`
3. 오픈서치 자바를 애들이 가지고 온 자바를 쓰게하기위해 아래 코드 실행해주기. 즉, 임시 환경변수가 새롭게 등록된다고 생각하면 됨. 껐다 키면 사라짐
   - `export OPENSEARCH_JAVA_HOME=$OPENSEARCH_HOME/jdk`
   - 만약 매번 등록하는게 귀찮으면 그냥 환경변수에 넣어주면 됨

##### plugin 설치하기
밖에서 가져온거를 내꺼에 끼워넣는것.
1. 플러그인 제거하기
   - 보안이 매우 빡세서 그냥 제거해주는게 편함
      ``` 
      $OPENSEARCH_HOME/bin/opensearch-plugin remove opensearch-security
      $OPENSEARCH_HOME/bin/opensearch-plugin remove opensearch-security-analytics
      ```
2. `ls $OPENSEARCH_HOME/plugins/`를 실행해 security 관련된게 전혀 없는 지 확인해봄
3. plugin 실행
   - `$OPENSEARCH_HOME/bin/opensearch`
4. 서버는 꺼지면 안되니 새로운 창 열어줘 (base) ubuntu@ip-172-31-11-147:~$를 키기
5. 실행 확인을 위해 OpenSearch의 작동 상황 확인
   - `curl -X GET http://localhost:9200`
   - 실행 결과 distribution이 opensearech로 나오는 것만 확인!

#### Fluentd - OpenSearch 연동
1. Opensearch 서버로 Fluentd로 수집한 로그를 보내기위해 plugin 을 설치
   - `sudo fluent-gem install fluent-plugin-opensearch`
   - 오류가 남. 왜냐면 버전이 바뀌어서..ㅎㅎ 아래 코드로 다운그레이드해주기
      - `sudo gem install faraday -v 2.8.1`
      - `sudo gem install fluent-plugin-opensearch -v 1.1.0`
2. Fluentd와 Openshearch 이어주기
   - `cd fluent`
   - `vi fluent-opensearch.conf`
   - 아래 내용 기입
      ```xml
      <source>
            @type dummy
            tag dummy
            dummy {"hello":"world"}
      </source>

      <match dummy>
            @type opensearch
            host 172.31.11.147 #인스턴스 프라이빗 IPv4 기입
            port 9200
            index_name fluentd-test
      </match>
      ```
3. `fluentd -c ./fluent-opensearch.conf -vv`로 실행 잘되었는지 확인해보기   
   - 파란색 글씨가 올라오면서 buffer가 잘 쌓이는지 보기
4. 새로운 창 키고 ubuntu접속
   - `curl -XGET http://localhost:9200/_cat/indices?v` 실행
   - index가 잘 나오는지 확인
5. 버퍼 나오는 3번 창 꺼주기
   - `vi fluent-opensearch.conf`실행
   - 기존에 있는거 싹다 지워주기
     - 영어 d를 꾹누르면 한줄씩 다지워줌
     - 아래 내용으로 다시 채우기
         ```xml
         <source>
         @type tail
         tag log.json.*
         path /home/ubuntu/loggen/json-*.log
         pos_file positions-json.pos
         read_from_head true
         follow_inodes true

         <parse>
            @type json
            time_key datetime
            time_type string
            time_format %d/%b/%Y:%H:%M:%S %z
         </parse>
         </source>

         <source>
         @type tail
         tag log.apache.*
         path /home/ubuntu/loggen/apache-*.log
         pos_file positions-apache.pos
         read_from_head true
         follow_inodes true
         <parse>
            @type regexp
            expression /^(?<client>\S+) \S+ (?<userid>\S+) \[(?<datetime>[^\]]+)\] "(?<method>[A-Z]+) (?<request>[^ "]+)? (?<protocol>HTTP\/[0-9.]+)" (?<status>[0-9]{3}) (?<size>[0-9]+|-)/
            time_key datetime
            time_format %d/%b/%Y:%H:%M:%S %z
         </parse>
         </source>

         <match log.apache.**>
         @type opensearch
         host 172.31.11.147
         port 9200
         index_name apache-log
         </match>

         <match log.json.**>
         @type opensearch
         host 172.31.11.147
         port 9200
         index_name json-log
         </match>
         ```
   - 포시션 파일 삭제
     - `rm -rf position*` 
   - 다하고 `fluentd -c ./fluent-opensearch.conf -vv`실행!
6. 4번창으로 돌아와서 `curl -XGET http://localhost:9200/_cat/indices?v`실행
   - apache와 json가 잘 들어와있는지 확인
- json.log와 apache.log를 stream에 담아서 보낼거임. 이때 바가지(buffer)가 필요함
- buffer에다가 log가 채워지기를 기다려야함. 즉, 버퍼링이라 생각하면 됨

#### Timeformat 으로 index 지정하기
시간의 흐름과 같은 log를 확인하고 싶을때도 사용할 수 있음
1. 위쪽 5번창 꺼주기(ctrl+c)
2. 이후 `rm positions-*`실행
3. `vi fluentd-opensearch.conf`로 코드 수정
   - 이거 뭔가 안함. 그래서 다른걸로 ㄱㄱ
4. `vi fluent-opensearch-json.conf` 실행
   - 아래 코드 입력
      ```xml
      <source>
      @type tail
      tag log.json.*
      path /home/ubuntu/working/fluent/logs/json-*.log
      pos_file positions-json.pos
      read_from_head true
      follow_inodes true

      <parse>
         @type json
         time_key datetime
         time_type string
         time_format %d/%b/%Y:%H:%M:%S %z
      </parse>
      </source>


      <match log.json.**>
      @type opensearch
      ⭐hosts 172.31.11.147:9200
      logstash_format true
      ⭐logstash_prefix json-timelog
      include_timestamp true
      ⭐time_key datetime
      ⭐time_key_format %d/%b/%Y:%H:%M:%S %z
      </match>
      ```
5. `fluentd -c ./fluent-opensearch-json.conf -vv`로 실행해서 json.log만 받기
6. `curl -XGET http://localhost:9200/_cat/indices?v`를 실행해서 timelog가 잘 들어왔는지 확인

### Open Dashboard(Kibana)로 로그 시각화하기
#### Open Dashboard 설치하기
1. Open Dashboard 설치하기
   - `wget https://artifacts.opensearch.org/releases/bundle/opensearch-dashboards/2.4.0/opensearch-dashboards-2.4.0-linux-x64.tar.gz`
   - `tar -zxf opensearch-dashboards-2.4.0-linux-x64.tar.gz`

2. 환경변수 등록
   - `vi ~/.bashrc`
      ```xml
      # OPENSEARCH_DASHBOARDS_HOME
      export OPENSEARCH_DASHBOARDS_HOME=/home/ubuntu/opensearch-dashboards-2.4.0
      export PATH=$PATH:$OPENSEARCH_DASHBOARDS_HOME/bin
      ```
   - `source ~/.bashrc`실행
   - `echo $OPENSEARCH_DASHBOARDS_HOME`으로 확인

3. 설정변경
   - `vi $OPENSEARCH_DASHBOARDS_HOME/config/opensearch_dashboards.yml`
   - 기존에 있는 애들 전부다 #으로 주석처리해주고 아래 코드만 집어넣기
      ```xml
      server.host: 0.0.0.0 # 또는 "ec2 public address"
      server.port: 5601
      opensearch.hosts: [http://172.31.11.147:9200]
      opensearch.ssl.verificationMode: none
      opensearch.username: kibanaserver
      opensearch.password: kibanaserver
      ```

4. 보안 플러그인 제거
   - `$OPENSEARCH_DASHBOARDS_HOME/bin/opensearch-dashboards-plugin remove securityAnalyticsDashboards`
   - `$OPENSEARCH_DASHBOARDS_HOME/bin/opensearch-dashboards-plugin remove securityDashboards`
5. 오픈서치 서버 실행!
   - `$OPENSEARCH_DASHBOARDS_HOME/bin/opensearch-dashboards`를 실행해서 대시보드창 키기
   - 맨처음부터 지금까지 켜져있는 서버창과 대시보드 창이 같이 있어야함
6. 구글새탭에 `퍼블릭 aws dns:5601`를 입력

#### Open Dashboard 에서 인덱스 패턴 생성하기
새로운 인덱스를 만들기 전에 항상 새로고침 해주는건 권장함

#### Open Dashboard 에서 인덱스 패턴 생성하기
##### 인덱스 만들기(json-timelog*)
1. 왼족 햄버거 누르기
2. Management -> Stack Management
3. Create index pattern
4. json-timelog* 클릭후 timestamp(시계열)지정
5. refresh해주고 다시 Stack Management클릭하면 인덱스가 나오는 것을 볼 수 있음

#### Open Dashboard에서 검색하기

##### discover
- timelog와 같이 시계열 데이터의 경우에는 자동으로 시각화해서 보여줌
- 달력 옆에 클릭하면 Absolute, Relative가 나옴
  - Absolute: 절대적인시간
  - Relative: 현재시간 기준 상대적인 시간
  
##### visualization(시각화)
1. Create new visulization
2. 원하는 데이터 선택
3. 개수를 보고싶을때 terms만 기억하면 됨
4. 이것저것 만져보고 오른쪽 위 save 클릭!

##### Dashboard
시각화의 결과를 기반으로 간단한 대시보드를 만ㄷ르 수 잇음
- 특히 시각화해서 저장한 파일을 여러개 가져와서 나열할수 있음
- 다른사람들과 공유도 할 수 있음(PDF, PNG)
  - SHARE : 다름사람에게 대시보드를 공유하고 싶을때, 

## Spark
`(base) ubuntu@ip-172-31-11-147:~$ conda activate spark-env`를 통해 (spark-env)환경에서 시작함

### 스파크 설치
1. 스파크 설치
   - `wget https://archive.apache.org/dist/spark/spark-3.2.4/spark-3.2.4-bin-hadoop3.2.tgz`
   - `tar xvfz spark-3.2.4-bin-hadoop3.2.tgz`
2. 폴더의 이름 바꿔주기
   - `mv spark-3.2.4-bin-hadoop3.2/ spark-3.2.4/`
3. 환경변수 설정
   - `vi ~/.bashrc `
   - 아래 코드 등록
      ```
      # SPARK
      export SPARK_HOME=/home/ubuntu/spark-3.2.4
      export PATH=$PATH:$SPARK_HOME/bin
      ```
   - 저장후 나오기
   - `source ~/.bashrc`실행
   - `echo $SPARK_HOME`로 잘 설치되었는지 확인
4. `conda activate spark-env`를 실행해서 다시 (spark-env)만들어주기
5. `pip install pyspark==3.2.4` 설치
6. `which python`실행 후 나온 결과 나중에 사용하니 메모!
   - /home/ubuntu/miniconda3/envs/spark-env/bin/python
   - 아래처럼 사용할거임
      ```xml
      export PYSPARK_PYTHON=/home/ubuntu/miniconda3/envs/spark-env/bin/python
      export PYSPARK_DRIVER_PYTHON=/home/ubuntu/miniconda3/envs/spark-env/bin/python
      ```
7. spark 실행환경을 조절할수 있는파일 열기
   - `cp $SPARK_HOME/conf/spark-env.sh.template $SPARK_HOME/conf/spark-env.sh`
   - `vi $SPARK_HOME/conf/spark-env.sh`
   - 6번에 메모한 애들 맨 아래에 집어넣기
8. `pyspark`실행해서 spark version 3.2.4나오는지 확인
9. `python`에서 에러없는지 확인하고 (spark-env)환경으로 돌아오기
10. Web UI 주소 변경
   - `cp $SPARK_HOME/conf/spark-defaults.conf.template $SPARK_HOME/conf/spark-defaults.conf`
   - `vim $SPARK_HOME/conf/spark-defaults.conf`
   - 맨 아래에 아래 코드 집어넣기
      - `spark.driver.host 0.0.0.0`
   - 저장후 나오기
11. `pyspark` 실행해서 스파크 서버 켜주기
12. 구글 탭에 `aws 퍼블릭dns:4040`을 입력해 pysparkshell이 잘 나오는지 확인
13. 쥬피터 노트북도 (spark-env)환경에서 `jupyter notebook --allow-root`를 실행해주기
    - 앞으로 모든 코드입력 및 데이터 분석은 spark juypter notebook에서 할거임
    - 구글 탭에 `aws 퍼블릭dns:8888`해서 쥬피터 창 켜주기


### spark_jupyter 실행법
항상 주피터 환경에서 실행!
1. bash에 접속 후 `cd .`
2. `ssh -i "V-lab.pem" ubuntu@ec2-3-114-30-206.ap-northeast-1.compute.amazonaws.com`로 (base)환경 들어가기
3. `conda activate spark-env`를 통해 (spark-env)가상환경 들어가기
4. `pyspark`로 스파크 서버 키기
5. 구글 탭에  `aws 퍼블릭dns:4040`을 입력해 스파크 홈페이지키기
6. 새로운 Bash창 오픈
7. 1~3번과정 다시하기
8. (spark-env)환경에서 `jupyter notebook --allow-root`실행
9. 구글 탭에  `aws 퍼블릭dns:8888`을 입력해 쥬피터노트북키기cd