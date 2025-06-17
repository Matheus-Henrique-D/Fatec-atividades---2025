def multiplo (valor1,valor2):
    if valor1 % valor2 == 0:        # % significa modulo e sempre retorna o resto da divisão bastante útil
        return True
    else:
        return False   

resposta=  multiplo(8,4)       #Pode ser interresante fazer em um formato de lista ao inves de 3 variaveis
resposta1= multiplo(7,4)
resposta2= multiplo(5,5)

print("Ele é", resposta)
print("Ele é",resposta1)
print("Ele é", resposta2)


