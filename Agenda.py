class Agenda:
    def __init__(self, db):
        self.db = db
        self.horarios_disponiveis = {}
        self.agendamentos = self.carregar_agendamentos()

    def carregar_agendamentos(self):
        cursor = self.db.conn.execute("SELECT id, data, horario, servico_id, cliente FROM Agendamentos")
        agendamentos = []
        for row in cursor.fetchall():
            agendamento = {
                "id": row[0],
                "data": row[1],
                "horario": row[2],
                "servico_id": row[3],
                "cliente": row[4]
            }
            agendamentos.append(agendamento)
        return agendamentos

    def agendar_servico(self, servico, data, horario, cliente):
        if data in self.horarios_disponiveis and horario in [horario_agendado for horario_agendado, _, _ in self.horarios_disponiveis[data]]:
            return "Este horário já está ocupado. Por favor, selecione outro horário."

        data_atual = datetime.now().date()
        data_agendamento = datetime.strptime(data, "%d/%m/%Y").date()
        if data_agendamento <= data_atual:
            return "Não é possível agendar para uma data passada ou presente."

        try:
            datetime.strptime(horario, "%H:%M")
        except ValueError:
            return "Formato de horário inválido. Use HH:MM."

        if data not in self.horarios_disponiveis:
            self.horarios_disponiveis[data] = []
        self.horarios_disponiveis[data].append((horario, servico, cliente))

        with self.db.conn:
            cursor = self.db.conn.execute('''
                INSERT INTO Agendamentos (data, horario, servico_id, cliente)
                VALUES (?, ?, ?, ?)
            ''', (data, horario, servico.id, cliente))
        agendamento_id = cursor.lastrowid
        novo_agendamento = {
            "id": agendamento_id,
            "data": data,
            "horario": horario,
            "servico_id": servico.id,
            "cliente": cliente
        }
        self.agendamentos.append(novo_agendamento)
        return "Serviço agendado com sucesso."

    def remover_agendamento(self, agendamento_id):
        with self.db.conn:
            self.db.conn.execute('DELETE FROM Agendamentos WHERE id = ?', (agendamento_id,))
        self.agendamentos = [agendamento for agendamento in self.agendamentos if agendamento["id"] != agendamento_id]
