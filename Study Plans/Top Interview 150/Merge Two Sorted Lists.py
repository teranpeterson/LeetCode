# SOLVED

class Node:
    def __init__(self, val):
        self.next = None
        self.val = val

def merge(l1: Node, l2: Node):
    head = Node(-1)

    curr = head
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        elif l1.val > l2.val:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    while l1:
        curr.next = l1
        l1 = l1.next
    while l2:
        curr.next = l2
        l2 = l2.next
    return head.next

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
n9 = Node(9)

# 1 3 4 8
n1.next = n3
n3.next = n4
n4.next = n8

# 2 5 6 7 9
n2.next = n5
n5.next = n6
n6.next = n7
n7.next = n9

def pprint(node: Node):
    while node:
        print(node.val)
        node = node.next

pprint(merge(n1, n2))
