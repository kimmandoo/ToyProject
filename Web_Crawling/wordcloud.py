# if you can't run this code, use Google colab research.
# Korean Natural Language processing code.

from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
from IPython.display import set_matplotlib_formats

data = pd.read_csv("./review.csv", sep=",")
dict_data = data.loc[:, ['STAR', 'REVIEW']]
dic = dict_data.to_dict('list')

lists = dic['REVIEW']

twitter = Okt()
morphs = []
for sentence in lists:
    morphs.append(twitter.pos(sentence))

print(morphs)

#전처리
noun_adj_adv_list = []
for sentence in morphs:
    for word, tag in sentence:
        if tag in ['Alpha'] and ("또" not in word) and ("등" not in word) and ("앞" not in word) and (
                "생" not in word) and ("를" not in word) and ("여기" not in word) and ("다른" not in word) and (
                "예" not in word) and ("은" not in word) and ("위해" not in word) and ("다음" not in word) and (
                "대한" not in word) and ("아주" not in word) and ("그" not in word) and ("도움" not in word) and (
                "약" not in word) and ("때문" not in word) and ("여러" not in word) and ("더" not in word) and (
                "이" not in word) and ("의" not in word) and ("및" not in word) and ("것" not in word) and (
                "내" not in word) and ("나" not in word) and ("수" not in word) and ("게" not in word) and (
                "말" not in word) and ("좀" not in word):
            noun_adj_adv_list.append(word)
        if tag in ['Noun'] and ("또" not in word) and ("등" not in word) and ("앞" not in word) and ("생" not in word) and (
                "를" not in word) and ("여기" not in word) and ("다른" not in word) and ("예" not in word) and (
                "은" not in word) and ("위해" not in word) and ("다음" not in word) and ("대한" not in word) and (
                "아주" not in word) and ("그" not in word) and ("도움" not in word) and ("약" not in word) and (
                "때문" not in word) and ("여러" not in word) and ("더" not in word) and ("이" not in word) and (
                "의" not in word) and ("및" not in word) and ("것" not in word) and ("내" not in word) and (
                "나" not in word) and ("수" not in word) and ("게" not in word) and ("말" not in word)and ("좀" not in word)and ("계좌" not in word) and ('인증' not in word):
            noun_adj_adv_list.append(word)
print(noun_adj_adv_list)

# 글자 수 세기
count = Counter(noun_adj_adv_list)
words = dict(count.most_common())
print(words)

# word cloud show
matplotlib.rc('font', family='Malgun Gothic')
set_matplotlib_formats('retina')
matplotlib.rc('axes', unicode_minus=False)

wordcloud = WordCloud(font_path='./NanumBarunGothic.ttf', background_color='black', colormap="Accent_r", width=4000,
                      height=2000).generate_from_frequencies(words)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
