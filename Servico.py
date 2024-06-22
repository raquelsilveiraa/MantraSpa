class Servico:
    def __init__(self, nome, descricao, beneficios, local, id=None):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.beneficios = beneficios
        self.local = local

    def __str__(self):
        return f"Nome: {self.nome}\nDescrição: {self.descricao}\nBenefícios: {self.beneficios}\nLocalização: {self.local}"

    @staticmethod
    def carregar_servicos(db):
        cursor = db.conn.execute("SELECT id, nome, descricao, beneficios, local FROM Servicos")
        servicos = [Servico(row[1], row[2], row[3], row[4], row[0]) for row in cursor.fetchall()]
        return servicos

    def salvar(self, db):
        with db.conn:
            if self.id is None:
                self.id = db.conn.execute('''
                    INSERT INTO Servicos (nome, descricao, beneficios, local)
                    VALUES (?, ?, ?, ?)
                ''', (self.nome, self.descricao, self.beneficios, self.local)).lastrowid
            else:
                db.conn.execute('''
                    UPDATE Servicos SET nome = ?, descricao = ?, beneficios = ?, local = ?
                    WHERE id = ?
                ''', (self.nome, self.descricao, self.beneficios, self.local, self.id))

    def deletar(self, db):
        with db.conn:
            db.conn.execute("DELETE FROM Servicos WHERE id = ?", (self.id,))
