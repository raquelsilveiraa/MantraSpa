class Vendas:
    def __init__(self, db):
        self.db = db
        self.fluxo_de_caixa = self.carregar_vendas()

    def carregar_vendas(self):
        cursor = self.db.conn.execute("SELECT id, valor, servico FROM Vendas")
        return [{"id": row[0], "valor": row[1], "servico": row[2]} for row in cursor.fetchall()]

    def registrar_venda(self, valor, servico):
        with self.db.conn:
            self.db.conn.execute('''
                INSERT INTO Vendas (valor, servico)
                VALUES (?, ?)
            ''', (valor, servico.nome))
        self.fluxo_de_caixa.append({"id": self.db.conn.lastrowid, "valor": valor, "servico": servico.nome})
        return "Venda registrada com sucesso."

    def exibir_fluxo_de_caixa(self):
        return [{"id": venda["id"], "texto": f"Serviço: {venda['servico']}, Valor: R${venda['valor']}"} for venda in self.fluxo_de_caixa]

    def remover_venda(self, venda_id):
        with self.db.conn:
            self.db.conn.execute('DELETE FROM Vendas WHERE id = ?', (venda_id,))
        self.fluxo_de_caixa = [venda for venda in self.fluxo_de_caixa if venda["id"] != venda_id]
