class Node :

    def __init__(self,val):


        self.val=val
        self.right=None
        self.left=None

    def insert(self,data):

        if (self.val == data):

            return False

        elif(self.val > data):

            if (self.left):

               return self.left.insert(data)

            else:
                self.left = Node(data)

                print("Node created as leftchild  with value : " + str(data))

                return True

        else:

            if (self.right):


               return self.right.insert(data)

            else:
                self.right = Node(data)
                print("Node created as rightchild with value : " + str(data))
                return True

    def find(self,data):

        if (self.val == data):

            return True

        elif(self.val > data):

            if(self.left):

                return self.left.find(data)

            else:
                return False

        else:
            if (self.right):

                return self.right.find(data)
            else:
                return False


    



class Tree :


    def __init__(self):

        self.root =None



    def insert(self,data):



        if self.root:

            return self.root.insert(data)


        else:


            self.root = Node(data)
            return("Root Node created with value " + str(data))


    def find(self, data):

        if (self.root):      #to check if there is root in the tree

            return self.root.find(data)





        else :
            print("root doesnt exist")
            return False







    #  10
    # / \
    #2   12
    # \
    #  5
    #   \
    #    6
def main():

    test=Tree()

    print(test.insert(10))

    print(test.insert(12))
    print(test.insert(2))
    print(test.insert(5))
    print(test.insert(6))
    print(test.insert(3))
    print(test.find(15))
    print(test.find(10))
    print(test.find(11))




main()
