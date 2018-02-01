words = {}
for word in input().split():
    words[word] = words.get(word,0)+1
    print(words[word],end = ' ')
    
    
        
