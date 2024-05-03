class Agenda:
    def __init__(self):
        self.horarios_disponiveis = {}

    def agendar_servico(self, servico, data, horario):
        if data not in self.horarios_disponiveis:
            self.horarios_disponiveis[data] = []
        self.horarios_disponiveis[data].append((horario, servico))
        return "Serviço agendado com sucesso."

    def listar_horarios_disponiveis(self):
        disponiveis = []
        if self.horarios_disponiveis:
            for data, horarios in self.horarios_disponiveis.items():
                for horario, servico in horarios:
                    disponiveis.append(f"{data} - {horario}: {servico.nome}")
        return disponiveis
