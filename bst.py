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
        """ Add this item to its correct position on the tree """
        # This is a non recursive add method.
        if self.root == None: # ... Empty tree ...
            self.root = Node(item, None, None) # ... so, make this the root
        else:
            # Find where to put the item
            child_tree = self.root
            while child_tree != None:
                parent = child_tree
                if item < child_tree.item: # If smaller ... 
                    child_tree = child_tree.left # ... move to the left
                else:
                    child_tree = child_tree.right

            # child_tree should be pointing to the new node, but we've gone too far
            # we need to modify the parent nodes
            if item < parent.item:
                parent.left = Node(item, None, None)
            elif item > parent.item:
                parent.right = Node(item, None, None)
            #else:
            #   equal ... don't add it to the set.
    def height(self):
        return self.r_height(self.root)
    def r_height(self, ptr):
        if not ptr:
            return 0
        return max(1 +self.r_height(ptr.right), 1+ self.r_height(ptr.left))
                
    def recursive_countToNode(self, ptr, item, _lst):
        if not ptr:
                return 0
        _lst.append(ptr.item)
        if ptr.item == item:
            return _lst
        elif ptr.item < item:
            return(self.recursive_count(ptr.right, item,  _lst))
        elif ptr.item > item:
            return(self.recursive_count(ptr.left,item,_lst))
    def countToNode(self, item):
        l_st = []
        return self.recursive_count(self.root, item, l_st)
    def max(self):
        return self.r_max(self.root)   
    def r_max(self, ptr):
            if not ptr:
                return 0
            if not ptr.right:
                return ptr.item
            else:
                return self.r_max(ptr.right)
    def min(self):
        return self.r_min(self.root)
    def r_min(self, ptr):
        if not ptr:
            return 0
        if not ptr.left:
            return ptr.item
        else:
            return self.r_min(ptr.left)
    def count(self):
        return self.r_count(self.root)
    def r_count(self,ptr):
        if not ptr:
            return 0
        else:
            return 1 + self.r_count(ptr.left) + self.r_count(ptr.right)
    def countLeaves(self):
        return self.r_countLeaves(self.root)
    def r_countLeaves(self,ptr):
        if not ptr:
            return 0
        if not ptr.right and not ptr.left:
            return 1 
        return self.r_countLeaves(ptr.right) + self.r_countLeaves(ptr.left)
    def in_order(self):
        return self.r_in_order(self.root)
    def r_in_order(self, ptr):
        if not ptr:
            return 
        self.r_in_order(ptr.left)
        print(ptr.item)
        self.r_in_order(ptr.right)
    def post_order(self):
        return self.r_post_order(self.root)
    def r_post_order(self, ptr):
        if not ptr:
            return
        self.r_post_order(ptr.left)
        self.r_post_order(ptr.right)
        print(ptr.item)
    def pre_order(self):
        return self.r_pre_order(self.root)
    def r_pre_order(self, ptr):
        if not ptr:
            return
        print(ptr.item)
        self.r_pre_order(ptr.left)
        self.r_pre_order(ptr.right)
    def is_balanced(self):
        if not self.root:
            return False
        return True if abs(self.r_height(self.root.left)- self.r_height(self.root.right)) <= 1 else False





