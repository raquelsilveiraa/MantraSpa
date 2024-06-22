
from datetime import datetime
class Agenda:
    def __init__(self, db):
        self.db = db

    def carregar_agendamentos(self):
        cursor = self.db.conn.execute('''
            SELECT Agendamentos.data, Agendamentos.horario, Servicos.nome, Agendamentos.cliente
            FROM Agendamentos
            JOIN Servicos ON Agendamentos.servico_id = Servicos.id
        ''')
        agendamentos = [{"data": row[0], "horario": row[1], "servico": {"nome": row[2]}, "cliente": row[3]} for row in cursor.fetchall()]
        return agendamentos

    def agendar_servico(self, servico, data, horario, cliente):
        data_atual = datetime.now().date()
        data_agendamento = datetime.strptime(data, "%d/%m/%Y").date()
        if data_agendamento <= data_atual:
            return "Não é possível agendar para uma data passada ou presente."

        try:
            datetime.strptime(horario, "%H:%M")
        except ValueError:
            return "Formato de horário inválido. Use HH:MM."

        cursor = self.db.conn.execute('''
            SELECT COUNT(*) FROM Agendamentos
            WHERE data = ? AND horario = ?
        ''', (data, horario))
        if cursor.fetchone()[0] > 0:
            return "Este horário já está ocupado. Por favor, selecione outro horário."

        with self.db.conn:
            self.db.conn.execute('''
                INSERT INTO Agendamentos (data, horario, servico_id, cliente)
                VALUES (?, ?, ?, ?)
            ''', (data, horario, servico.id, cliente))
        return "Serviço agendado com sucesso."
