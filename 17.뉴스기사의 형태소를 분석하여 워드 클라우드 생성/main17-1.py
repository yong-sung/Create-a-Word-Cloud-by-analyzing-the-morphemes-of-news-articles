from konlpy.tag import Kkma, Komoran, Okt

kom = Komoran()
kkm = Kkma()
okt = Okt()

text = '일잘러를 위한 파이썬과 40개의 작품들 형태소 분석방법 입니다.'

print("kom: ", kom.pos(text))
print("kkm: ", kkm.pos(text))

print("okt: ", okt.morphs(text))
print("okt 명사: ", okt.nouns(text))