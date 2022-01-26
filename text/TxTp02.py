from pythainlp.util import rank
from pythainlp.tokenize import word_tokenize
from collections import Counter

with open('NEWS.txt', mode = 'r', encoding = 'utf-8') as new:
    
        text = new.read()
        words = word_tokenize(text, engine='newmm', keep_whitespace=False)
        word_rank = rank(words)  #Counter(words)
        print(word_rank)

new.close()

with open('Count.txt', mode = 'w', encoding = 'utf-8') as cnt:
    
        word_sort = word_rank.most_common()
        for i in word_sort:
            cnt.write('%s\t %d' %(i[0],i[1]) + '\n')
        
cnt.close()

