class Funcionario:
    def __init__(self, nome, cargo, disponivel=True):
        self.nome = nome
        self.cargo = cargo
        self.disponivel = disponivel

    def __str__(self):
        return f"Nome: {self.nome}\nCargo: {self.cargo}\nDisponível: {'Sim' if self.disponivel else 'Não'}"
