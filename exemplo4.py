## DICIONARIO
brinquedo = {
    "marca" : "Estrela",
    "modelo" : "Boneca",
    "preco" :150
}

### QUANDO EU CRIAR UMA FUNCAO QUE NAO SEI A QUANTIDADE DE PARAMETROS QUE IRA RECEBER USAR O *ARGS

def my_func(param1, *args):
    print(param1)
    print(len(args))


my_func(12,14,16,18)

