class Node:
    def __init__(self):
        self.Data=None
        self.NextPointer=None

    def GetData(self):
        return self.Data
        

    def SetData(self,newdata):
        self.Data=newdata

    def GetNextPointer(self):
        return self.next

    def SetNextPointer(self,newnext):
        self.next=newnext
        



class UnorderedList:
    def __init__(self):
        self.Head=None

    def isEmpty(self):
        return self.head==none

    def add(self,item):
        temp=Node(data)
        temp.setNext(self.head)
        self.head=temp

    def getList(self):

    def length(self):

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

if __name__="__main__":
    
        
