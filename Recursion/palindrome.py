def palindrome_check(word,first,last):
    
    if word[first] == word[last]:
        Result=True
    else:
        Result=palindrome_check(word, first+1,last-1)
        Result=False
         
    

    return Result
if __name__=="__main__":
    word=input("Please enter a word: ")
    first=0
    last=len(word)- 1
    Result=palindrome_check(word,first,last)
    print(Result) 
