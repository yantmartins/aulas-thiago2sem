
pessoa = {
    "nome" : "Yan",
    "idade" : 26,
    "cidade" : "Campo Grande"
}

def verifica_cidade(dicionario):
    if dicionario["cidade"] == "SP":
        return "É de CG"
    else:
        return f"É de {dicionario["cidade"]}"
    
cidade_yan = verifica_cidade(pessoa)    
print(cidade_yan)

## FUNÇÃO PARA IMPRIMIR LISTAS
def imprime_listas(lista):
    for item in lista:
        print(item)

frutas = ["Banana","Maçã","Pera","Uva","Salada Mista"]
carros = ["Gol", "Corsa","Celta","Chevette","Fusca"] 
tupla = (33,44,55,66,77,88,99,0)

##imprime_listas(tupla)
