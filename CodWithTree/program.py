#######################################################################
# Necessaria a instalacao do biopython (pip install biopython)
from Bio import pairwise2
from Bio.pairwise2 import format_alignment 
from Bio.Seq import Seq


ROOT = "root"

class Node:
    def __init__(self, data = None, tudo = None, seq1 = None, seq2 = None):
        self.data = data
        self.seq1 = seq1
        self.seq2 = seq2
        self.tudo = tudo
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self, data=None, tudo=None, node=None):
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

class BinarySearchTree(BinaryTree):
    
    def insert(self, value):
        parent = None
        x = self.root
        while(x):
            parent = x
            if value < x.data:
                x = x.left
            else:
                x = x.right
        if parent is None:
            self.root = Node(value)
        elif value < parent.data:
            parent.left = Node(value)
        else:
            parent.right = Node(value)

    def simetric_transversal(self, node = None):
        if node is None:
            node = self.root
        if node.left:
            self.simetric_transversal(node.left)
        print(node)
        if node.right:
            self.simetric_transversal(node.right)              

    def add(self, node):
        if node.value < self.value:
            if self.left is None:
                self.left = node
            else:
                self.left.add(node)
        else:
            if self.right is None:
                self.right = node
            else:
                self.right.add(node)

    def max(self, node = ROOT):
        if node == ROOT:
            node = self.root
        while node.right:
            node = node.right
        return node.data

    def min(self, node=ROOT):
        if node == ROOT:
            node = self.root
        while node.left:
            node = node.left
        return node.data


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

if resto1 == 0:
    alpha = 1
    beta = 0
    delta = -1

elif resto1 == 1:
    alpha = 2
    beta = 0
    delta = -1

elif resto1 == 2:
    alpha = 1
    beta = 0
    delta = -2

print(f'alpha: {alpha}')
print(f'beta: {beta}')
print(f'delta: {delta}')

nome2 = converte(nome2)
nome2 = int(nome2)              #O último nome
pref_gap = nome2 % 3

nome3 = converte(nome3)
nome3 = int(nome3)             #O nome do meio
gap_js = nome3 % 2

#Obs: lembrar que esses valores sao para teste

matrix = []
print("Entrada e enter:")
for i in range(1):          # loop para linhas                 
    a = []
    for j in range(3):      # loop para colunas               
         a.append(str(input()))
    matrix.append(a)

seq1 = matrix[0][0]
seq2 = matrix[0][1]
seq3 = matrix[0][2]
seqt = []
seqt = [seq1, seq2, seq3]

score = 0
scoreaux = 0
count1 = 0
count2 = 0

n = 3     # numero de sequencias
k = 0


while n > 0:
    if n == 3:# eh reduzido 0.5 do score a cada gap consecutivo, ou seja, as sequencias com gaps separados podem ter maior score, assim cumprindo a condicao de que os gaps sejam separados
        alignments = pairwise2.align.globalms(seqt[k], seqt[k + 1], alpha, beta, delta, -0.5)
        for alignment in alignments:
            if count1 == 0:
                seqt[k] = alignment.seqA
                seqt[k + 1] = alignment.seqB
                score = alignment.score
                count1 = count1 + 1
                
                tudo = alignment
                tree = BinarySearchTree(alignment) #raiz, arvore q vai conter os alinhamentos das duas primeiras sequencias
                tree.seq1 = alignment.seqA
                tree.seq2 = alignment.seqB
                tree.tudo = alignment
                
                for alignment in alignments:
                    BinarySearchTree.insert(tree, alignment)
                    tree.seq1 = alignment.seqA
                    tree.seq2 = alignment.seqB
                    tree.tudo = alignment
                break
            else:
                BinarySearchTree.insert(tree, alignment.score)
                tree.seq1 = alignment.seqA
                tree.seq2 = alignment.seqB
                
        n = n - 2
        k = k + 1
        alignmax1 = BinarySearchTree.max(tree)
    else:
        alignments = pairwise2.align.globalms(seqt[k], seqt[k + 1], alpha, beta, delta, -0.5)        
        for align in alignments: 
            if count2 == 0:
                seqt[k] = align.seqA
                seqt[k + 1] = align.seqB
                scoreaux = align.score
                count2 = count2 + 1

                tudo = align
                tree1 = BinarySearchTree(align)
                tree1.seq1 = align.seqA
                tree1.seq2 = align.seqB
                tree1.tudo = align

                for align in alignments:
                    BinarySearchTree.insert(tree1, align)
                    tree1.seq1 = align.seqA
                    tree1.seq2 = align.seqB
                    tree1.tudo = align
                break
            else:    
                BinarySearchTree.insert(tree1, align.score)
                tree1.seq1 = align.seqA
                tree1.seq2 = align.seqB
                BinarySearchTree.simetric_transversal(tree1)
        n = n - 2
        k = k + 1
        alignmax2 = BinarySearchTree.max(tree1)
        
print("-----------------------------------------")
print(f'Sequencia final: {seqt[0]}')
print(f'Sequencia final: {seqt[1]}')
print(f'Sequencia final: {seqt[2]}')
print(f'Score Total: {alignmax1.score + alignmax2.score}')
