from datetime import datetime
class Agenda:
    def __init__(self):
        self.horarios_disponiveis = {}

    def agendar_servico(self, servico, data, horario):
        
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
        return "Serviço agendado com sucesso."
