
class Estudante: ##NOME DA CLASSE
    def __init__(self,nome,idade,nota): ##METODO CONSTRUTOR
        self.nome = nome ##ATRIBUTOS
        self.idade = idade
        self.nota = nota

    def get_grade(self):
        print(self.nota)    