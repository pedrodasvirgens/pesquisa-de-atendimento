# Pesquisa de opinião para satisfação de atendimento. 

excelente = 0
ruim = 0

for i in range(1, 51):
    print(f"\n--- Entrevistado {i} ---")

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    print("Opinião sobre o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opinião = int(input("Digite a opção: "))

    if opinião == 1:
        excelente += 1
    elif opinião == 2:
        pass
    elif opinião == 3:
        ruim += 1

print("\n===== RESULTADO DA PESQUISA =====")
print(f"Quantidade de respostas EXCELENTE: {excelente}")
print(f"Quantidade de respostas RUIM: {ruim}")
