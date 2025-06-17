'''exercício 1'''
nome= "Matheus"
idade= 25
altura= 1,70

'''exercício 2'''
print(f"meu nome é  {nome}, tenho {idade} e tenho {altura} metros de altura.")

Número1= 500
Número2= 2000

print(f"A soma de {Número1} e {Número2} é igual a {Número1 + Número2}.")

'''exercício 3'''
primeiro_nome= input('digite seu primeiro nome:')
sobrenome= input('digite seu sobrenome:')

print(f"Olá, {primeiro_nome} {sobrenome}! Seja bem-vindo(a)!")

'''exercício 4'''
idade_atual= int(input("digite sua idade atual:"))
idade_futura= idade_atual + 10

print(f"Hoje você tem {idade_atual} anos. Daqui a 10 anos, terá {idade_futura} anos.")

'''exercício 5'''
numero= int(input("digite um número que venha na sua cabeça:"))
palavra= input("Agora digite uma palvra:")

print(f"{numero * palavra}")

'''exercício 6'''
nota1 = float(input("digite sua primeira nota:"))
nota2 = float(input("digite sua segunda nota:"))
nota3 = float(input("digite sua terceira nota:"))

média= (nota1+ nota2+ nota3) /3

print(f"A média das notas é: {média:.2f}")

'''exercício 7'''
nome_usuario= input("digite seu nome:")
ano_nascimento= input("digite seu ano de nascimento:")


print(f"{nome_usuario}{ano_nascimento}")

'''exercício 8'''
preço_original= float(input("digite o preço do alimento:"))
desconto1= 0.10

desconto_final= (preço_original * desconto1)
valor_real_final= (preço_original- desconto_final)
print(f"O alimento que custava {preço_original}, recebeu um desconto de {desconto1}, ficando com o preço final de {valor_real_final}.")

'''exercício 9'''

graus_celsius= 38
transformação_fahrenheit= (graus_celsius*9/5)+32

print(f"A temperatura de {graus_celsius}°C corresponde a {transformação_fahrenheit}°F")

'''exercício 10'''

nome= input("Digite seu nome:")
evento= input("E o evento na qual quer ir:")

print(f"Olá, {nome}! Você está convidado(a) para o(a) {evento}. Esperamos por você!")