from konlpy.tag import Kkma, Komoran, Okt

okt = Okt()

text = '일잘러를 위한 파이썬과 40개의 작품들 형태소 분석방법 입니다.'

명사_list = []
for 명사 in okt.nouns(text):
    if len(명사) > 1: # 한 글자 초과인 경우에만
        명사_list.append(명사)
        
print("명사:",명사_list)