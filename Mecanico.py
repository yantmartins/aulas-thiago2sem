class Mecanico:
    def __init__(self,nome,matricula,nivel):
        self.nome = nome
        self.matricula = matricula
        self.nivel = nivel
        self.nome = nome
        self.salario = 0

    def passar_orcamento(self):
        print("Seu carro ficou tanto.....")

    def realizar_diagnostico(self):
        print(f"{self.nome} diagnosticando o veículo")       

    def get_salario(self):
        return self.salario

    def set_salario(self, valor):
        self.salario = valor

mec1= Mecanico("Yan","1234", "n1")
mec1.passar_orcamento()    
mec1.realizar_diagnostico()
sal = mec1.get_salario()
print(f"Salário atual: {sal}")
mec1.set_salario(5000)

sal2 = mec1.get_salario()
print(f"Novo salário: {sal2}")

mec2 = Mecanico("Maria","67890","n2")