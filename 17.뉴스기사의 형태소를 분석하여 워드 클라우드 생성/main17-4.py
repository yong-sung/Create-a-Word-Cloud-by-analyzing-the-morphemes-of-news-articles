import requests
import re
import xml.etree.ElementTree as ET
from konlpy.tag import Okt
from collections import Counter

okt = Okt()

url = 'https://news.google.com/rss?hl=ko&gl=KR&ceid=KR:ko'

headers = {
    'User-Agent': 'Mozilla/5.0',
    'Content-Type': 'text/html; charset=utf-8'
}

response = requests.get(url, headers=headers)

root_element = ET.fromstring(response.text)
iter_element = root_element.iter(tag="item")

title_list = []
description_list = []
for element in iter_element:
    title_list.append(element.find("title").text)
    hangul = re.compile('[^ ㄱ-ㅣ가-힣]+') # 한글만 가져옴
    description = element.find("description").text
    description_list.append(hangul.sub("",description))
    
명사_list = []
for title in title_list:
    for 명사 in okt.nouns(title):
        if len(명사) > 1:
            명사_list.append(명사)
            
for description in description_list:
    for 명사 in okt.nouns(description):
        if len(명사) > 1:
            명사_list.append(명사)
            
명사_빈도수_list = Counter(명사_list)
print(명사_빈도수_list)