def solution(word):
    answer = 0
    word_list = []
    words = "AEIOU"
    
    def search(cnt, w):
        if cnt == 5:
            return
        for i in range(len(words)):
                word_list.append(w + words[i])
                search(cnt + 1, w + words[i])
                
            
    search(0, "")
    
    return word_list.index(word) + 1