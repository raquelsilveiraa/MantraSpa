import unittest
from tkinter import Tk
from eu import *

class TestGerenciadorApp(unittest.TestCase):
    def setUp(self):
        self.app = GerenciadorApp(Tk())

    def test_adicionar_servico_adiciona_um_servico(self):
        self.app.adicionar_servico()
        self.assertNotEqual(len(self.app.servicos), 0)

    def test_agendar_servico_agenda_um_servico_com_sucesso(self):
        servico = Servico("Corte de Cabelo", "Corte de cabelo masculino", "Corte, lavagem, secagem")
        data = "01/05/2024"
        horario = "10:00"
        resultado = self.app.agenda.agendar_servico(servico, data, horario)
        self.assertEqual(resultado, "Serviço agendado com sucesso.")

    def test_listar_agendamentos_retorna_lista_de_agendamentos(self):
        self.app.listar_agendamentos()

    def test_adicionar_funcionario_adiciona_um_funcionario(self):
        self.app.adicionar_funcionario()
        self.assertNotEqual(len(self.app.funcionarios), 0)

    def test_remover_funcionario_remove_um_funcionario(self):
        self.app.remover_funcionario()

    def test_registrar_venda_registra_uma_venda_com_sucesso(self):
        servico = Servico("Manicure", "Manicure e pedicure", "Corte, pintura, tratamento")
        resultado = self.app.vendas.registrar_venda(50, servico)
        self.assertEqual(resultado, "Venda registrada com sucesso.")

    def test_exibir_fluxo_exibe_o_fluxo_de_caixa(self):
        self.app.exibir_fluxo()

    def test_listar_servicos_retorna_lista_de_servicos(self):
        self.app.listar_servicos()

    def test_listar_funcionarios_retorna_lista_de_funcionarios(self):
        self.app.listar_funcionarios()

    def test_menu_servicos_abre_menu_de_gerenciamento_de_servicos(self):
        self.app.menu_servicos()

    def test_menu_agendamentos_abre_menu_de_gerenciamento_de_agendamentos(self):
        self.app.menu_agendamentos()

    def test_menu_funcionarios_abre_menu_de_gerenciamento_de_funcionarios(self):
        self.app.menu_funcionarios()

    def test_menu_vendas_abre_menu_de_gerenciamento_de_vendas(self):
        self.app.menu_vendas()

    def test_fechar_aplicacao_fecha_o_aplicativo_com_sucesso(self):
        self.app.fechar_aplicacao()

    def test_salvar_dados_salva_os_dados_com_sucesso(self):
        self.app.salvar_dados()

    def test_carregar_dados_carrega_os_dados_com_sucesso(self):
        self.app.carregar_dados()

    def test_limpar_tela_limpa_a_tela_com_sucesso(self):
        self.app.limpar_tela()

    def test_fazer_agendamento_abre_janela_para_fazer_agendamento(self):
        self.app.fazer_agendamento()

    def test_registrar_venda_abre_janela_para_registrar_venda(self):
        self.app.registrar_venda()

    def tearDown(self):
        self.app.master.destroy()

if __name__ == '__main__':
    # Executa os testes
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGerenciadorApp)
    result = unittest.TextTestRunner().run(suite)

    # Verifica se houve algum erro
    if result.errors or result.failures:
        print("Houve erro nos testes.")
    else:
        print("Todos os testes foram executados com sucesso.")
