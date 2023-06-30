class Node:

    def __init__(self, item, value, prev=None, next=None):
        
        self.item = (item, float(value))
        self.prev = prev
        self.next = next


class lista_encadeada:

    def __init__(self):
        
        self.header = None
        self.trailer = None
        self.size = 0
        self.caixa1 = 0
        self.caixa2 = 0


    def insert(self, item, value):
        
        if self.size > 0:
        
            newNode = Node(item, value)
            newNode.prev = self.trailer
            self.trailer.next = newNode
            self.trailer = newNode
        
        else:
        
            self.header = self.trailer = Node(item, value)

        self.size += 1

    def is_empty(self):

        if self.size == 0:

            return True

        else:
            
            return False

  
    def _lenght_ (self):
      
        return self.size
    
    def delete_first(self, num):
        
        if self.size == 0:

            return

        elif self.size == 1:

            name = self.header.item
            print(f'{name[0]} foi chamado para o caixa {num}')
            
            if num == 1:
                    
                self.caixa1 = self.valores(name[1], num)
            
            elif num == 2:
                
                self.caixa2 = self.valores(name[1], num)
            
            self.header = self.trailer = None
        
        else:

            name = self.header.item
            print(f'{name[0]} foi chamado para o caixa {num}')
            
            if num == 1:
                    
                self.caixa1 = self.valores(name[1], num)
            
            elif num == 2:
                
                self.caixa2 = self.valores(name[1], num)
            
            self.header = self.header.next
            self.header.prev = None
        
        self.size -= 1
        return
    
    def delete_last(self, num):
      
        if self.size == 0:

            return

        elif self.size == 1:

            name = self.trailer.item
            print(f'{name[0]} foi chamado para o caixa {num}')
            
            if num == 1:
                    
                self.caixa1 = self.valores(name[1], num)
            
            elif num == 2:
                
                self.caixa2 = self.valores(name[1], num)
            
            self.trailer = self.header = None
        
        else:
            
            name = self.trailer.item
            print(f'{name[0]} foi chamado para o caixa {num}')
            
            if num == 1:
                    
                self.caixa1 = self.valores(name[1], num)
            
            elif num == 2:
                
                self.caixa2 = self.valores(name[1], num)
            
            self.trailer = self.trailer.prev
            self.trailer.next = None
            
        self.size -= 1
            
    
    def to_show(self):
      
        actualNode = self.trailer
        
        while actualNode:

            print(actualNode.item)
            actualNode = actualNode.next
    
    
    def valores(self, money, num):
        
        if num == 1:

            self.caixa1 = self.caixa1 + money
            return self.caixa1
        
        elif num == 2:
          
            self.caixa2 = self.caixa2 + money
            return self.caixa2
        
    
    def return_values(self, num):

        if num == 1:
            
            return self.caixa1
        
        elif num == 2:
          
            return self.caixa2

    

fila1 = lista_encadeada()
fila2 = lista_encadeada()

while True:

    entrada = input().strip().split()
    
    #fila1.to_show()
    
    if entrada[0] == 'ENTROU:':
        
        valor = entrada[3]
        
        if entrada[2] == '1':

            fila1.insert(entrada[1], entrada[3])
            #fila1.to_show()
            print(f'{entrada[1]} entrou na fila {entrada[2]}')  
            
        elif entrada[2] == '2':

            fila2.insert(entrada[1], entrada[3])
            print(f'{entrada[1]} entrou na fila {entrada[2]}')  
            
    elif entrada [0] == 'PROXIMO:':
    
        if entrada[1] == '1':

            tamanho = fila1._lenght_()
            if tamanho == 0:
              
                fila2.delete_last(1)
            
            else:
                
                fila1.delete_first(1)
                
        elif entrada[1] == '2':
            
            tamanho = fila2._lenght_()
            if tamanho == 0:
              
                fila1.delete_last(2)
            
            else:
                
                fila2.delete_first(2)
                
        
    elif entrada[0] == 'FIM':

        #fila1.to_show()
        #fila2.to_show()
        
        total1 = fila1.return_values(1) + fila2.return_values(1)
        total2 = fila1.return_values(2) + fila2.return_values(2)
        
        print(f'Caixa 1: R$ {total1:.2f}, Caixa 2: R$ {total2:.2f}')
        break
  
