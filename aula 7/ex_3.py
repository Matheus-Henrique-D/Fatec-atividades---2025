lista_produtos = ["maçã", "banana", "laranja", "maçã", "uva", "banana", "abacaxi"]

print(f"Lista original de produtos: {lista_produtos}")


produtos_unicos = set(lista_produtos)

print(f"Produtos únicos (em formato de conjunto): {produtos_unicos}")


lista_produtos_sem_repeticao = list(produtos_unicos)
print(f"Lista de produtos sem repetição (ordem não garantida): {lista_produtos_sem_repeticao}")

print(f"\nNúmero de produtos originais: {len(lista_produtos)}")
print(f"Número de produtos únicos: {len(produtos_unicos)}")