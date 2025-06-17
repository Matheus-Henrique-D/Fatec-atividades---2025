def inteiro_para_romano(numero_para_converter):
    # AJUSTE 2: Dicionário na ordem DECRESCENTE, do maior para o menor.
    romanos_map = {
        1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C",
        90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V",
        4: "IV", 1: "I"
    }
    
    # AJUSTE 3: Usando um nome de variável consistente.
    resultado_romano = ""
    
    # O loop for para percorrer o dicionário
    for valor, simbolo in romanos_map.items():
        while numero_para_converter >= valor:
            # Usando a variável correta para construir o resultado
            resultado_romano += simbolo
            numero_para_converter -= valor
            
    # AJUSTE 1: 'return' está FORA do loop 'for', mas ainda DENTRO da função.
    # Repare na indentação (recuo) correta.
    return resultado_romano

# --- Parte principal do programa (está correta!) ---
try:
    numero_usuario = int(input("Digite um número inteiro entre 1 e 3999: "))
    
    if 1 <= numero_usuario <= 3999:
        romano = inteiro_para_romano(numero_usuario)
        print(f"O número {numero_usuario} em romanos é: {romano}")
    else:
        print("Erro: O número precisa estar no intervalo de 1 a 3999.")
        
except ValueError:
    print("Erro: Por favor, digite um número inteiro válido.")