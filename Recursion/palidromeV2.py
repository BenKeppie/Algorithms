def palindrome_check(word):
    
    if len(word==1):
        Result=True
    else:
        Result=palindrome_check(word, first+1,last-1)
        Result=False
         
    

    return Result
if __name__=="__main__":
    word=input("Please enter a word: ")
    Result=palindrome_check(word)
    print(Result) 
