
# a program that takes a text input from user and prints it back to user in reverse order using stack implementation
class Stack:


    def __init__(self):
        self.list_of_items = []


    def push(self, item):
        self.list_of_items.append(item)


    def pop(self):
        return(self.list_of_items.pop())  # inbuilt pop operation for lists to remove and return  topmost item of the stack


    def isEmpty(self):
        if not self.list_of_items:  # to check for an empty list
            return True


    def peek(self):
        print(self.list_of_items[-1])  # returns topmost element of the stack


    def stack_items(self):
        print(self.list_of_items)





def Reverse():

    user_input= input ( "Input the string to reverse : ")

    length_of_string = len(user_input)

    a = Stack()

    for i in range (0,length_of_string):

        a.push(user_input[i])



    reverse_list=""


    for c in range(0,length_of_string):

        reverse_list+=a.pop()


    print(reverse_list)


Reverse()



