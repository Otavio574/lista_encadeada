class TreeNode:

    #Inicializando a classe, espero que faça sentido, vi em alguns fóruns e no slide que usam muito uma relação de chave e valor, como em um dicionário, então tentei replicar

    def __init__(self, value = None, left=None, right=None): 

        self.value = value
      
        self.left = left
        self.right = right
        self.node = None
        self.parent = None
        self.grandparent = None
        self.tall = 1

# Criando uma classe própria para a árvore, inicializando sem parâmetros bem definidos pois não sei, mas indicando que inicialmente não tem raiz e que a altura é 0

class BinaryTree:

    def __init__(self):

        self.deep = 0
        self.size = 0
        self.root = None
        self.tall = 0
    
    def add(self, value):
        
        self.root = self._add(self.root, value)

    def _add(self, node, value):

        if not node:
            
            return TreeNode(value)
        
        elif value < node.value:
        
            
            node.left = self._add(node.left, value)
            node.left.parent = node

        elif value > node.value:
        
            node.right = self._add(node.right, value)
            node.right.parent = node
    
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
    

    def height_node(self, value):

            return self._height_node(self.root, value, 0)
    
    def _height_node(self, node, value, height = 0):

        if node == None:

            return -1
        
        else:
        
            if value == node.value:

                return height

            elif value > node.value:

                return self._height_node(node.right, value, height + 1)
        
            else:

                return self._height_node(node.left, value, height + 1)
    
    def turn_right(self, node):
        
        if node is None or node.parent is None or node.parent.left is not node:
        
            return

        parent = node.parent
        grandparent = parent.parent
        
        if grandparent is not None:
        
            if parent is grandparent.left:
        
                grandparent.left = node
        
            else:
        
                grandparent.right = node
        
            node.parent = grandparent
        
        else:
        
            node.parent = None
            self.root = node

        parent.left = node.right
        
        if node.right is not None:
        
            node.right.parent = parent
        
        node.right = parent
        parent.parent = node


    def turn_left(self, node):
        
        if node is None or node.parent is None or node.parent.right is not node:
        
            return

        parent = node.parent
        grandparent = parent.parent
        
        if grandparent is not None:
        
            if parent is grandparent.left:
        
                grandparent.left = node
        
            else:
        
                grandparent.right = node
        
            node.parent = grandparent
        
        else:
        
            node.parent = None
            self.root = node

        parent.right = node.left
        
        if node.left is not None:
        
            node.left.parent = parent
        
        node.left = parent
        parent.parent = node


    def rotate(self, value):

        node = self.search(value)
        
        while node.parent is not None:
        
            if node.value < node.parent.value:
        
                self.turn_right(node)
        
            else:
        
                self.turn_left(node)

        
    def printtree(self):
        
        if self.root != None:
            
            self._printtree(self.root)
    
    
    def _printtree(self, node):
        
        if node != None:
            
            self._printtree(node.left)
            print(node.value, end = ' ')
            self._printtree(node.right)

root = None
tree = BinaryTree()

while True:
    
    
    try:
        
        sentence = input().split()
        
        if sentence[0] == 'ADD':
            
            tree.add(int(sentence[1]))
            print(tree.height_node(int(sentence[1])))
                  
        if sentence[0] == 'SCH':
            
            print(tree.height_node(int(sentence[1])))
            tree.search(int(sentence[1]))
            
            if tree.search(int(sentence[1])):
            
                tree.rotate(int(sentence[1]))
   
    except EOFError as Error:
        
        #tree.printtree()
        break