entrada = input().strip().split(',')
valor = input().strip()
novalista = list()

organizado = False

for i in range (len(entrada)-1):
    
    if entrada[i] > entrada[i+1]:
        
        print('A pilha está um caos.')
        organizado = True
        break
  

if organizado == False:
    
    for i in range (len(entrada)):
        
        if int(valor) > int(entrada[i-1]) and int(valor) < int(entrada[i]):
            
            entrada.insert(i, valor)
            break
        
    print(entrada)
