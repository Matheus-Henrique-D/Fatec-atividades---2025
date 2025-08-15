class aluno:
# __init__  chamado de consultor, permite a construção inicial
# da classe
    def __init__(self,nome,altura,idade,peso,cor_do_olho,personalidade,sexo):
#Self serve para acessar as propriedades de uma instância
        self.nome = nome
        self.altura = altura
        self.idade = idade
        self.peso = peso
        self.cor_do_olho = cor_do_olho
        self.personalidade = personalidade
        self.sexo = sexo
    
    def apresentar(self):
        print(f"Olá aluno {aluno1.nome}")

    def calcular_imc(self):
            if self.peso == None and self.altura == None:
                print("Deu errado chefe")
            IMC = self.peso / (self.altura ** 2)
            return IMC
    
aluno1= aluno('Karl', 1.70, 17, 80, 'marron', 'introvertida', '  Masculino')
aluno2 = aluno('Diana', 1.55, 14, 45,'Azul','extrovertida','feminino')

