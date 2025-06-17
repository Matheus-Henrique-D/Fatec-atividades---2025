        # Qualquer nome numa lista precissa estar com ''
meses = ['Janeiro', 'Fevereiro' , 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
                                                                # O formato de dicionario cai melhor para esse exercicio
dia = int(input("Digite o dia que você quiser: "))
mes = int (input("Agora o mês (1 a 12): "))
if 1 <= mes <= 12:
    print(f"O mês correspondente é: {meses[mes - 1]}")
    ano = int(input("E por fim o ano: "))
    print(f"Você está no dia {dia} de {meses[mes - 1]} no ano de {ano}.")
else:
    print("Número inválido. Digite de 1 a 12.")