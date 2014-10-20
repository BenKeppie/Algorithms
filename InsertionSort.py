def insertion_sort(List):
    for CurrentPointer in range(1,len(List)):
        CurrentValue=List[CurrentPointer]
        Pointer=CurrentPointer-1
        while (List[Pointer]>CurrentValue) and (Pointer>=0):
            
            List[Pointer+1]=List[Pointer]
            Pointer=Pointer-1
            
        List[Pointer+1]=CurrentValue
    return List

if __name__=="__main__":
    List=["z","A","A","D","C","B","A",]
    List=insertion_sort(List)
    print(List)
