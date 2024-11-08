"""
4. Faça um programa que cadastre n produtos. Para cada produto devem ser
cadastrados os seguintes dados: código, descrição e preço. Use um método de
ordenação e em seguida calcule e mostre quantas comparações devem ser feitas
para encontrar um funcionário pelo código:
a. Usando busca sequencial.
b. Usando busca binária.
"""

from modules import pesquisaLR_estruturado
from modules import pesquisaBR_estruturado
from modules import quicksort

def cadastro():
    lista_produtos = []
    cadastrar = True
    while cadastrar:
        try:
            produto = []

            codigo = int(input("Informe o código do produto: "))
            descricao = input("Informe a descrição do produto: ")
            preco = float(input("Informe o preço do produto: "))

            produto.append(codigo)
            produto.append(descricao)
            produto.append(preco)

            lista_produtos.append(produto)

            cadastrar = True if input("Deseja continuar cadastrando produtos? [s/n]: ").lower() == "s" else False
        except Exception as e:
            print(f"Erro: {e}, tente novamente")
    
    return lista_produtos

def main():
    lista_produtos = cadastro()
    quicksort(lista_produtos)
    codigo = int(input("Codigo: "))
    index = -1
    for produto in lista_produtos:
        if produto[0] == codigo:
            index = lista_produtos.index(produto)
    
    linear = pesquisaLR_estruturado(lista_produtos[index], lista_produtos)
    binaria = pesquisaBR_estruturado(lista_produtos[index], lista_produtos)

    print(lista_produtos)
    print("PESQUISA LINEAR: ")
    print(f"Índice do funcionário na lista: {linear[0]}, iterações: {linear[1]}")
    print("PESQUISA BINÁRIA: ")
    print(f"Índice do funcionário na lista: {binaria[0]}, iterações: {binaria[1]}")

main()


