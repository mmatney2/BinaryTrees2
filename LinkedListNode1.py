class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next = None
    def traverse(self):
        node = self
        while node != None:
            print(node.value)
            node = node.next

node1 = LinkedListNode(1)
node2 = LinkedListNode(2)
node3 = LinkedListNode(3)
node4 = LinkedListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4

node1.traverse()