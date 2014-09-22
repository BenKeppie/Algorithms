class Node:
    def __init__(self,data):
        self.Data=data
        self.NextPointer=None

    def GetData(self):
        return self.Data
        

    def SetData(self,newdata):
        self.Data=newdata

    def GetNextPointer(self):
        return self.NextPointer

    def SetNextPointer(self,newnext):
        self.NextPointer=newnext
        



class UnorderedList:
    def __init__(self):
        self.Head=None

    def isEmpty(self):
        return self.Head==none

    def add(self,item):
        temp=Node(item)
        temp.SetNextPointer(self.Head)
        self.Head=temp

    def getList(self):
        
        while self.Head!=None:
            return self.Head
            self.Head=self.NextPointer        
            
        else:
            print()
            
        
            
            
            
        

    def length(self):
        temp=self.Head
        count=0
        while temp != None:
            
            count+=1
            temp=temp.NextPointer
        print(count)
        return count 

    def search(self,item):
        found=False
        while (current != None) and (found==False) :
            if current.getData() == item:
                found=True
            else:
                current= current.getNextPointer()
        return found

    def remove(self,item):
        current=self.Head
        found=False
        while found==False:
            if current.getData() == item:
                found=True
            else:
                previous=current
                current= current.getNext()

        if previous==None:
            self.Head=current.getNext()



class OrderedList(UnorderedList):
    def __init__(self):
        super().__init__()

    def search(self,item):
        current=self.Head
        found=False
        stop=False
        while current != None and stop ==False:
            if current.getData()==item:
                found=True
            else:
                if current.getData() > item:
                    stop=True
                else:
                    current=current.getNext()

        return found 
        

    def add(self,item):
        temp=self.Head
        while temp != None:
            if temp.NextPointer>temp.Head:
                print()
            temp=temp.NextPointer
        

if __name__=="__main__":
    myList=UnorderedList()
    myList.add(5)
    print(myList.length())
    myList.add(6)
    print(myList.length())
    myList.add(6)
    print(myList.length())
    print(myList.getList())
    List=OrderedList()
    List.add(5)
    List.add(3)
    List.add(8)
    
    
        
