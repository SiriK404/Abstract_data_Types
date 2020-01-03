#Binary Tree Implementation with Insert,Find operations
#Also has Depth First Traversal (Preorder & Postorder)

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

#Depth First Traversal


#Preorder function starts from root and goes down to left first then right till last node and prints values

#postorder function starts from last node on left side and traverses upward.


#inorder function starts from left side reaches root then traveres right side
    def preorder(self):



        if self.val:

            print(self.val)

        if self.left:

            self.left.preorder()

        if self.right:

            self.right.preorder()


    def postorder(self):


        if self.left:

            self.left.postorder()

        if self.right:

            self.right.postorder()

        if self.val:

            print(str(self.val))

    def inorder(self):

        if self.left:

            self.left.inorder()

        if self.val:

            print(str(self.val))

        if self.right:

            self.right.inorder()
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

    def prinTree(self):

        if self.root:
            print("this is depth first preorder traversal of the tree:")
            self.root.preorder()
            print("this is depth first postorder traversal of the tree:")
            self.root.postorder()
            print("this is depth first inorder traversal of the tree:")
            self.root.inorder()


        else:
            return False


    #       10
    #      / \
    #     2   12
    #    / \
    #   1   3
    #        \
    #         5
def main():

    test=Tree()

    print(test.insert(10))

    print(test.insert(12))
    print(test.insert(2))
    print(test.insert(5))
    print(test.insert(3))
    print(test.insert(1))


    print(test.find(15))
    print(test.find(10))
    print(test.find(11))

    print(test.prinTree())


if __name__== "__main__" :

    main()
