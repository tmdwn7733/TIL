# 크롤링 코드

# pip.install은 외부에서 추가적으로 도구를 설치하기 위한것

# 웹브라우저를 바로 뜨게 만드는 명령어
import webbrowser

webbrowser.open('https://finance.naver.com/sise/')

'''
 kospi.py
'''
import requests 
from bs4 import BeautifulSoup

# pip install requests beautifulsoup4 를 먼저 설치해야함. 
# 도구 2개(requests, beautifulsoup4)가 들어가있음

URL = 'https://finance.naver.com/sise/'

# 네이버 증권에 접속하여 전체 페이지를 다운
# 여기서 request는 요청하다라는 것으로 요청함으로써 우리가 원하는 정보를 얻음
page = requests.get(URL)

# Parsing (구문분석/해석)_이걸 이제부터 해석하고 조금있다가 내가 필요하다고 말하면 줘
data = BeautifulSoup(page.text, 'html.parser')

# 코스피 전체 지수 데이터를 찾아 내기
# 찾아낼때 이름을 바로 찾거나 이름을 못찾으면 [F12 -> COPY -> COPY SELECT]를 눌러 이름주소 찾기
kospi = data.select_one('#KOSPI_now')

# 찾은 데이터를 출력
# .text는 그중 우리가 원하는 숫자만 출력해서 보여줌
print(kospi.text)

'''
lotto-api.py
'''
import requests

URL = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1096'

data = requests.get(URL).json()

print(data, type(data))

# dictionary라는 것으로 단어가 있고 듯이 따라오는 저장방법으로 키와 벨류로 저장되는거랑 비슷하는데 { key : value }

# 대괄호를 사용하면 키를 사용해 꽂아서 돌리는 것처럼 그중 원하는 데이터만 마지막에 출력할 수 있음
print(data['firstWinamnt'])

# url만 봐도 끝에 =main으로 하면 gui버전으로 
# =getLottoNumber&drwNo=1096으로 하면 api버전으로 나오게 동양복권이 세팅함

'''
telegram.py
'''

#웹 세상은 결국 요청은 url로 응답은 문서한장으로 

import requests

# 내 텔레그램 봇에 대한 토큰_봇 정보
TOKEN = '6481788936:AAHAXQ2wGFQD4WSgeIXt5ePQgvZWz7odz5I'

# 근데 여기서 getme가 정말 중요한데 이 의미가 어찌보면 텔레그램이 나에대한 결과를 주는 것을 볼 수 있음
'https://api.telegram.org/bot6481788936:AAHAXQ2wGFQD4WSgeIXt5ePQgvZWz7odz5I/getMe'

# 내 정보를 알아낼 수 있는 실시간 업데이트 URL
'https://api.telegram.org/bot6481788936:AAHAXQ2wGFQD4WSgeIXt5ePQgvZWz7odz5I/getUpdates'

# 내 정보
MY_ID = '6965081843'

# 봊정보와 내 정보를 알고 있으면 봇이 나에게 정보를 보낼수 있음
URL = 'https://api.telegram.org/bot6481788936:AAHAXQ2wGFQD4WSgeIXt5ePQgvZWz7odz5I/sendMessage?chat_id=6965081843&text='
message = '안녕하세요'

requests.get(URL + message)