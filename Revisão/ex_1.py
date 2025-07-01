# --- Parte 1: Lógica para contar as palavras (a mesma de antes) ---

# Cria um dicionário vazio para as contagens.
frequencia = {}

# Pede a frase ao usuário e a prepara.
frase_usuario = input("Digite uma frase: ").strip().lower()

# Quebra a frase em uma lista de palavras.
lista_de_palavras = frase_usuario.split()

# O loop para contar, usando o método .get()
for palavra in lista_de_palavras:
    frequencia[palavra] = frequencia.get(palavra, 0) + 1


# --- Parte 2: Apresentando o resultado no formato desejado ---

print("\n--- Frequência de cada palavra ---")

# O .items() nos dá acesso tanto à chave (palavra) quanto ao valor (contagem)
for palavra, contagem in frequencia.items():
    # Usamos uma f-string para formatar cada linha
    # A palavra é a chave e a contagem é o valor
    print(f"'{palavra}': {contagem}")