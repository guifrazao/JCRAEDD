from unorderedLinkedList import UnorderedLinkedList
ull = UnorderedLinkedList()
teste = {"name": "RECEBA", "link": "www.receba.com"}
teste2 = {"name": "DEVOLVA", "link": "www.devolva.com"}
teste3 = {"name": "RONALDO", "link": "www.ronaldo.com"}
ull.append(teste)
ull.append(teste2)
ull.append(teste3)
ull.print()
dado = ull.searchSite("DEVOLVA")
print(dado)
ull.print()
print(ull.head.data)
