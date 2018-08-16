from LinkedList import LinkedList

class HashSet:
    def __init__(self, capacity=10):
        # Create a list to use as the hash table
        self.table = [None] * capacity

    def add(self, item):
        # Find the hash code
        h = hash(item)
        index = h % len(self.table)

        # Check is it empty
        if self.table[index] == None:
            self.table[index] = LinkedList() # Need a new linked list for this entry

        if item not in self.table[index]:
            # Only add it if not already there (this is a set)
            self.table[index].add(item)

            if self.table[index] == 1:
                return None

            else:    
                return(index, item)

    def avarage_bucket_length(self):
        i = 0
        N = 0
        total = 0

        for i in range(0, len(self.table)):
            if self.table[i] != None:
                total += len(self.table[i])
                i += 1
                N += 1
        return total//N        

    def min_max_bucket(self):

        start_min = 0
        start_max = 0  
        for i in range(0, len(self.table)):
            if self.table[i] != None:
                if len(self.table[i]) > start_max:
                    start_max = i
                start_min = i     

        return(start_min, start_max) 

    def __iter__(self):
        cursor = self.table.head
        while cursor is not None:
            yield cursor.item
            cursor = cursor.next      

def main():

    # Read each test case
    lst = [1,5,27,35,11,15,105,95,31]
    hashset = HashSet()

    for x in lst:
        hashset.add(x)
    print(hashset.min_max_bucket())    
   

if __name__ == '__main__':
    main()







