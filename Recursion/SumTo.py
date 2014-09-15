def SumTo(n):
    if n==1:
        result=1
    else:
        result=n+SumTo(n-1)
    return result


if __name__=="__main__":
    
    n=int(input("Enter your number: "))
    Result=SumTo(n)    
    print(Result) 
