
from Servico import Servico
from Funcionario import Funcionario
from Agenda import Agenda
from Vendas import Vendas

servico1 = Servico("Massagem Relaxante", "Uma massagem que promove relaxamento muscular", "Reduz o estresse, alivia dores musculares", "Sala de Massagem 1")
servico2 = Servico("Tratamento Facial", "Um tratamento para a pele do rosto", "Limpa os poros, promove a renovação celular", "Sala de Estética Facial")

print("Informações sobre os serviços:")
print(servico1)
print(servico2)
print()


funcionario1 = Funcionario("Maria", "Massoterapeuta")
funcionario2 = Funcionario("João", "Esteticista")

print("Informações sobre os funcionários:")
print(funcionario1)
print(funcionario2)
print()


agenda = Agenda()

agenda.agendar_servico(servico1, "15/05/2024", "14:00")
agenda.agendar_servico(servico2, "17/05/2024", "10:30")
agenda.agendar_servico(servico1, "20/05/2024", "16:00")


print("Horários disponíveis na agenda:")
print(agenda.listar_horarios_disponiveis())
print()

vendas = Vendas()

vendas.registrar_venda(150.00, servico1)
vendas.registrar_venda(200.00, servico2)
vendas.registrar_venda(100.00, servico1)

print("Fluxo de Caixa:")
print(vendas.exibir_fluxo_de_caixa())
print()
