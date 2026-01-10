class Hotel:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        self.quartos = {}
        self.hospedes = []

    def adicionar_quarto(self, quarto):
        if quarto.numero not in self.quartos:
            self.quartos[quarto.numero] = quarto
            return True
        return False

    def registrar_hospede(self, hospede):
        if not any(h.cpf == hospede.cpf for h in self.hospedes):
            self.hospedes.append(hospede)
            return True
        return False

    def buscar_hospede_por_cpf(self, cpf):
        return next((h for h in self.hospedes if h.cpf == cpf), None)

    def check_in(self, cpf, numero_quarto):
        hospede = self.buscar_hospede_por_cpf(cpf)
        quarto = self.quartos.get(numero_quarto)
        if not hospede:
            return "Erro: Hóspede não encontrado."
        if not quarto:
            return "Erro: Quarto não existe."
        if quarto.alocar_hospede(hospede):
            return f"Check-in realizado: {hospede.nome} no quarto {quarto.numero}."
        return "Erro: Quarto já está ocupado."

    def check_out(self, numero_quarto):
        quarto = self.quartos.get(numero_quarto)
        if not quarto:
            return "Erro: Quarto não existe."
        if quarto.ocupado:
            nome = quarto.hospede.nome
            quarto.liberar_quarto()
            return f"Check-out realizado: {nome} deixou o quarto {numero_quarto}."
        return "Quarto já está disponível."

    def listar_quartos_disponiveis(self):
        return [q for q in self.quartos.values() if not q.ocupado]

    def listar_quartos_ocupados(self):
        return [q for q in self.quartos.values() if q.ocupado]
