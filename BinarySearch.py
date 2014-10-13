def BinarySearch(List,First,Last,ItemSought):
    ItemFound=False
    SearchFailed=False
    while not ItemFound or not SearchFailed:
        Midpoint=(First+Last)/2
        #print("Item Sought: {0} , Comparing to: {1}".format(ItemSought, List[Midpoint]))
        if List[Midpoint]==ItemSought:
            ItemFound=True
            print("Item found in the list")
            if First>=Last:
                SearchFailed=True
                
        else:
            if List[Midpoint]>ItemSought:
                Last=Midpoint-1
            else:
                First=Midpoint+1
    

if __name__ == "__main__":
    List=[1,2,3]
    BinarySearch(List, List[0], len(List)-1, 2)
    
