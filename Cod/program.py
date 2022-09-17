from calendar import c
import string
from tokenize import String

first_name = "guilherme"

list_Fname = list(first_name)
  

dicionario = {"q":1, "w":2, "e":3, "r":4, "t":5, "y":6, "u":7, "i":8, "o":9, "p":10, "á":11, "ã":12,
             "a":11, "s":9, "d":7, "f":5, "g":3, "h":1, "j":11, "k":9, "l":7, "ç":5, "é":3, "í":1, 
             "z":2,  "x":4, "c":6, "v":8, "b":10, "n":12, "m":2, "ó":4, "õ":6, "ô":8, "ẫ":10, "ê":12}


## entrada de Linhas de DNA
lin = 10
linha = []
matriz = []
print("Escreva uma linha de DNA e dê enter para escrever a próxima: ")
a = []
for j in range(lin):
    a.append(str(input()))
    if (len(a[j])) == 10:#no lugar do 10 é100      
        matriz.append(list(a[j]))

for i in range(10):
    for j in range(10):
        print(matriz[i][j])
    print()








#n = 378713423  #Nome: Guilherme
#resto = n % 3
#print(resto)
