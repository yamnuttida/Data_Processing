from pythainlp.transliterate import romanize
from pythainlp.tokenize import word_tokenize

with open('songTH.txt', mode = 'r', encoding = 'utf-8') as th:
        text = th.read()
        word = word_tokenize(text, engine='icu', keep_whitespace=False)
        print(word)
th.close()

with open('songEN.txt', mode = 'w', encoding = 'utf-8') as en:
        lsword = []
        for i in word:
            lsword.append(romanize(i,engine='royin'))
        outtext = ' '.join(lsword)
        print(outtext)
        en.write(outtext)
en.close()
