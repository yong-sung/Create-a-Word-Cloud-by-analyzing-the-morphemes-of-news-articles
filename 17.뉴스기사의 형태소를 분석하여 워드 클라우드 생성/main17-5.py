import requests
import re
import xml.etree.ElementTree as ET
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud

okt = Okt() # 한국어 형태소 분석을 위한 인스턴스

# 제외하고자 하는 단어들 리스트
excluded_words = ['뉴스', '연합뉴스', '전체', '콘텐츠', '보기', '서울', '조선일보', '동아일보', '매일경제', '노컷뉴스', '한겨레', '방송', '프티', '한국어', '위기']


url = 'https://news.google.com/rss?hl=ko&gl=KR&ceid=KR:ko'

headers = {
    'User-Agent': 'Mozilla/5.0',
    'Content-Type': 'text/html; charset=utf-8'
}

response = requests.get(url, headers=headers) # 해당 URL에서 데이터를 가져옴

root_element = ET.fromstring(response.text) # XML 형식의 데이터를 파싱해 파이썬에서 다룰 수 있는 구조로 변환(트리 형태로 구성돼 있어, 트리의 최상위 요소가 'root_element' 변수에 저장)
iter_element = root_element.iter(tag="item")

title_list = []
description_list = []
for element in iter_element:
    title_list.append(element.find("title").text)
    hangul = re.compile('[^ ㄱ-ㅣ가-힣]+') # 한글만 추출
    description = element.find("description").text
    description_list.append(hangul.sub("",description))
    
명사_list = []
for title in title_list:
    for 명사 in okt.nouns(title):
        if len(명사) > 1 and 명사 not in excluded_words: # 길이가 1보다 크고, 'excluded_words'에 포함되지 않는 명사만 추가
            명사_list.append(명사)
            
for description in description_list:
    for 명사 in okt.nouns(description):
        if len(명사) > 1 and 명사 not in excluded_words:
            명사_list.append(명사)
            
명사_빈도수_list = Counter(명사_list) # '명사_list'에서 각 명사의 빈도수를 계산해 '명사_빈도수_list'에 저장

wc = WordCloud(font_path="gulim", width=400, height=400, scale=2.0, max_font_size=250)
gen = wc.generate_from_frequencies(명사_빈도수_list)
wc.to_file(r'17.뉴스기사의 형태소를 분석하여 워드 클라우드 생성\뉴스_워드클라우드.png')