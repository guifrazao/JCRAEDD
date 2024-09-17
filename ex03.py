'''
A função pow retorna o resultado de elevar um número a determinada potência. 
Defina uma função expo que execute essa tarefa e indique a complexidade 
computacional usando a notação big-O. O primeiro argumento dessa função é o 
número e o segundo argumento é o expoente (apenas números não negativos). Você 
pode usar um laço em sua implementação, mas não use o operador ** do Python ou a 
função pow do Python. 
'''

def expo(base, exp):
    result = 1
    for c in range(exp):
        result *= base
    return result

def main():
    exponentiation = expo(2, 3)
    print(exponentiation)

main()

'''
O(n), n = exp
'''