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
        n = Doubly_Linked_List_Node(x)
        if self.head:
            n.next = self.head
            self.head.prev = n
            self.head = n
        else:
            self.head = self.tail = n

    def insert_last(self, x):
        n = Doubly_Linked_List_Node(x)
        if self.tail:
            n.prev = self.tail
            self.tail.next = n
            self.tail = n
        else:
            self.head = self.tail = n

    def delete_first(self):
        x = self.head.item
        if self.head:
            self.head = self.head.next
            self.head.prev = None
        else:
            self.tail = None
        return x

    def delete_last(self):
        x = self.tail.item
        if self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            self.head = None
        return x

    def remove(self, x1, x2):
        L2 = Doubly_Linked_List_Seq()
        L2.head, L2.tail = x1, x2

        if x1.prev:
            x1.prev.next = x2.next
        else:
            self.head = x2.next

        if x2.next:
            x2.next.prev = x1.prev
        else:
            self.tail = x1.prev

        x1.prev, x2.next = None, None
        return L2

    def splice(self, x, L2):
        x1, x2 = L2.head, L2.tail
        xn = x.next
        L2.head = L2.tail = None
        x.next, x1.prev = x1, x
        x2.next = xn
        if xn:
            xn.prev = x2
        else:
            self.tail = x2
