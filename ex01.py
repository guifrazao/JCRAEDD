'''
Uma pesquisa sequencial de uma lista ordenada pode ser interrompida quando o alvo 
é menor que determinado elemento na lista. Defina uma versão modificada desse 
algoritmo e indique a complexidade computacional, usando a notação big-O, do 
desempenho nos casos melhor, pior e médio. 
'''

def sequential_search(lista, element):
    for c in range(len(lista)): 
        if element < lista[c]:  
            return False
        if element == lista[c]:
            print(f"Index = {c}")
                
def main():
    result = sequential_search([1,2,3,4,5], 4)
    print(result)

main()


'''
- pior caso = O(n)
- caso médio = O(n/2) = O(n)
- melhor caso = O(1)
'''