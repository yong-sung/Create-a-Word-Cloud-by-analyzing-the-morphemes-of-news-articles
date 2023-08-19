import requests
import re
import xml.etree.ElementTree as ET

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
    
print("뉴스제목: ",title_list[0:3])
print("뉴스요약: ",description_list[0:3])