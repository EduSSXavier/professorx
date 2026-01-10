class Quarto:
    def __init__(self, numero, tipo='standard', capacidade=2):
        self.numero = numero
        self.tipo = tipo
        self.ocupado = False
        self.hospede = None

    def alocar_hospede(self, hospede):
        if not self.ocupado:
            self.ocupado = True
            self.hospede = hospede
            hospede.quarto_alocado = self
            return True
        return False

    def liberar_quarto(self):
        if self.ocupado:
            self.hospede.quarto_alocado = None
            self.hospede = None
            self.ocupado = False

    def __str__(self):
        status = "Ocupado" if self.ocupado else "Disponível"
        ocupante = f" ({self.hospede.nome})" if self.ocupado else ""
        return f"Quarto {self.numero} ({self.tipo}) - {status}{ocupante}"
