class Pessoa:
    def __init__(self, nome, cpf, fone, email, cidade, estado):
        self.nome = nome
        self.cpf = cpf
        self.fone = fone
        self.email = email
        self.cidade = cidade
        self.estado = estado

    def mostrar_dados(self):
        print("===== Dados da Pessoa =====")
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Telefone: {self.fone}")
        print(f"E-mail: {self.email}")
        print(f"Cidade: {self.cidade}")
        print(f"Estado: {self.estado}")
        print("===========================")


    def atualizar_fone(self, novo_fone):
        self.fone = novo_fone
        print(f"Telefone de {self.nome} atualizado para {self.fone}")


    def atualizar_email(self, novo_email):
        self.email = novo_email
        print(f"E-mail de {self.nome} atualizado para {self.email}")


    def __str__(self):
        return (f"{self.nome} | CPF: {self.cpf} | Telefone: {self.fone} | "
                f"E-mail: {self.email} | Cidade: {self.cidade}-{self.estado}")



p1 = Pessoa("Yan Torres", "123.456.789-00", "(67) 99999-9999", 
            "yan@email.com", "Campo Grande", "MS")

p2 = Pessoa("Maria Silva", "987.654.321-00", "(11) 98888-8888", 
            "maria@email.com", "São Paulo", "SP")


p1.mostrar_dados()
p2.mostrar_dados()


p1.atualizar_fone("(67) 91111-2222")
p2.atualizar_email("nova.maria@email.com")


print("\n--- Lista de Pessoas ---")
print(p1)
print(p2)
