class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
# Creating nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# Linking nodes
node1.next = node2
node2.next = node3
# Traversing the linked nodes
current = node1

while current is not None:
    print(current.data)
    current = current.next