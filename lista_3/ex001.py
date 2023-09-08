class Hash:

    def __init__(self, cpf, magic_number):  #inicializando a classe, tomando o magic number e o cpf como parâmetro

        self.cpf = cpf
        self.magic_number = magic_number
        self.table = [None] * 10


    def hash_insert(self, cpf):
        
        for char in cpf: #uma forma de pegar cada caractere do CPF e multiplicar por 10 e fazer o hash
        
            index = int(char)
        
            if self.table[index] is not None:
        
                self.table[index] += index * 10
        
            else:
        
                self.table[index] = index * 10
                

    def validate(self): #função pra validar o que a questão pediu. insiro o CPF, aplico a mumltiplicação por 10 e somo os valores até verificar se em alguma das somas possíveis de pares resulta no magic nubmer
        
        self.hash_insert(self.cpf)
        
        for i in range(len(self.table)):

            for j in range (len(self.table)):

                if self.table[i] is not None and self.table[j] is not None:
                
                    if i != j:

                        addition = self.table[i] + self.table[j]
                    
                        if addition == int(self.magic_number):
                            
                            return True
        
        return False


N = int(input())

for c in range (N):
    
    numbers = input().split()
    
    cpf = numbers[0]
    magic_number = numbers[1]
    person = Hash(cpf, magic_number)
    conclusion = person.validate()

    if conclusion == True:

        print ('UP Permission')
    
    else:

        print('NOT Permission')