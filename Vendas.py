class Vendas:
    def __init__(self):
        self.fluxo_de_caixa = []

    def registrar_venda(self, valor, servico):
        self.fluxo_de_caixa.append({"valor": valor, "servico": servico.nome})
        return "Venda registrada com sucesso."

    def exibir_fluxo_de_caixa(self):
        registros = []
        if self.fluxo_de_caixa:
            for venda in self.fluxo_de_caixa:
                registros.append(f"Serviço: {venda['servico']}, Valor: R${venda['valor']}")
        return registros
