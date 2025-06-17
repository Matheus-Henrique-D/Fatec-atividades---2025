boletim = {
    "Ana": (8.0, 7.5),
    "Carlos": (5.0, 6.0),
    "Beatriz": (9.0, 8.5),
    "Daniel": (6.0, 6.5)
}

print("--- Situação Final dos Alunos ---")

for nome, notas in boletim.items():
    
    media = (notas[0] + notas[1]) / 2
    
    
    if media >= 7:
        situação = "Aprovado"
    else:
        situação = "Reprovado"
    
    print(f"{nome}: média {media:.1f} - Situação: {situação}")


