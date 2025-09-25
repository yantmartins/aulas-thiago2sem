
class Dog:
    def __init__(self,nome,peso,cor):
        self.nome = nome
        self.peso = peso
        self.cor = cor


    def latir(self):
        print(f"{self.nome} AU AU AU")   

    def comer(self):
        print(f"{self.nome} comendo.........") 

dog1 = Dog("TOTO",35,"Caramelo")           
dog2 = Dog("Charlene",22,"Branca")
print("Peso do TOTO", dog1.peso)
dog1.latir()