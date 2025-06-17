curso_a = {("Ana", 101), ("Carlos", 102), ("João", 103)}
curso_b = {("João", 103), ("Marina", 104), ("Carlos", 102)}

interseção = curso_a & curso_b
print("Exclusivo curso A")
print(curso_a.difference(curso_b))
print("Exclusivo curso B")
print(curso_b.difference(curso_a))
print("Ambos")
print(interseção)


# Método 2

# Seus cálculos (que estão perfeitos)
exclusivos_a = curso_a.difference(curso_b)
exclusivos_b = curso_b.difference(curso_a)
ambos_cursos = curso_a & curso_b

# O passo de formatação que faltava
print("Exclusivos do curso A:")
for nome, matricula in exclusivos_a:
    print(f"{nome} ({matricula})")

print("\nExclusivos do curso B:")
for nome, matricula in exclusivos_b:
    print(f"{nome} ({matricula})")

print("\nMatriculados nos dois cursos:")
for nome, matricula in ambos_cursos:
    print(f"{nome} ({matricula})")