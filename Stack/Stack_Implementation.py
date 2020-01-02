# This program shows implementation of stack data stucture in python using list

class Stack :

    def __init__(self):

        self.list_of_items = []


    def push(self,item):

        self.list_of_items.append(item)

    def pop(self):

        self.list_of_items.pop()  #inbuilt pop operation for lists to remove and return  topmost item of the stack


    def isEmpty(self):

        if not self.list_of_items:    #to check for an empty list
            return True




    def peek(self):

        print(self.list_of_items[-1])       #returns topmost element of the stack

    def  stack_items(self):

        print(self.list_of_items)

def main()

    a=Stack()


    if (a.isEmpty()==True):

        a.push('A')
        a.push('B')
        a.push('C')
        a.push('D')
        a.stack_items()
        a.pop()
        a.pop()
        a.stack_items()
        a.push('2')
        a.stack_items()
        a.peek()


    else :

        print("Stack is not empty .It has following elements on it : ")
        a.stack_items()



if __name__ == "__main__":

    main()

