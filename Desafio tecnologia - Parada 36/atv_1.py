import os, openpyxl

planilha = openpyxl.Workbook()
page = planilha ['Sheet']
page.title = 'Lista de Alimentos'

alimentos =int(input("Digite quantos alimentos comprará:"))

page.append(['ALIMENTO', 'QUANTIDADE', 'PREÇO'])

for x in range(alimentos):
    Alimento = input("Digite o nome do alimento:")
    Quantidade = int(input("Digite a quantidade:"))
    Preço = float(input("Digite o preço:"))
    print("")
    page.append([Alimento, Quantidade, Preço])

planilha.save("Lista de Alimentos.xlsx")

print("Planilha criada com sucesso!")
os.system("pause")