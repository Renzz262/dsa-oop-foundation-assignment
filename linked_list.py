class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self,data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        
        while current.next is not None:
            current = current.next
            
        current.next = new_node
        
    def display(self):
        current = self.head
        
        while current is not None:
            print(current.data)
            current = current.next
            
    def search(self,data):
        current = self.head
        
        while current is not None:
            if current.data == data:
                return True
            
            current = current.next
            
        return False
    
    # Creating linked list object
    
my_list = LinkedList()
    
my_list.append(10)
my_list.append(20)
my_list.append(30)
    
# display list
print("Linked List is:")
my_list.display()
    
    # search for a value
print("Searching for 20")
print(my_list.search(20))
    
print ("Searching for 50:")
print(my_list.search(50))
    
    