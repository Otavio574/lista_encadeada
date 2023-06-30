letras = list()
sobra = list()

cont = totalf = totalv = 0
correto = True
posicao = 0
tamanho = 0
incremento = False
contador_absoluto = 0
referencia = 0

try:
    
    entrada = input().strip()

except:
    
    incremento = True
    print('Correto.')

else:

    for i in range (len(entrada)):
    
        letras.append(entrada[i])
    
    original = letras

if incremento == False:
    
    while True:
    
        contador_absoluto += 1
  
        if len(letras) == 0:
          
            print('Correto.')
        
        else:
        
            if original.count('F') == 0 or original.count('V') == 0:
              
                print('Incorreto, devido a capa na posição 1.')
                break

        
            else:
              
        
                if letras[0] == 'V':
    
                    print(f'Incorreto, devido a capa na posição {1}.')
                    break
                
                else:
    
                    contador = 0

                    if original.count('V') < original.count('F'):

                        for i in range(len(original)):

                            if original[i] == 'F':
                                contador += 1
        
                            if contador > original.count('V'):

                                print(f'Incorreto, devido a capa na posição {i + 1}.')
                                break
                        break
                      
                    elif original.count('F') > original.count('V'):

                        totalf = 0
                        totalv = 0
                        
                        for i in range(len(original)):

                            if original[i] == 'F':
                                totalf = totalf + 1
                            
                            elif original[i] == 'V':
                                totalv = totalv + 1

                            if totalv > totalf:

                                print(f'Incorreto, devido a capa na posição {i + 1}.')
                                break
                        
                        break

                        
                    else:

                        totalf = 0
                        totalv = 0

                        for i in range(len(original)):

                            if original[i] == 'F':
                                totalf = totalf + 1
                            
                            elif original[i] == 'V':
                                totalv = totalv + 1

                            if totalv > totalf:

                                correto = False
                                posicao = i
                                break
                        
                        if correto == True:

                            print('Correto.')
                            break
                        
                        else:

                             print(f'Incorreto, devido a capa na posição {posicao + 1}.')
                             break
