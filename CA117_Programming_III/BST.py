#
#   Add a method to the BST class called in_order which will print all elements in order.
#

class Node:
    """ A node in a BST. It may have left and right subtrees """
    def __init__(self, item, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right

class BST:
    """ An implementation of a Binary Search Tree """
    def __init__(self):
        self.root = None

    def add(self, item):
        self.r_add(self.root, item)   

    def r_add(self, ptr, item):
        if ptr == None:
            ptr = Node(item, None, None)   

        elif item < ptr.left:
            return self.r_add(ptr.left, item)

        elif item > ptr:     
            return self.r_add(ptr.right, item)


    def count(self):
        self.r_count(self.root)

    def r_count(self, ptr):

         if ptr == None:
            return 0

         else:   
            return 1 + self.r_count(ptr.left) + self.r_count(ptr.right)

    def count_in_range(self, lo, hi):
        self.r_count_in_range(lo, hi, self.root)

    def r_count_in_range(self, lo, hi, ptr): 

        if ptr == None:
            return 0

        else: 
            if ptr.item == lo:      
                return 1 + self.r_count_in_range(lo, hi, ptr.right)

            elif ptr == hi:
                return 1 + self.r_count_in_range(lo, hi, ptr.left)

            elif ptr.item > lo and ptr.item < hi:
                return 1 + self.r_count_in_range(lo, hi, ptr.left) + self.r_count_in_range(lo, hi, ptr.right)
            
            else:
                return self.r_count_in_range(lo, hi, ptr.left) + self.r_count_in_range(lo, hi, ptr.right)    

    def height(self):
        self.r_height(self.root) 

    def r_height(self, ptr):
    
        if ptr == None:
            return 0

        else:
            1 + max(self.r_height(ptr.left), self.r_height(ptr.right))

    def summ(self):
        self.r_summ(self.root)

    def r_summ(self, ptr):
    
        if ptr == None:
            return 0

        else:
            return ptr.item + (self.r_summ(ptr.left) + self.r_summ(ptr.right))       

    def is_present(self, item):
        self.r_is_present(self.root, item)

    def r_is_present(self, ptr, item):

        if ptr == None:
            return False

        if ptr.item == item:
            return True

        elif item < ptr.item:
            return self.r_is_present(ptr.left, item)
        elif item > ptr.item:
            return self.r_is_present(ptr.right, item)   

    def leaf_count(self):
        self.r_leaf_count(self.root)

    def r_leaf_count(self, ptr):
    
        if ptr == None:
            return 0  

        if self.r_leaf_count(ptr.left) == 0 and self.r_leaf_count(ptr.right) == 0:
            return 1

        else:
            return self.r_leaf_count(self.left) + self.r_leaf_count(self.right)     

def maximus(BST):
    return 2 ** int(BST.height() - 1) == int(BST.count())
        


    def r_in_order(self, ptr):
        if ptr != None:
            self.r_in_order(ptr.left)
            print(ptr.item, end==' ')
            self.r_in_order(ptr.right)
        return None

    def in_order(self): 
        return(self.r_in_order(self.root))
        print()


    def pre_order(self):
        return self.r_pre_order(self.root)
        print()

    def r_pre_order(self, ptr):
        if ptr != None:
           print(ptr.item, end==' ')
           self.r_pre_order(ptr.left)
           self.r_pre_order(ptr.right)
        return None 

    def post_order(self):
        return self.r_post_order(self.root)
        print()

    def r_post_order(self, ptr):
        if ptr != None:
           self.r_pre_order(ptr.left)
           self.r_pre_order(ptr.right)
           print(ptr.item, end==' ')
        return None    

import sys
from BST import BST

def main():
    # Read each test case

    bst = BST()
    for ele in [2, 7, 4, 8, 5]:
        bst.add(ele)
    print(bst.count_in_range(3, 5))

if __name__ == "__main__":
    main()        
       




