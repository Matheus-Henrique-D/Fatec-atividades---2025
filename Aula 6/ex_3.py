cargos= {
    1:{'cargo': 'Escriturário', 'salario':2500, 'beneficio': 300, 'imposto':8}, 
    2:{'cargo': 'Secretário', 'salario':3200, 'beneficio': 450, 'imposto':10},              #Interresante um dicionario de dicionarios
    3:{'cargo': 'Caixa', 'salario':3800, 'beneficio': 600, 'imposto':12}, 
    4:{'cargo': 'Gerente', 'salario':7500, 'beneficio': 1000, 'imposto':15}, 
    5:{'cargo': 'Diretor', 'salario':12000, 'beneficio': 2000, 'imposto':20} 
}

def salario (salario_base,beneficios,imposto):
    imposto_valor = salario_base * (imposto/100)
    salario_liquido= salario_base + beneficios + imposto_valor
    return salario_liquido 

numero_cargo=int(input('Digite o número do cargo que quer saber: '))

if numero_cargo in cargos:
    cargo = cargos[numero_cargo]
    salario_final = salario(cargo['salario'], cargo['beneficio'], cargo['imposto'])
    print(f"\nCargo: {cargo['cargo']}")
    print(f"Salário líquido: R$ {salario_final:.2f}")
else:
    print("Código inválido. Digite um número de 1 a 5.")

