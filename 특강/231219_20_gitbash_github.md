# GIThub

리눅스의 오픈소스가 너무많이 나와 오히려 지옥이 되었다고 할 수 있음. 이에 리눅스가 GIT을 만들기 시작해서 리눅스 뿐만아니라 수많은 소프트웨어 소스코드가 관리하고 있음. 
> 즉, git은 대표적인 버전 관리 시스템!

* git의 3대 목적
  1. 버전관리(version)
  2. 백업(backup)
  3. 협업(collaborate)

## 1. 버전관리(version)
- 일반 파일의 이름으로 버전관리를 할시 어떠한 내용이 수정되고 안에 내용을 볼수 없으나,
- 깃허브로 관리를 하게되면 바로 수정된 과정을 볼수 있어 버전관리를 하기에 용이하다.  
  - 버전만 생성하면 히스토리를 통해 이력을 확인 할 수 있음
  - 복수의 파일(텍스트, 이미지 등)의 변경사항을 추적할 수 있음
- 클릭한번으로 과거의 상태로 돌릴 수 있음
  
## 2. 백업(backup)
- 컴퓨터는 언제 고장나거나 사라질지 모름... 그때 컴퓨터 안에 있을 데이터를 영원히 보호하기 위해 
- 원격저장소에(github.com)에 데이터를 백업

## 3. 협업(collaborate)
- 백업을 한 순간 이미 협업의 준비는 끝
- 원격저장소(github.com)에 나의 데이터를 저장(push)하면 다른 사랑이 당겨와서(pull) 작업하고 작업한 파일을 다시 원격저장소에 push함. 이렇게 상호작용을 시작

## git 명령어
### (1) `git init`
git으로 코드 관리를 시작하는 명령어
```bash
$ git init
```
- 디렉토리 경로는 git으로 코드 관리를 하고 싶은 폴더로 이동한 후 명령어를 입력해야 한다.

- `(master)` : 현재 브랜치(branch)명
    > `git init`를 실행하니 프롬프트의 현재 경로 옆에 `(master)`가 추가된 것을 확인할 수 있다. `(master)` 앞에는 현재 디렉토리 경로로 사용자가 `git init`을 시작한 폴더 경로에 따라 다를 수 있다.
    ```bash
    user@OS-2107250526 MINGW64 ~/kdt-data-33/github/test (master)
    $
    ```
- `git init`를 실행하면 현재 폴더에 `.git`이라는 폴더가 생성된다.
  - `.git` : git의 관리와 관련된 파일


### (2) `git status`
현재 상태를 출력(Git에게 현재 상태를 물어봄)
1. `git init` 직후 `git status` 실행
```
$ git status
On branch master

No commits yet

nothing to commit (create/copy files and use "git add" to track)
```
`git init` 직후 `git status` 명령어를 입력하니 위와 같이 출력된다. 
> 현재 master라는 이름의 branch에 있으며
> 
> 아직 commit이 없음
>
> commit할 것이 없음(파일을 만들거나 복사하고, `git add`를 통해 추적해봐)

1. 현재 폴더에서 git에 관리할 파일을 만들어 준다.
```bash
$ touch a.txt
```

1. 파일 생성 후 `git status` 실행
```bash
$ git status
On branch master

No commits yet

Untracked files: 
  (use "git add <file>..." to include in what will be committed)
```
파일을 생성후 `git status` 실행하니 마지막 문장이 바뀌어서 출력되었다.
> 현재 master라는 이름의 branch에 있으며
>
> 아직 commit이 없음
>
> 추적되지 않은 파일:
> (`git add <파일명>`을 사용해서 commit될 것에 포함시켜라)


### (3) `git add [파일명]`
- `git add .` : 현재 폴더의 모든 변경사항 Stage Area에 추가

1. `git add a.txt` 실행
   - a.txt 파일을 Stage Area에 추가
   - 파일을 commit하기 위해 먼저 파일이 Stage Area에 존재해야 한다.
```bash
$ git add a.txt
```
2. `git add a.txt` 실행 후 `git status` 실행
```bash
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   a.txt
```
파일을 Stage Area에 추가하고 `git status` 실행하니 마지막 문장이 바뀌어서 출력되었다.

> 현재 master라는 이름의 branch에 있으며
>
> 아직 commit이 없음
>
> commit 될 수 있는 변화 존재:
>   (`git rim --cached <파일명>`을 사용해서 unstage 해봐)
>       새로운 파일 : a.txt

### (4) `git commit -m "메시지"`
`commit`은 **버전을 생성하는 것**이다. 
- 작업물의 변화된 내용을 기록하는 것이다. 
- `-m` 옵션은 message의 약자
- `"메시지"`에 들어갈 내용은 버전을 기록하면서 어떤 내용이 변화되었는지 남기면 좋다.

1. 처음으로 `commit`을 시도할 경우
```bash
$ git commit -m "Fisrt commit"
Author identity unknown

*** Please tell me who you are.

Run

git config --global user.email "tmdwn7733@gmail.com"
git config --global user.name "j"
```
처음 `commit`을 시도하는 경우 git이 사용자가 누군지 물어보는 내용이 나온다. " "안의 내용은 사용자가 설정할 본인의 이메일과 이름을 적으면 된다. 이메일은 github와 연결할 이메일로 적는 것이 좋다.
>
> 작자미상(신원을 알 수 없는 작성자)
>
> 당신이 누군지 알려달라.
>
> 아래의 명령어를 실행하라.
>
> 전역의(global) 사용자 이메일을 `"이메일주소"`로 설정
> 
> 전역의 사용자 이름을 `"사용자 이름"`으로 설정

2. `git config`로 이메일 주소와 사용자 이름을 설정
```bash
git config --global user.email "tmdwn7733@gmail.com"
git config --global user.name "j"
```
3. `git commit`
   - `commit`을 하면서 "First commit"이라고 내용을 담는다.
    ```bash
    $ git commit -m "Fisrt commit"
    ```
    Repository에 파일이 commit되면 아래와 같이 출력된다.
   - 사용자의 위치경로 등에 따라 내용이 다를 수 있다.
    ```bash
    [master 216b26f] First commit
     1 file changed, 0 insertions(+), 0 deletions(-)
     create mode 100644 a.txt
    ```
    - 만약 `-m` 옵션으로 메시지를 입력하지 않고, 에디터창으로 넘어가고 싶다면 `git commit`만 입력한다.
    ```bash
    $ git commit
    ```

    > 아래처럼 commit message를 입력하라는 에디터창이 나온다. 편집모드(`i`)에서 commit message를 입력하고 `Esc`를 눌러서 편집모드에서 나간다. `wq`를 입력하여 저장하고 종료한다.
    ```bash
    
    # Please enter the commit message for your changes.

    # Lines starting with '#' will be ignored, and an empty message aborts the commit.

    # On branch master
    #
    # Initial commit
    #
    # Changes to be committed:
    # new file: test.txt
    ```

### (5) `git config`
git에 관한 설정
- 전역으로(global) 사용자의 이메일을 설정
```bash
$ git config --global user.email "이메일주소"
```
- 설정값 확인
```bash
$ git config --global user.email
```

### (6) `git log`
현재까지의 `commit`을 출력
- `git log`를 실행하면 작성자, 날짜, commit message를 확인할 수 잇다.
```bahs
$ git log
commit bab6792111fa2c3eed036e7ef11401c4a5425b15 (HEAD -> master)
Author: silverA-01 <silvermare01@gmail.com>
Date:   Tue Dec 19 16:31:59 2023 +0900

    First commit
```
- `git log --oneline`를 실행하면 한 줄로 log가 출력된다.
```bash
$ git log --oneline
bab6792 First commit

```

### (7) `git remote`
- `git remote add <저장소 이름> <저장소 주소>` : git에게 원격저장소(remote)를 추가(add)하라는 명령어


### (8) 그 외 커맨드
- 커맨드 편집
   - `git commit --amend` : 직전 커맨드 수정하기 위해 직전 커맨드 편집 모드 실행

- add status 편집
   - `git reset HEAD 파일명`: add한 파일을 워킹 디렉토리에 다시 내리기(staging area -> working directory)
   - `git reset HEAD .` : 모든 파일의 스테이징 취소하고 워킹 디렉토리로 되돌리기

- commit status 편집
   - `git reset --soft HEAD^` : 커밋 취소 후 스테이징 영역으로 복귀
   - `git reset --mixed HEAD^` : 커밋 취소 후 워킹 디렉토리 영역으로 복귀(언스테이징)
   - `git reset --hard HEAD^` : 커밋 취소 + 워킹 디렉토리 영역 복귀 + 변경 사항 삭제 


## 복습
user@J MINGW64 ~
$ mkdir practice 
> 연습폴더 만들기

user@J MINGW64 ~
$ cd practice 
> 연습폴더로 이동

user@J MINGW64 ~/practice
$ git init
> git 시작

user@J MINGW64 ~/practice (master)
$ git status  
> 현재 git 상태 물어보기. 상태어때?
```
On branch master

No commits yet

nothing to commit (create/copy files and use "git add" to track)

-> 아무것도 없고 한것도 없어.
```
user@J MINGW64 ~/practice (master)
$ code .    
> 현재 해당 폴더 열어주기   
> 열린 vs폴더에 readme.md만들고 자기소개 만들고 저장

user@J MINGW64 ~/practice (master)
$ git status
```
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        readme.md -> 여기선 빨간색으로 파일명이 뜲

nothing added to commit but untracked files present (use "git add" to track)
```
user@J MINGW64 ~/practice (master)
$ git add readme.md
> 이걸 하고난 뒤 git status하면 파일명이 초록색으로 바뀜

user@J MINGW64 ~/practice (master)
$ git commit -m "First commit" 
> 버전 저장, 즉, 스냅샷 찍는다 생각
```
[master (root-commit) be67c1b] First commit
 1 file changed, 1 insertion(+)
 create mode 100644 readme.md
 ```
user@J MINGW64 ~/practice (master)
$ git log 
> 지금까지의 기록 확인
```
commit be67c1bb83e7e34572c85d8ee48dc29565628bbe (HEAD -> master)
Author: J <tmdwn7733@gmail.com>
Date:   Wed Dec 20 10:47:05 2023 +0900

    First commit
```
user@J MINGW64 ~/practice (master)
$ git status
```
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   readme.md -> 파일을 수정하고 저장한뒤 git 상태를 물으면 modified란 말이 앞에 붙음

no changes added to commit (use "git add" and/or "git commit -a")
```
user@J MINGW64 ~/practice (master)
$ git diff
> 내가 무얼 수정했는지 구체적으로 설명해줌
> > git add [파일명] 을 지정하면 결과가 안뜸. 파일명이 빨간색일때 설명해줌 
```
diff --git a/readme.md b/readme.md
index 1ddadd9..d3ed449 100644
--- a/readme.md
+++ b/readme.md
@@ -1 +1,4 @@
 # 자기소개
+
+## 이름
+한승주
\ No newline at end of file
```
user@J MINGW64 ~/practice (master)
$ git add readme.md
> commit하기 위해 준비하기  
> git status 하면 파일명이 다시 초록색으로 뜸

user@J MINGW64 ~/practice (master)
$ git commit -m "second commit"
> 버전 저장, 스냅샷 찍기
```
[master 71dc565] second commit
 1 file changed, 3 insertions(+)
 ```
 user@J MINGW64 ~/practice (master)
$ git log
> commit 이력 보기
```
commit 71dc565bcbdfd482213950a919bde16775b372db (HEAD -> master)
Author: J <tmdwn7733@gmail.com>
Date:   Wed Dec 20 11:18:40 2023 +0900

    second commit

commit be67c1bb83e7e34572c85d8ee48dc29565628bbe
Author: J <tmdwn7733@gmail.com>
Date:   Wed Dec 20 10:47:05 2023 +0900

    First commit
```
user@J MINGW64 ~/practice (master)
$ git log --oneline
> 예쁘게 요약해줘
```
71dc565 (HEAD -> master) second commit
be67c1b First commit
```

user@J MINGW64 ~/practice (master)
$ git checkout be67c1b
> first commit을 한 과거로 돌아가고 싶을때 사용
> 하지만 과거를 맘대로 바꾸는게 위험한 것처럼 조심해야함

user@J MINGW64 ~/practice ((be67c1b...))
$ git checkout master
> 현실세계로 돌아가고 싶을때 
```
Previous HEAD position was be67c1b First commit
Switched to branch 'master'
```

## github 실습
- github 회원가입

user@J MINGW64 ~/practice (master)
$ git remote add origin https://github.com/tmdwn7733/practice.git
> github에서 새로 생성한 페이지 링크 복붙해서 넣음
> origin이라는 이름으로 등록을 하는 거
> 앞으로 원격으로 이 장소에 백업할거야라는 느낌

user@J MINGW64 ~/practice (master)
$ git remote
origin

user@J MINGW64 ~/practice (master)
$ git remote -v
> 상세 설명
```
origin  https://github.com/tmdwn7733/practice.git (fetch)
origin  https://github.com/tmdwn7733/practice.git (push)
```
user@J MINGW64 ~/practice (master)
$ git push origin master
> git 브라우저가 바로뜸
```
info: please complete authentication in your browser...
Enumerating objects: 18, done.
Counting objects: 100% (18/18), done.
Delta compression using up to 8 threads
Compressing objects: 100% (10/10), done.
Writing objects: 100% (18/18), 1.57 KiB | 5.00 KiB/s, done.
Total 18 (delta 3), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (3/3), done.
To https://github.com/tmdwn7733/practice.git
 * [new branch]      master -> master
```

### 깃 허브 프로젝트 꾸미는법
1. 내 tmdwn7733에 들어가서 code눌러서 downloadZIP을 클릭후 다운
2. git bash 이용
      
   1) git clone https://github.com/sooz-developer/sooz-developer.git
   2) git add README.md
   3) git commit -m "주석 해제"
   4) git push origin main

- user에 있는 내 tmdwn7733폴더 안 readme.md 파일을 클릭해서 작업한다 생각해 보기

user@J MINGW64 ~
$ git clone https://github.com/tmdwn7733/tmdwn7733.git
```
Cloning into 'tmdwn7733'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (3/3), done.
```
user@J MINGW64 ~
$ cd tmdwn7733/
user@J MINGW64 ~/tmdwn7733 (main)
$ 
> 내 tmdwn7733프로젝트에 들어오게됨


## 최종 실습

### 파일 올리기
user@J MINGW64 ~
$ ^C

user@J MINGW64 ~
$ mkdir wordchain

user@J MINGW64 ~
$ cd wordchain/

user@J MINGW64 ~/wordchain
$ git init
Initialized empty Git repository in C:/Users/user/wordchain/.git/

user@J MINGW64 ~/wordchain (master)
$ code .

user@J MINGW64 ~/wordchain (master)
$ ls
readme.md

user@J MINGW64 ~/wordchain (master)
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        readme.md

nothing added to commit but untracked files present (use "git add" to track)

user@J MINGW64 ~/wordchain (master)
$ git add readme.md

user@J MINGW64 ~/wordchain (master)
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   readme.md


user@J MINGW64 ~/wordchain (master)
$ git commit -m "add readme.md"
[master (root-commit) d2d5c3b] add readme.md
 1 file changed, 4 insertions(+)
 create mode 100644 readme.md

user@J MINGW64 ~/wordchain (master)
$ git log
commit d2d5c3b81bd4ee72bc17eda074783c1e5faaf771 (HEAD -> master)
Author: J <tmdwn7733@gmail.com>
Date:   Wed Dec 20 16:44:45 2023 +0900

    add readme.md

user@J MINGW64 ~/wordchain (master)
$ git remote

user@J MINGW64 ~/wordchain (master)
$ git remote add origin https://github.com/tmdwn7733/wordchain.git

user@J MINGW64 ~/wordchain (master)
$ git remote -v
origin  https://github.com/tmdwn7733/wordchain.git (fetch)
origin  https://github.com/tmdwn7733/wordchain.git (push)

user@J MINGW64 ~/wordchain (master)
$ ^C

user@J MINGW64 ~/wordchain (master)
$ git push origin master
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 251 bytes | 1024 bytes/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/tmdwn7733/wordchain.git
 * [new branch]      master -> master

user@J MINGW64 ~/wordchain (master)
$

### 내 팀원이 올렸으면 이제 내가 차이나는 만큼만 다시 가져와야함

0. git pull origin master
1. 파일저장
2. git add README.md
3. git commit -m "메시지 쿵쿵따"
4. git push origin master

user@J MINGW64 ~/wordchain (master)
$ git pull origin master
> 내 동료가 추가로 작성한 데이터를 가져오기
```
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 3 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), 321 bytes | 6.00 KiB/s, done.
From https://github.com/tmdwn7733/wordchain
 * branch            master     -> FETCH_HEAD
   d2d5c3b..7f4aad5  master     -> origin/master
Updating d2d5c3b..7f4aad5
Fast-forward
 readme.md | 1 +
 1 file changed, 1 insertion(+)
```

### 폴더/파일 삭제하는법
0. git rm -rf {파일 및 폴더명} : 모두 삭제
1. git rm -r --cached {파일 및 폴더명} : 원격 저장소에 있는것만 삭제
2. git commit -m "commit 내용"
3. git push -u origin master