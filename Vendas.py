class Vendas:
    def __init__(self, db):
        self.db = db
        self.fluxo_de_caixa = self.carregar_vendas()

    def carregar_vendas(self):
        cursor = self.db.conn.execute("SELECT valor, servico FROM Vendas")
        return [{"valor": row[0], "servico": row[1]} for row in cursor.fetchall()]

    def registrar_venda(self, valor, servico):
        with self.db.conn:
            self.db.conn.execute('''
                INSERT INTO Vendas (valor, servico)
                VALUES (?, ?)
            ''', (valor, servico.nome))
        self.fluxo_de_caixa.append({"valor": valor, "servico": servico.nome})
        return "Venda registrada com sucesso."

    def exibir_fluxo_de_caixa(self):
        return [f"Serviço: {venda['servico']}, Valor: R${venda['valor']}" for venda in self.fluxo_de_caixa]
