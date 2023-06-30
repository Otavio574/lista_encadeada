class Node:

    def __init__(self, item, prev=None, next=None):
        
        self.item = item
        self.prev = prev
        self.next = next


class lista_encadeada:

    def __init__(self):
        
        self.header = None
        self.trailer = None
        self.size = 0


    def insert(self, item):
        
        if self.size > 0:
        
            newNode = Node(item)
            newNode.prev = self.trailer
            self.trailer.next = newNode
            self.trailer = newNode
        
        else:
        
            self.header = self.trailer = Node(item)


        self.size += 1


    def delete_node(self, item):

        currNode = self.header
        
        while currNode:

            if currNode.item == item:

                if currNode.prev is not None:

                    currNode.prev.next = currNode.next
                
                
                if currNode.next is not None:
                    
                    currNode.next.prev = currNode.prev
                
                else:
                  
                    self.trailer = currNode.prev
               
                if currNode == self.header:
                    
                    self.header == currNode.next
                
                return
            
            currNode = currNode.next

            
    def to_show(self):
      
        actualNode = self.trailer
        
        while actualNode:

            print(actualNode.item)
            actualNode = actualNode.prev
    

        
site = lista_encadeada()

while True:

    entrada = input().strip().split()
    
    if entrada [0] == 'ADD':

        site.insert(entrada[1])
    

    elif entrada[0] == 'REM':

        site.delete_node(entrada[1])


    elif entrada[0] == 'FIND':
        
        site.delete_node(entrada[1])
        site.insert(entrada[1])
    
    elif entrada[0] == 'EXIB':
      
        site.to_show()
    
    elif entrada[0] == 'END':
      
        break

