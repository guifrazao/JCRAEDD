"""
6. Faça um programa que cadastre n funcionários. Para cada funcionário devem ser
cadastrados nome e salário. Os dados devem ser armazenados em uma lista
simplesmente encadeada e ordenada, de forma decrescente, pelo salário do
funcionário. Posteriormente, o programa de mostrar:
a. O nome do funcionário que tem o maior salário (em caso de empate mostrar
todos);
b. A média salarial de todos os funcionários juntos;
c. A quantidade de funcionários com salário superior a um valor fornecido pelo
usuário. Caso nenhum funcionário satisfaça essa condição, mostrar
mensagem.
"""
from orderedLinkedList import OrderedLinkedList

def cadastro():
    linkedList = OrderedLinkedList()
    continuar = "s"
    while continuar == "s":
        try:  
            nome_func = input("Digite o nome do funcionário: ")
            salario = float(input("Digite o salário do funcionário: "))
            linkedList.insert({"name": nome_func, "salary": salario})
            continuar = input("Deseja cadastrar mais funcionários? [s/n]: ").lower()              
        except Exception as e:
            print(f"Erro: {e}, tente novamente")
            continue
 
    return linkedList
    
def imprimirListaMaiorSalarios(list):
    for funcionario in list:
        print(f"Nome: {funcionario['name']}, Salário: {funcionario['salary']}")


def imprimirDados(oll: OrderedLinkedList):
    print("\nFuncionário(s) que tem maior salário:")
    imprimirListaMaiorSalarios(oll.searchHighestSalaryEmployee())
    print(f"\nMédia salarial de todos os funcionários: {oll.getAverageSalary()}")
    qtd = float(input("Digite um salário: "))
    print(f"\nQuantidade de funcionários com salário maior que o informado: {oll.requisiteC(qtd)}")


def main():
    oll = cadastro()
    oll.print()
    imprimirDados(oll)

main()

