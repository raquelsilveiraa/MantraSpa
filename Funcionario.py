class Funcionario:
    def __init__(self, nome, cargo, disponivel=True, id=None):
        self.id = id
        self.nome = nome
        self.cargo = cargo
        self.disponivel = disponivel

    def __str__(self):
        return f"Nome: {self.nome}\nCargo: {self.cargo}\nDisponível: {'Sim' if self.disponivel else 'Não'}"

    @staticmethod
    def carregar_funcionarios(db):
        cursor = db.conn.execute("SELECT id, nome, cargo, disponivel FROM Funcionarios")
        funcionarios = [Funcionario(row[1], row[2], bool(row[3]), row[0]) for row in cursor.fetchall()]
        return funcionarios

    def salvar(self, db):
        with db.conn:
            if self.id is None:
                self.id = db.conn.execute('''
                    INSERT INTO Funcionarios (nome, cargo, disponivel)
                    VALUES (?, ?, ?)
                ''', (self.nome, self.cargo, self.disponivel)).lastrowid
            else:
                db.conn.execute('''
                    UPDATE Funcionarios SET nome = ?, cargo = ?, disponivel = ?
                    WHERE id = ?
                ''', (self.nome, self.cargo, self.disponivel, self.id))

    def deletar(self, db):
        with db.conn:
            db.conn.execute("DELETE FROM Funcionarios WHERE id = ?", (self.id,))
