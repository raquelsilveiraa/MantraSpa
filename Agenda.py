from datetime import datetime
import json

class Agenda:
    def __init__(self):
        self.horarios_disponiveis = {}
        self.agendamentos = self.carregar_agendamentos()

    def carregar_agendamentos(self):
        try:
            with open("dados.json", "r") as file:
                dados = json.load(file)
                return dados.get("agendamentos", [])
        except FileNotFoundError:
            return []

    def agendar_servico(self, servico, data, horario):
        # Verificar se o horário já está ocupado
        if data in self.horarios_disponiveis and horario in [horario_agendado for horario_agendado, _ in self.horarios_disponiveis[data]]:
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
        self.horarios_disponiveis[data].append((horario, servico))

        # Adicionar agendamento à lista de agendamentos
        novo_agendamento = {
            "data": data,
            "horario": horario,
            "servico": vars(servico)
        }
        self.agendamentos.append(novo_agendamento)

        return "Serviço agendado com sucesso."
