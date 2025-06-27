# Linha 1: Definindo os Caracteres
caracteres_especiais = "!@#$%&*"

# Linha 2: O Loop Principal
while True:
    # Linha 3: Capturando a Senha
    senha = input("Digite uma senha: ").strip()
    
    # Linha 4: A Lista de Erros
    erros = []

    # Linha 5: Verificação do Comprimento
    if len(senha) < 8:
        erros.append("A senha precisa ter pelo menos 8 caracteres.")

    # Linha 8: Verificação do Caractere Especial
    if not any(char in caracteres_especiais for char in senha):
        erros.append(f"A senha precisa conter um caractere especial ({caracteres_especiais}).")

    # Linha 11: A Validação Final
    if not erros:
        print("\n✅ Senha aceita!")
        break
    else:
        print("\n❌ Senha inválida:")
        for erro in erros:
            print(f"   - {erro}")
        print("-" * 30)