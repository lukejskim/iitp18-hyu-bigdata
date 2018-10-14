from collections import Counter
from konlpy.tag import Twitter
import pytagcloud

fp = open('data/president_speech.txt')
speech = fp.read()
fp.close()

nlp = Twitter()
nouns = nlp.nouns(speech)
# count = Counter(nouns)

nouns2 = [noun for noun in nouns if len(noun)>1]
count = Counter(nouns2)
print(nouns2)

common_tag = count.most_common(50)
tag_list = pytagcloud.make_tags(common_tag, maxsize=80)

# save_img = 'wordcloud/president_moon1.jpg'
# pytagcloud.create_tag_image(tag_list, save_img, size=(900, 600), fontname='Korean', rectangular=False)

# save_img = 'wordcloud/president_moon2.jpg'
# pytagcloud.create_tag_image(tag_list, save_img, size=(800, 600), fontname='Korean', rectangular=False)
#
save_img = 'wordcloud/president_moon3.jpg'
pytagcloud.create_tag_image(tag_list, save_img, size=(500, 500), fontname='Korean', rectangular=False)
