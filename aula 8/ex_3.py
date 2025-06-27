frase = input("Digite a frase:").lower().strip()
#Eu gosto de comer feijoada com farinha
procura = input("Agora qual palavra você quer procurar? ")

posiçao= frase.find(procura)   # O FIND retorna apenas a posição da palavra e caso não encontre retorna -1

if posiçao != -1:  # Se a posição for diferente de -1, a palavra foi encontrada!
    print(f"\n✅ Sim! A palavra '{procura}' foi encontrada.")
    print(f"   Ela aparece pela primeira vez na posição {posiçao}.")
else: # Se a posição for igual a -1, a palavra não foi encontrada.
    print(f"\n❌ Não. A palavra '{procura}' não existe na frase que você digitou.")