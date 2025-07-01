frase = "Aprender Python é divertido e Python é muito poderoso.".lower().strip()

# Filtra só letras (sem espaços, sem pontuação)
so_letras = [c for c in frase if c.isalpha()]
i = set(so_letras)
a= sorted(i)

print("\nLista com apenas letras:")
print(a)
