class Doubly_Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.prev = None
        self.next = None

    def later_node(self, i):
        if i == 0: return self
        assert self.next
        return self.next.later_node(i - 1)

class Doubly_Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def __str__(self):
        return '-'.join([('(%s)' % x) for x in self])

    def build(self, X):
        for a in X:
            self.insert_last(a)

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):
        x_node = Doubly_Linked_List_Node(x)
        prev_head = self.head

        self.head = x_node
        if (self.tail is None):
            self.tail = x_node

        x_node.next = prev_head
        if (prev_head is not None):
            prev_head.prev = x_node
    
    def insert_last(self, x):
        x_node = Doubly_Linked_List_Node(x)
        prev_tail = self.tail

        self.tail = x_node
        if (self.head is None):
            self.head = x_node

        x_node.prev = prev_tail
        if (prev_tail is not None):
            prev_tail.next = x_node

    def delete_first(self):
        x = self.head
        self.head.next.prev = None
        self.head = self.head.next
        return x.item

    def delete_last(self):
        x = self.tail
        self.tail.prev.next = None
        self.tail = self.tail.prev
        return x.item

    def remove(self, x1, x2):
        L2 = Doubly_Linked_List_Seq()

        prev_node = x1.prev
        next_node = x2.next
        prev_node.next = next_node
        next_node.prev = prev_node
        
        x1.prev = None
        x2.next = None
        L2.head = x1
        L2.tail = x2
        
        return L2

    def splice(self, x, L2):
        L2.head.prev = x
        L2.tail.next = x.next

        if (x.next is not None):
            x.next.prev = L2.tail
        x.next = L2.head
        
        L2.head = None
        L2.tail = None
