print("============ Tabela da Tabuada  ============")

# Cabeçalho
print("    ", end="")
for j in range(1, 11):
    print(f"{j:4}", end="")
print("\n" + "-" * 44)

# Corpo da tabela
for i in range(1, 11):
    print(f"{i:2} |", end="")  # número da linha
    for j in range(1, 11):
        print(f"{i*j:4}", end="")  # resultado formatado em 4 espaços
    print()  # quebra de linha

print("============= Fim da Tabela  ===============")
