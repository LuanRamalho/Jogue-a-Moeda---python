import random

# Inicializa contadores
cara = 0
coroa = 0

# Simula 1000 jogadas
for _ in range(1000):
    if random.choice(["cara", "coroa"]) == "cara":
        cara += 1
    else:
        coroa += 1

# Exibe os resultados
print(f"Quantidade de vezes que deu cara: {cara}")
print(f"Quantidade de vezes que deu coroa: {coroa}")
input()