compras = {
    "Sabonete": 2.50,
    "Shampoo": 15.00,
    "Condicionador": 16.50
}

#for item in compras.items(): se apenas uma variavel como só item ele retorna em formato de tupla
#for chave, valor in compras.keys(): ele funciona para dar somente o valor
for chave, valor in compras.items():
    print(f"{chave}: R$ {valor:.2f}")

"""Fonte:"""
#https://youtu.be/XVFFjEPp7jw?si=BDa6l0JmUhWrHiFa