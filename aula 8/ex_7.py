'''
 Peça uma palavra e mostre-a de trás para frente.
 Depois diga se ela é um palíndromo (lê igual de trás pra frente).
 Dica: Use slicing [::-1].
'''

# 1. Pede a palavra ao usuário e já a prepara
#    .strip() remove espaços extras nas pontas
#    .lower() converte para minúsculas para a comparação do palíndromo ser justa
palavra = input("Digite a palavra: ").strip().lower()

# 2. Inverte a palavra usando slicing
#    A sintaxe [::-1] significa "comece do início, vá até o fim, em passos de -1"
palavra_invertida = palavra[::-1]

# 3. Mostra a palavra invertida para o usuário
print(f"A palavra de trás para frente é: {palavra_invertida}")

# 4. Compara a palavra original com a invertida para ver se é um palíndromo
if palavra == palavra_invertida:
    print("✅ Sim! Esta palavra é um palíndromo.")
else:
    print("❌ Não. Esta palavra não é um palíndromo.")