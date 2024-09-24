'''O melhor server de mine é o server dos guris
Matheus >>> Kauã
Data: 02/07/2024
'''
#---> Comentario de linha com hashtag é so anotação em 1 linha
# Deus salve os bons

print('Hello World')

# Saída --> print ()
print('Galinho furry safado') # "string"
print('100+100=') # "string"
print(100+100) # "operação"

# Entrada --> input()
galão = input('O galinho é safado? ')
print('Sua resposta a pergunta "O galinho é safado?" foi:', galão)
valor1 = int(input('Chute quantos r34 furry o galinho tem no PC dele: '))
valor2 = int(input('Ele tem mais, chute mais um valor pq eu vou soma-los: '))
total = valor1 + valor2
print('A soma dos seus chutes foram: ', total,
'. Você passou longe, galinho tem muito mais r34 furry que isso em seu pc...')

# Varíaveis --> Espaço de memória que armazena valores temporariamente
# str --> Armazena textos e caracteres --> %s ou %c
nome = 'Galinho'
print('A variáel nome é do tipo: ', type(nome), 'e tem armazenado o valor: %s' %nome)
# Int --> Armazena numeros interos positivos e nagativos
ValorX = -81
pi = 3.14159
print('A variável ValorX é do tipo ', type(ValorX), 'e tem armazenado o valor: %d' %pi)
# float --> Armazena números de ponto flutuante posivos e negativos --> NÃO USA VIRGULA, USA PONTO! -->


# bool --> Armazena "True" ou "False"

# Operadores --> Aritiméticos para calculos (+, -, *, /, **, // e %)
print(5*5)
print(15/4) # resultado float
print(10//3) # resultado int
print(10%4)
# Operadores --> Atribuição para ver se é True ou False
A = 10 # (Recebe)
A += 1 # Incremento soma 1
A -= 1 # Decremento diminui 1
# Operadores --> Relacionais fazem comparações e retornam True ou False
A == 10 #( == é igual == True)
A != 10 #( Diferente == False)
# >; <; >+; <=
# Operadores --> Lógicos para concatenação de operadores relacionais (and == e; or == ou; not == não)

# Repetição --> Laço for para quando eu sei quantas vezes vai repetir
for i in range(11, 102, 2): 
  print(i)

palavra = 'Galinhosafadãofurry'
for letra in palavra:
  print(letra)

tecla = 1
while tecla != 0: # Repete até a condição ser False
  tecla = int(input('Digite um número: '))

# Condição --> if; else; elif
Furry = int(input('O quão furry vc é?: '))
if Furry >= 1000000: # Ve se o resultado é True
  print('Comparável ao galinho')
elif Furry >= 100000: # Vê se o if == False e o elif == True
  print('Tá perto de ser comparavel ao galinho')
else: #Ve se o resultado do if é == a False
  print('Não chega nem a ser compáravel ao galinho')

# Funções --> def
def soma(X, Y):
  R = X + Y
  return R

print(soma(10, 5 ))
print(soma(100, 50))
A = int(input('Digite um valor: '))
B = int(input('Digite outro valor: '))
print('Soma de %d e %d é igual a %d' %(A, B, (soma(A.B))))