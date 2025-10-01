class Produto:
    def __init__(self,nome,marca,modelo,preco):
        self.nome = nome
        self.marca = marca
        self.modelo = modelo
        self.preco = preco
        self.__inicia_prod()

    def get_nome(self):
        return self.nome

    def __inicia_prod(self):
        print("Produto inicializado com sucesso")    
        

prod1 = Produto("Notebook","Dell","Core i8",9500)
nome_prod = prod1.get_nome()
print(nome_prod)
