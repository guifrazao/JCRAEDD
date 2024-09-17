'''
Uma estratégia alternativa para a função expo usa a seguinte definição recursiva: 
expo(número, expoente) 
= 1, quando expoente = 0. 
= número * expo(número, expoente – 1), quando o expoente é ímpar. 
= (expo(número, expoente / 2))2, quando o expoente é par. 
Defina uma função recursiva expo que usa essa estratégia e indique sua 
complexidade computacional usando a notação big-O. 
'''

def expo(base, exp):
    if exp == 0:
        return 1
    elif (exp % 2 == 1):
        return base * expo(base, exp - 1) # recursive call
    else:
        half = (expo(base, (exp / 2))) # recursive call
        return half * half

def main():
    result = expo(2, 8)
    print(result)

main()

'''
O(log n)
'''