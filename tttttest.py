import re
from zhon.hanzi import punctuation
import jieba

text = ['商业秘密的秘密性那是维系其商业价值和垄断地位的前提条件之一',
        '南口阿玛施新春第一批限量春装到店啦\\ue310   \\ue310   \\ue310   春暖花开淑女裙、冰蓝色公主衫\\ue006   气质粉小西装、冰丝女王长半裙、\\ue319   皇',
        '带给我们大常州一场壮观的视觉盛宴',
        '有原因不明的泌尿系统结石等',
        '23年从盐城拉回来的麻麻的嫁妆']


# print(len(text))

stop_words = ['商业秘密','盐城', '春装']


words = []
remove_chars = '[0-9’a-zA-Z!"#$%&\'()*\\\\+,-./:;<=>?@?★…‘’[\\]^_`{|}~(\s*)]+'
for i in range(0, len(text)):
  newstr = re.sub(remove_chars, '', text[i])
  text[i] = re.sub("[{}]+".format(punctuation), "", newstr)
  list_words = jieba.lcut(text[i])
  for word in list_words:
    if word in stop_words:
      list_words.remove(word)
  words.append(list_words)

print(words)