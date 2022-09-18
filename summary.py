from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

file_name = input("Input File Name :\n")

with open('sample4.txt', 'r', encoding="utf8") as file:
    text = file.read().replace('\n', '')


stopWords = set(stopwords.words("english"))
words = word_tokenize(text)

frequencyTable = dict()
for word in words:
    word = word.lower()
    if word in stopWords:
        continue
    if word in frequencyTable:
        frequencyTable[word] += 1
    else:
        frequencyTable[word] = 1

sentences = sent_tokenize(text)
sentenceWeight = dict()
for sentence in sentences:
    for word, freq in frequencyTable. items():
        if word in sentence. lower():
            if sentence in sentenceWeight:
                sentenceWeight[sentence] += freq
            else:
                sentenceWeight[sentence] = freq

sumWeight = 0
for sentence in sentenceWeight:
    sumWeight += sentenceWeight[sentence]

average = int(sumWeight / len(sentenceWeight))

summary = ''
for sentence in sentences:
    if (sentence in sentenceWeight) and (sentenceWeight[sentence] > (1.2 * average)):
        summary += "" + sentence
print(summary)
