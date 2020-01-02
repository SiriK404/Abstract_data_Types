
class Queue_implementation():



    def __init__(self,max):

        self.items=[]
        self.None_value = None
        self.max=max


    def push(self,item):

        if( int(len(self.items)) < self.max):
            self.items.append(item)



        else :
            self.items.pop(0)
            self.items.append(item)

        return self.items

    def pop(self):


        self.items.pop(0)







    def queue_items(self):

        print(self.items)




def main():

    max = input("Enter the size of queue to be created: ")
    a= Queue_implementation(int(max))



    a.push(1)
    a.push(2)
    a.push(3)
    a.queue_items()
    a.push(4)
    a.queue_items()
    a.pop()
    a.pop()
    a.queue_items()




if __name__ == '__main__':
    main()
