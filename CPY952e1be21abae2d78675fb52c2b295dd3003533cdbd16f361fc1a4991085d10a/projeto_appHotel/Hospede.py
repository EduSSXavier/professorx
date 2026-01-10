class Hospede:
    def __init__(self, nome, cpf, email=None, telefone=None):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.quarto_alocado = None

    def __str__(self):
        quarto = self.quarto_alocado.numero if self.quarto_alocado else "Não alocado"
        return f"{self.nome} (CPF: {self.cpf}) - Quarto: {quarto}"
