def numero (N):
    
    def soma_pilha(N):
        if N <= 0:
            return 0
        else:
            return N + pilha_soma(N - 1)

    pilha = []

    for i in range(N, 0, -1):
        pilha.append(i)

    resultado = 0
  
    while pilha:
        resultado += pilha.pop()

    return resultado

N = int(input("Digite um número inteiro: "))

if N <= 0:
    print("Digite um numero inteiro! ")
else:
    resultado = numero (N)
    print(f'A soma dos primeiros {N} números inteiros positivos é {resultado}')

print ("\n")

#2
def fatorial(n, pilha=[]):
    if n == 0:
        return 1
    
    pilha.append(n)
    resultado = n * fatorial(n - 1, pilha)
    pilha.pop()
    
    return resultado

n = 5
resultado = fatorial(n)
print(f'O fatorial de {n} é {resultado}')

print ("\n")

#3
def invr_string(string):
    pilha = []   
    
    for char in string:
        pilha.append(char)
 
    invercao_string = ""
    
    while pilha:
        invercao_string += pilha.pop()
    
    return invercao_string
 
string = "Programação"
string_invertida = invr_string(string)
print(string_invertida)

print ("\n")

#4
def convercao (decimal):
    pilha = []  
    
    if decimal == 0:
        pilha.append(0)
    
    while decimal > 0:
        pilha.append(decimal % 2)   
        decimal //= 2   
    
    representacao_binaria = ""
    
    while pilha:
        representacao_binaria += str(pilha.pop())
    
    return representacao_binaria

numero_decimal = 25
representacao_binaria = convercao (numero_decimal)
print(f'A representação binária de {numero_decimal} é {representacao_binaria}')
