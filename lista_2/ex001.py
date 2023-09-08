class TreeNode:

    #Inicializando a classe, espero que faça sentido, vi em alguns fóruns e no slide que usam muito uma relação de chave e valor, como em um dicionário, então tentei replicar

    def __init__(self, value = None, left=None, right=None): 

        self.value = value
      
        self.left = left
        self.right = right
        self.node = None
        self.parent = None
        self.tall = 1

# Criando uma classe própria para a árvore, inicializando sem parâmetros bem definidos pois não sei, mas indicando que inicialmente não tem raiz e que a altura é 0

class BinaryTree:

    def __init__(self):

        self.deep = 0
        self.size = 0
        self.root = None
        self.tall = 1
  
#Lógica da função de inserção: recebo um item, transformo em um nó, verifico se já há uma raiz. Após isso, comparo com as chaves da raiz para verificar o lado em que se insere. Fiz isso recursivamente.

    def add(self, value):

        self.root = self._add(self.root, value)


    def _add(self, node, value):

        if not node:
            
            return TreeNode(value)
        
        elif value < node.value:
        
            node.left = self._add(node.left, value)
        
        else:
        
            node.right = self._add(node.right, value)

        node.tall = 1 + max(self.height_node(node.left), self.height_node(node.right))
      
        balance = self.balance_factor(node)
        
        if balance > 1:
            
            if value < node.left.value:
                
                return self.turn_right(node)
            
            else:
                
                node.left = self.turn_left(node.left)
                return self.turn_right(node)

        if balance < -1:
            
            if value > node.right.value:
                
                return self.turn_left(node)
           
            else:
                
                node.right = self.turn_right(node.right)
                return self.turn_left(node)

        return node
        

    def search(self, value):
        
        if self.root == None:

            return None
        
        else:

            return self._search(value, self.root)


    def _search(self, value, node):

        
        if value == node.value:
            
            return node

        elif value < node.value:

            if node.left:

                return self._search(value, node.left)
            

        elif value > node.value:

            if node.right:

                return self._search(value, node.right)
        
        else:

            return None
      
    
    def remove(self, value):
      
        self.root = self._remove(self.root, value)
    
    def _remove(self, node, value):
        
        if not node:
            
            return node
        
        elif value < node.value:
                
            node.left = self._remove(node.left, value)
            
        elif value > node.value:
            
            node.right = self._remove(node.right, value)    
            
        else:
            
            if node.left is None:
                
                aux = node.right
                node = None
                return aux
            
            elif node.right is None:
                
                aux = node.left
                node = None
                return aux
            
            aux = self.find_minimum(node.right)
            node.value = aux.value
            node.right = self._remove(node.right, aux.value)
        
        if node is None:
            
            return node
            
        balance = self.balance_factor(node)
        
        #if node.left != None and node.right != None:
            
        node.tall = 1 + max(self.height_node(node.left),
                            self.height_node(node.right))
                            
        if balance > 1:
            
            if self.balance_factor(node.left) >= 0:
            
                return self.turn_right(node)
            
            else:
            
                node.left = self.turn_left(node.left)
                return self.turn_right(node)
        
        if balance < -1:
        
            if self.balance_factor(node.right) <= 0:
    
                return self.turn_left(node)
    
            else:
    
                node.right = self.turn_right(node.right)
                return self.turn_left(node)
        
        return node
        
    def num_kids(self, node):

        num_kids = 0

        if node.left != None:

            num_kids += 1

        if node.right != None:

            num_kids += 1
        
        return num_kids

    
    def _min(self, node):
        
        node = node
        
        while node.left != None:
            
            node = node.left
        
        return node


    def minimum(self):

        node = self.root
        previous = None

        while node != None:

            previous = node
            node = node.left
        
        if previous != None:
        
            print(f'MENOR: {previous.value}')
        
        else:

            print('ARVORE VAZIA')

        return previous


    def maximum(self):

        node = self.root
        following = None

        while node != None:

            following = node
            node = node.right
        
        if following != None:
            
            print(f'MAIOR: {following.value}')
        
        else:

            print('ARVORE VAZIA')

        return following


    def height(self, node = None):

        if node == None:

            node = self.root

        if self.root == None:
            
            return 0
        
        else:
            
            return self._height(node, 0)


    def _height(self, node, currHeight):

        if node == None:

            return currHeight

        left_height = self._height(node.left, currHeight)
        right_height = self._height(node.right, currHeight)
        
        return max(left_height, right_height) + 1

    
    def height_node(self, node):
        
        if not node:
            
            return 0
        
        return node.tall
    

    
    def printtree(self):
        
        if self.root != None:
            
            self._printtree(self.root)
    
    
    def _printtree(self, node):
        
        if node != None:
            
            self._printtree(node.left)
            results.append(node.value)
            self._printtree(node.right)

    




    def turn_left(self, node):
        
        if node.right != None:
        
            newnode = node.right
            aux = newnode.left
            newnode.left = node
            node.right = aux
            node.tall = 1 + max(self.height_node(node.left),
                               self.height_node(node.right))
            newnode.tall = 1 + max(self.height_node(newnode.left),
                               self.height_node(newnode.right))
            return newnode
        
        else:
            
            return node

    def turn_right(self, node):
        
        if node.left != None:
        
            newnode = node.left
            aux = newnode.right
            newnode.right = node
            node.left = aux
            node.tall = 1 + max(self.height_node(node.left),
                               self.height_node(node.right))
            newnode.tall = 1 + max(self.height_node(newnode.left),
                               self.height_node(newnode.right))
 
            return newnode
        
        else:
          
            return node
    
    def find_minimum(self, node):
      
        if node is None or node.left is None:
            
            return node
       
        return self.find_minimum(node.left)
    
    
    def balance_factor(self, node):

        if node is None:
            
            return 0
        
        return self.height_node(node.left) - self.height_node(node.right)
    
tree = BinaryTree()
results = list()

while True:

    sentence = input().split()
    command = sentence[0]

    if command == 'DELETAR':
        
        name = sentence[1]
        tree.search(name)
        
        if tree.search(name) == None:
            
            print(f'{name} NAO ENCONTRADO')
        
        else:
            
            tree.remove(name)
            print(f'{name} DELETADO')
            
    
    if command == 'INSERIR':

        name = sentence[1]
        tree.search(name)
        
        if tree.search(name) == None:
        
            tree.add(name)
            print(f'{name} INSERIDO')
        
        else:
            
            print(f'{name} JA EXISTE')
        
    if command == 'MINIMO':

       tree.minimum()
    
    if command == 'MAXIMO':
      
        tree.maximum()
    
    if command == 'ALTURA':
        
        #print(node.right.value)
        print(f'ALTURA: {tree.height()}')
    
    if command == 'FIM':
        
        tree.printtree()
        
        if len(results) == 0:

            print('ARVORE VAZIA')
        
        else:

            for i in range (len(results)):

                if i == len(results) - 1:

                    print(f'{results[i]}')
                
                else:

                    print(f'{results[i]}', end = ' ')
        break