class stack:
    """a class to represent a stack"""
    
    def __init__(self,items,max_size,stack_pointer):
        self.items=items
        self.max_size=max_size
        self.stack_pointer=stack_pointer


    def is_empty(self):
        if self.items==0:
            print("The stack is empty.")

        else:
            print("The stack contains items.")

    def push(self,item):
        pass

    def pop(self):
        pass

    def peek(self):
        pass

    def size(self):
        print("The number of items in the stack is: {0}".format(self.items))


if __name__=="__main__":
    stack_one=stack(0,10,10)
    stack_one.is_empty()
    stack_one.size()

    
