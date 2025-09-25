
class Estudante: ##NOME DA CLASSE
    def __init__(self,nome,idade,nota): ##METODO CONSTRUTOR
        self.nome = nome ##ATRIBUTOS
        self.idade = idade
        self.nota = nota

    def get_grade(self):
        print(self.nota)




e1 = Estudante("Yan",20,10)
e2 = Estudante("José", 22,10)

print(e1)