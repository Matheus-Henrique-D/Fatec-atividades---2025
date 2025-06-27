frase= input("Digite aqui sua frase: ").lower()
# A rápida raposa marrom salta sobre o cão preguiçoso
print("O total a seguir de vogais foi")

a= frase.count('a') + frase.count ('á') + frase.count ('à') + frase.count ('ã') + frase.count ('â')
print(f"A quantia de A é: {a}")
e=frase.count('e') + frase.count ('é') + frase.count ('è')  + frase.count ('ê')
print(f"A quantia de E é: {e}")
i=frase.count('i') + frase.count ('í') + frase.count ('ì') + frase.count ('î') 
print(f"A quantia de I é: {i}")
o=frase.count('o') + frase.count ('ó') + frase.count ('ò') + frase.count ('õ') + frase.count ('ô')
print(f"A quantia de O é: {o}")
u=frase.count('u') + frase.count ('ú') + frase.count ('ù') + frase.count ('û') 
print(f"A quantia de U é: {u}")