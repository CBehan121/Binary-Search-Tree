class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

# Note, these are methods "A method is a function that is stored as a class attribute"
class LinkedList:
    def __init__(self):
        self.head = None
    def __iter__(self):
        cursor = self.head
        while cursor is not None:
            yield cursor.item
            cursor = cursor.next

    def add(self, item):
        self.head = Node(item, self.head)

    def remove(self):
        if self.is_empty():
            return None
        else:
            item = self.head.item
            self.head = self.head.next    # remove the item by moving the head pointer
            return item

    def is_empty(self):
        return self.head == None
    def count(self):
        return self._count(self.head)
    def _count(self,node):
        return 0 if not node else 1 + self._count(node.next)
    def contains(self, item):
        def _contains(node, item):
            if not node:
                return False
            else:
                return True if node.item == item else _contains(node.next, item)
        return _contains(self.head, item)

    def rcontains(self, item):
        return self._rcontains(self.head, item)

    def _rcontains(self, node, item):
        if not node:
            return False
        if node.item == item:
            return True
        return self._rcontains(node.next, item)
    def recursive_len(self, ptr):
        if ptr == None:
            return 0
        else:
            return 1 + self.recursive_len(ptr.next)

    def __len__(self):
        return self.recursive_len(self.head)
ll = LinkedList()
for i in range(0, 10):
    ll.add(i)

print(ll.count())