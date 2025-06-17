#Primeira tentativa

numeros = [10, 3, 5, 7, 2, 8, 12]
ordem= sorted(numeros)
maior= (ordem[-1] + ordem[-2] + ordem[-3])
menor= (ordem[0] + ordem[1] + ordem[2])
print(f" A maior soma é de {maior}")
print(f"A menor soma é de {menor}")

#Segunda maneira
""""""
# 2. Calcula a soma dos maiores
#    - ordem[-3:] cria a lista [8, 10, 12]
#    - sum() soma os elementos dessa nova lista
soma_maiores = sum(ordem[-3:])

# 3. Calcula a soma dos menores
#    - ordem[:3] cria a lista [2, 3, 5]
#    - sum() soma os elementos dessa nova lista
soma_menores = sum(ordem[:3])

# 4. Imprime o resultado no formato exato do exercício
print(f"{soma_maiores} {soma_menores}")

""""""