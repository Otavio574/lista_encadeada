class HashNode: #criação de um nó, pois achei que poderia ser conveniente

    def __init__(self, key, value):
        
        self.next = None
        self.key = key
        self.value = value


class HashTable: #criação de uma classe para a própria tabela, e sua inicialização com o parâmetro do tamanho

    def __init__(self, size):

        self.size = size
        self.slot = [None] * size
        self.currsize = 0 


    def hash_function(self, key): #função para saber aonde vou alocar os dados

        v = int(key)
        function = v % self.size

        return function
    

    def hash_insert(self, key, value): #o insert, feito com base no slot onde vou adicionar

        if self.hash_is_full == True:

            return -1
        
        flag = self.hash_function(key)

        if self.slot[flag] == None:

            self.slot[flag] = HashNode(key, value)
        
        else:

            aux = self.slot[flag]

            while aux != None:

                flag += 1
                flag = flag % self.size
                aux = self.slot[flag]

            self.slot[flag] = HashNode(key, value)

        self.currsize += 1
        #print(flag, value)
        return flag


    def hash_search (self, key):

        flag = self.hash_function(key)

        if self.slot[flag] == None:

            return False
        
        else:
            
            aux = self.slot[flag]

            while aux != None:

                if aux.value == key:
                    
                    return (flag, aux.value)
                
                flag += 1
                flag = flag % self.size
                aux = self.slot[flag]

            return False
    

    def hash_is_full(self):

        if self.currsize == self.size:

            return True

        else:

            return False
        

n = int(input())
c = int(input())
table = HashTable(n)

for i in range(c):

    sentence = input().split()
    
    command = sentence[0]
    number = int(sentence[1])

    verify = table.hash_is_full()

    if verify == False:
    
        if command == 'ADD':

            
            k = table.hash_insert(number, number)
            print(f'E: {k}')

        elif command == 'SCH':

            search = table.hash_search(number)
            
            if search == False:

                print('NE')
            
            else:

                print(f'E: {search[0]}')

        elif command == 'CAP':

        
            if table.slot[number] == None:

                print('D')
            
            else:

                print(f'A: {table.slot[number].value}')

    else:

        print('Toda memoria utilizada')
        break