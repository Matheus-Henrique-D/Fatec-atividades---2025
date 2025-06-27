frase = input(f"Digite uma frase e direi, se termina com obrigado ou começa com bom dia: ").lower().strip() 
#Pega o texto que o usuário digitou e remove todos os espaços em branco extras do início e do fim.
if frase.startswith('bom dia') and frase.endswith('obrigado'):
    print("Um bom dia e obrigado para voce")

elif frase.startswith('bom dia'):
    print("Um bom dia para você tambem")

elif frase.endswith('obrigado'):
    print("Obrigado você")

else:
    print("afff")
