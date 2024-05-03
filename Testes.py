import unittest
from unittest.mock import patch
from tkinter import Tk
from tkinter.messagebox import showinfo, showerror
from io import StringIO
import json
from Testes import Servico, Funcionario, Agenda, Vendas, GerenciadorApp


class TestarServico(unittest.TestCase):
    def testar_servico_str(self):
        gereciamento_servico = Servico("Massagem", "Massagem redutora", "Diminui medidas e proporciona relaxamento", "Sala 22")
        expected_output = "Nome: Massagem\nDescrição: Massagem redutora\nBenefícios: Diminuição de medida e proporciona relaxamento\nLocalização: Sala 22"
        self.assertEqual(str(gereciamento_servico), expected_output)

class TestarVendas(unittest.TestCase):
    def setUp(self):
        self.vendas = Vendas()

    def testar_registro_de_venda(self):
        registrar_servico = Servico("Massagem", "Massagem redutora", "Diminuição de medidas e proporciona relaxamento", "Sala 22")
        self.vendas.registrar_venda(100, registrar_servico)
        self.assertEqual(len(self.vendas.fluxo_de_caixa), 1)

    def testar_exibicao_fluxo_de_caixa(self):
        exibicao_servico1 = Servico("Massagem", "Massagem redutora", "Diminuição de medidas e proporciona relaxamento", "Sala 22")
        exibicao_servico2 = Servico("Peeling Facial", "Hidratação da pele e Adição de ácido ", "Renovação da pele, melhoramento do aspecto e viço da pele", "Sala 08")
        self.vendas.registrar_venda(100, exibicao_servico1)
        self.vendas.registrar_venda(150, exibicao_servico2)
        expected_output = ["Serviço: Massagem, Valor: R$100", "Serviço: Peeling Facial, Valor: R$250"]
        self.assertEqual(self.vendas.exibir_fluxo_de_caixa(), expected_output)


class Testar_funcionario(unittest.TestCase):
    def testar_funcionario_str(self):
        gereciamento_funcionario = Funcionario("Carla", "Massoterapeuta")
        expected_output = "Nome: Carla\nCargo: Massoterapeuta\nDisponível: Sim"
        self.assertEqual(str(gerenciamento_funcionario), expected_output)

    def testar_disponibilidade_funcionario_default(self):
        gerencia_funcionario = Funcionario("Amanda", "Recepcionista")
        self.assertTrue(gerencia_funcionario.disponivel)

    def test_disponibilidade_funcionario_false(self):
        disponibilidade_funcionario = Funcionario("Manuela", "Esteticista", disponivel=False)
        self.assertFalse(disponibilidade_funcionario.disponivel)

class TestarAgenda(unittest.TestCase):
    def setUp(self):
        self.agenda = Agenda()

    def testar_agendamento_de_servico(self):
        agendamento_servico = Servico("Massagem", "Massagem redutora", "Diminuição de medidas e proporciona relaxamento", "Sala 22")
        self.agenda.agendar_servico(servico, "2024-04-12", "15:00")
        self.assertEqual(len(self.agenda.horarios_disponiveis), 1)

    def testar_horarios_disponiveis(self):
        servico = Servico("Massagem", "Massagem redutora", "Diminuição de medidas e proporciona relaxamento", "Sala 22"")
        self.agenda.agendar_servico(servico, "2024-05-05", "15:00")
        self.agenda.agendar_servico(servico, "2024-05-06", "09:00")
        expected_output = ["2024-04-12 - 15:00: Massagem", "2024-05-08 - 09:00: Massagem"]
        self.assertEqual(self.agenda.horarios_disponiveis(), expected_output)







