frase =input("Digite a frase: ") 
#"Enquanto a inevitável marcha do tempo nos empurra para um futuro incerto e repleto de inovações tecnológicas que antes pertenciam apenas à ficção científica, ainda buscamos, nos pequenos gestos e nas conexões humanas mais simples, a âncora de serenidade que nos lembra de nossa própria e imutável essência".lower().split()

lista=[]
for items in sorted(set(frase), key=len):
    lista.append(items)

print(lista[0:48])

