class Servico:
    def __init__(self, nome, descricao, beneficios,local):
        self.nome = nome
        self.descricao = descricao
        self.beneficios = beneficios
        self.local=local

    def __str__(self):
        return f"Nome: {self.nome}\nDescrição: {self.descricao}\nBenefícios: {self.beneficios}\n Localização: {self.local}"
