class TreeNode:

    #Inicializando a classe, espero que faça sentido, vi em alguns fóruns e no slide que usam muito uma relação de chave e valor, como em um dicionário, então tentei replicar

    def __init__(self, key, value = None, left=None, right=None): 

        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.root = None

# Criando uma classe própria para a árvore, inicializando sem parâmetros bem definidos pois não sei, mas indicando que inicialmente não tem raiz e que a altura é 0

class BinaryTree:

    def __init__(self):

        self.root = None
        self.deep = 0    
        
    #Lógica da função de inserção: recebo um item, transformo em um nó, verifico se já há uma raiz. Após isso, comparo com as chaves da raiz para verificar o lado em que se insere. Fiz isso recursivamente.
    
    def add(self, item):

        node = TreeNode(item)
        
        if self.root == None:
            
            self.root = node
        
        else:

            currNode = TreeNode(item)
            root = self.root

            while root:

                prevNode = currNode
                
                if item.key < root.key:

                    root = root.left
                
                else:

                    root = root.right
            


    def search(self, root, key):

        if self.root is None:

            return None

        else:
            
            self.root = root

            if  self.root.key == key:

                return self.root
        
            elif self.root.key > key:

                return self.search(self.root.left, key)
            
            else:

                return self.search(self.root.right, key)

while True:

    try:

        sentence = input().split()

        if sentence[0] == 'ADD':

            num = int(sentence[1])
            
            tree = TreeNode(num)
            tree.insert(num)
            
        elif sentence[0] == 'SCH':

            num = int(sentence[1])
            tree = TreeNode(num)
            tree.search(num)

    except:

        break