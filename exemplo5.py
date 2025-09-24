
pessoa = {}

pessoa['nome'] = 'Yan'
pessoa['cidade'] = 'CG'


print(pessoa)

def cria_dicionario(**kwargs):
    for key,value in kwargs.items():
        print(key,value)

##CHAMADA DE FUNÇÃO COM PARAMETROS NOMEADOS
cria_dicionario(nome = "Yan", idade=26,city="Campão")
