def palindrome_check(word):
    
    if (len(word)==1) or (len(word)==0):
        Result=True
    elif word[0]==word[1]:
        word=word[1:-1]
        result=palindrome_check(word)
    else:
        Result=False
         
    

    return Result
if __name__=="__main__":
    word=input("Please enter a word: ")
    Result=palindrome_check(word)
    print(Result) 
