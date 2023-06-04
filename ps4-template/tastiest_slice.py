from Set_AVL_Tree import BST_Node, Set_AVL_Tree
#######################################
# DO NOT REMOVE THIS IMPORT STATEMENT #
# DO NOT MODIFY IMPORTED CODE         #
#######################################

class Key_Val_Item:
    def __init__(self, key, val):
        self.key = key
        self.val = val

    def __str__(self): 
        return "%s,%s" % (self.key, self.val)

class Part_B_Node(BST_Node):
    def subtree_update(A):
        super().subtree_update()
        #########################################
        A.total = A.item.val

#         import pdb; pdb.set_trace()
        if A.left is not None:
            A.total += A.left.total
        if A.right is not None:
            A.total += A.right.total

        A.max_prefix_sum = A.item.val
        if A.left is not None:
            A.max_prefix_sum += A.left.total
        A.k = A.item.key
    
        if (A.right is not None) and  (A.right.max_prefix_sum > 0):
            A.max_prefix_sum += A.right.max_prefix_sum
            A.k = A.right.k
        if (A.left is not None) and (A.left.max_prefix_sum > A.max_prefix_sum):
            A.max_prefix_sum = A.left.max_prefix_sum
            A.k = A.left.k
        #########################################

class Part_B_Tree(Set_AVL_Tree):
    def __init__(self): 
        super().__init__(Part_B_Node)

    def max_prefix(self):
        '''
        Output: (k, s) | a key k stored in tree whose
                       | prefix sum s is maximum
        '''
        k, s = 0, 0
        ##################
        if self.root is not None:
            k = self.root.k
            s = self.root.max_prefix_sum
        ##################
        return (k, s)

def tastiest_slice(toppings):
    '''
    Input:  toppings | List of integer tuples (x,y,t) representing 
                     | a topping at (x,y) with tastiness t
    Output: tastiest | Tuple (X,Y,T) representing a tastiest slice 
                     | at (X,Y) with tastiness T
    '''
    B = Part_B_Tree()   # use data structure from part (b)
    X, Y, T = 0, 0, 0

    # sort toppings by x coordinate
    # import pdb; pdb.set_trace()
    toppings.sort(key=lambda x: x[0])

    T = float('-inf')
    X = float('-inf')
    Y = float('-inf')
    class Topping:
        def __init__(self, key, val):
            self.key = key
            self.val = val
    
    for topping in toppings:
#        import pdb; pdb.set_trace()
        x = topping[0]
        y = topping[1]
        taste = topping[2]
        B.insert(Topping(y, taste))

        (k, max_pref) = B.max_prefix()
        if max_pref > T:
            T = max_pref
            X = x
            Y = k
    
    return (X, Y, T)
