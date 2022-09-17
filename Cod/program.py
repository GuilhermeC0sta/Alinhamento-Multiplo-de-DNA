nome1 = "guilherme"
nome2 = "costa"
nome3 = "oliveira"


  

dicionario = {"q":1, "w":2, "e":3, "r":4, "t":5, "y":6, "u":7, "i":8, "o":9, "p":10, "á":11, "ã":12,
             "a":11, "s":9, "d":7, "f":5, "g":3, "h":1, "j":11, "k":9, "l":7, "ç":5, "é":3, "í":1, 
             "z":2,  "x":4, "c":6, "v":8, "b":10, "n":12, "m":2, "ó":4, "õ":6, "ô":8, "ẫ":10, "ê":12}

#Funcao para transformar o primeiro nome em numeros 
def converte(x):
    for l in dicionario:
        x = x.replace(l, str(dicionario[l]))
    return x    

nome1 = converte(nome1)     #O primeiro nome
nome1 = int(nome1)
resto1 = nome1 % 3
print(f'nome1: {nome1}')
print(f'resto1: {resto1}')

if resto1 == 0:
    alpha = 1
    beta = 0
    delta = -1

elif resto1 == 1:
    alpha = 2
    beta = 0
    delta = -1

elif resto1 == 2:
    alpha = 2
    beta = 0
    delta = -2

nome2 = converte(nome2)
nome2 = int(nome2)              #O último nome
resto2 = nome2 % 3
print(f'nome2: {nome2}')
print(f'resto2: {resto2}')

#0: os gaps devem ocorrer preferencialmente no início da sequência
#1: os gaps devem ocorrer preferencialmente no final da sequência
#2: os gaps devem ocorrer preferencialmente no meio da sequência

nome3 = converte(nome3)
nome3 = int(nome3)             #O nome do meio
resto3 = nome3 % 2
print(f'nome3: {nome3}')
print(f'resto3: {resto3}')

#0: os gaps juntos
#1: os gaps separados



#n = 378713423 #valor que deveria ser obtido com o primeiro nome
#resto = 76411 % 3
#print(resto)