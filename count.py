import math

def minimalOperations(words):
    result = []
    i = 0
    
    #Iterating over all words
    for w in words:
        x = 0
        i = 0
        
        while i < len(w):
            count = 1
            #To compare adjacent letters
            for j in range(i+1, len(w)):
                if w[i] != w[j]:
                    break
                else:
                    count += 1
                    
            if count > 1:
                #This will determine the number of letters to be replaced
                x += math.floor(count / 2)
                i += count
            else:
                i += 1
                
        if x > 0:
            result.append(x)
        else:
            result.append(0)
            
    return result
    

wordList = ['aab','abb','baaac','break','qqwerrrdffghiio','jjjjjooperttyyywq']            
res = minimalOperations(wordList)
print(res)