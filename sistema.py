from Produto import Produto

lista_prods = []
i = 0

while i < 5:
    nome = input("Digite o nome do produto: ")
    marca = input("Digite a marca do produto: ")
    modelo = input("Digite o modelo do produto: ")
    preco = input("Digite o preco do produto: ")
    prod = Produto(nome,marca,modelo,preco)
    lista_prods.append(prod)
    i += 1

for item in lista_prods:
    print(item.mostrar_dados())    

