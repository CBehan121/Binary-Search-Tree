class HashSet:
    def __init__(self, capacity=10):
       
        self.table = [None] * capacity

    def add(self, item):
        
        h = hash(item)
        index = h % len(self.table)

        # Check is it empty
        if self.table[index] == None:
            self.table[index] = LinkedList() 

        if item not in self.table[index]:
     
            self.table[index].add(item)
            if len(self.table[index]) > 1:
                return (index, item)
            
    def average_bucket_length(self):
        i = 0
        j = 0
        _sum = 0
        while i < len(self.table):
            if self.table[i] != None:
                _sum += len(self.table[i])
                j += 1
            i += 1
        return(_sum / j)
    


    def max_min_bucket_length(self):
        i = 0
        list_ = []
        while i < len(self.table):
            if self.table[i] is not None:
                list_.append(len(self.table[i]))
            i = i + 1
        return(max(list_), min(list_))
    




    def __iter__(self):
        startpoint = 0
        while startpoint  < len(self.table):
            if self.table[startpoint] is not None:

                yield from self.table[startpoint]
            startpoint += 1



class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        self.head = Node(item, self.head)

    def remove(self):
        if self.is_empty():
            return None
        else:
            item = self.head.item
            self.head = self.head.next   
            return item

    def is_empty(self):
        return self.head == None

    def __iter__(self):
        cursor = self.head
        while cursor is not None:
            yield cursor.item
            cursor = cursor.next

    def recursive_len(self, ptr):
        if ptr == None:
            return 0
        else:
            return 1 + self.recursive_len(ptr.next)

    def __len__(self):
        return self.recursive_len(self.head)

    def recursive_contains(self, ptr, item):
        if ptr == None:
            return False
        else:
            return item == ptr.item or self.recursive_contains(ptr.next)

    def __in__(self, item):
        return recursive_contains(self.head, item)

    def recursive_str(self, ptr):
        if ptr == None:
            return ""
        else:
            return str(ptr.item) + "->" + self.recursive_str(ptr.next)

    def __str__(self):
        return self.recursive_str(self.head)

