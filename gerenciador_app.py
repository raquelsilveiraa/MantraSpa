from tkinter import *
import json
from tkinter import messagebox
from Servico import Servico
from Funcionario import Funcionario
from Vendas import Vendas
from Agenda import Agenda
from gerenciadorservicos import GerenciadorServicos
from gerenciadorfuncionario import GerenciadorFuncionarios
from gerenciadorvendas import GerenciadorVendas
from gerenciadoragendamentos import GerenciadorAgendamentos
from gerenciadorpromocoes import GerenciadorPromocoes
from gerenciadoravaliacoes import GerenciadorAvaliacoes

class GerenciadorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de Gerenciamento")
        self.master.geometry("800x600")
        self.master.configure(bg="#f0f0f0")

        self.servicos = []
        self.funcionarios = []
        self.agenda = Agenda()
        self.vendas = Vendas()
        self.avaliacoes = []
        self.promocoes = []

        self.carregar_dados()
        self.menu_login()

    def carregar_dados(self):
        try:
            with open("dados.json", "r") as file:
                dados = json.load(file)
                self.servicos = [Servico(**servico) for servico in dados["servicos"]]
                self.funcionarios = [Funcionario(**funcionario) for funcionario in dados["funcionarios"]]
                self.vendas.fluxo_de_caixa = dados.get("vendas", [])
                self.avaliacoes = dados.get("avaliacoes", [])
                self.promocoes = dados.get("promocoes", [])
        except FileNotFoundError:
            pass

    def salvar_dados(self):
        dados = {
            "servicos": [vars(servico) for servico in self.servicos],
            "funcionarios": [vars(funcionario) for funcionario in self.funcionarios],
            "vendas": self.vendas.fluxo_de_caixa,
            "avaliacoes": self.avaliacoes,
            "promocoes": self.promocoes,
            "agendamentos": []
        }
        for data, horarios in self.agenda.horarios_disponiveis.items():
            for horario, servico, cliente in horarios:
                agendamento = {
                    "data": data,
                    "horario": horario,
                    "servico": vars(servico),
                    "cliente": cliente
                }
                dados["agendamentos"].append(agendamento)
        with open("dados.json", "w") as file:
            json.dump(dados, file, indent=4)

    def menu_login(self):
        self.limpar_tela()

        lbl_titulo = Label(self.master, text="Mantra SPA - Login", font=("Albert Sans", 36, "bold"), bg="#FFC0CB", fg="black", padx=20, pady=10)
        lbl_titulo.pack(fill=X)

        frame_login = Frame(self.master, bg="#f0f0f0", padx=20, pady=20)
        frame_login.pack(pady=20)

        lbl_usuario = Label(frame_login, text="Usuário:", font=("Albert Sans", 18), bg="#f0f0f0")
        lbl_usuario.grid(row=0, column=0, pady=10, sticky=E)

        self.entry_usuario = Entry(frame_login, font=("Albert Sans", 18))
        self.entry_usuario.grid(row=0, column=1, pady=10, padx=10)

        lbl_senha = Label(frame_login, text="Senha:", font=("Albert Sans", 18), bg="#f0f0f0")
        lbl_senha.grid(row=1, column=0, pady=10, sticky=E)

        self.entry_senha = Entry(frame_login, font=("Albert Sans", 18), show="*")
        self.entry_senha.grid(row=1, column=1, pady=10, padx=10)

        btn_login = Button(frame_login, text="Login", font=("Albert Sans", 18), command=self.validar_login, bg="#FFC0CB", fg="black", padx=20, pady=10, bd=0, relief=FLAT)
        btn_login.grid(row=2, column=0, columnspan=2, pady=20)

    def validar_login(self):
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()
        if usuario == "admin" and senha == "123456":
            self.menu_principal()
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos.")

    def menu_principal(self):
        self.limpar_tela()

        lbl_titulo = Label(self.master, text="Mantra SPA", font=("Albert Sans", 36, "bold"), bg="#FFC0CB", fg="black", padx=20, pady=10)
        lbl_titulo.pack(fill=X)

        frame_botoes = Frame(self.master, bg="#f0f0f0", padx=20, pady=20)
        frame_botoes.pack(pady=20)

        btn_servicos = Button(frame_botoes, text="Gerenciar Serviços", font=("Albert Sans", 18), command=self.menu_servicos, bg="#FFC0CB", fg="black", padx=20, pady=10, bd=0, relief=FLAT)
        btn_servicos.grid(row=0, column=0, padx=10)

        btn_agendamentos = Button(frame_botoes, text="Gerenciar Agendamentos", font=("Albert Sans", 18), command=self.menu_agendamentos, bg="#FFC0CB", fg="black", padx=20, pady=10, bd=0, relief=FLAT)
        btn_agendamentos.grid(row=0, column=1, padx=10)

        btn_funcionarios = Button(frame_botoes, text="Gerenciar Funcionários", font=("Albert Sans", 18), command=self.menu_funcionarios, bg="#FFC0CB", fg="black", padx=20, pady=10, bd=0, relief=FLAT)
        btn_funcionarios.grid(row=1, column=0, padx=10, pady=10)

        btn_vendas = Button(frame_botoes, text="Gerenciar Vendas", font=("Albert Sans", 18), command=self.menu_vendas, bg="#FFC0CB", fg="black", padx=20, pady=10, bd=0, relief=FLAT)
        btn_vendas.grid(row=1, column=1, padx=10, pady=10)

        btn_ver_horarios = Button(frame_botoes, text="Ver Horários Agendados", font=("Albert Sans", 18), command=self.menu_ver_horarios, bg="#FFC0CB", fg="black", padx=20, pady=10, bd=0, relief=FLAT)
        btn_ver_horarios.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        btn_promocoes = Button(frame_botoes, text="Gerenciar Promoções", font=("Albert Sans", 18), command=self.menu_promocoes, bg="#FFC0CB", fg="black", padx=20, pady=10, bd=0, relief=FLAT)
        btn_promocoes.grid(row=3, column=0, padx=10, pady=10)

        btn_avaliacoes = Button(frame_botoes, text="Ver Avaliações", font=("Albert Sans", 18), command=self.menu_avaliacoes, bg="#FFC0CB", fg="black", padx=20, pady=10, bd=0, relief=FLAT)
        btn_avaliacoes.grid(row=3, column=1, padx=10, pady=10)

        self.master.protocol("WM_DELETE_WINDOW", self.fechar_aplicacao)

    def fechar_aplicacao(self):
        self.salvar_dados()
        self.master.destroy()

    def limpar_tela(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def menu_servicos(self):
        GerenciadorServicos(self.master, self.servicos, self.salvar_dados, self.menu_principal).menu_servicos()

    def menu_funcionarios(self):
        GerenciadorFuncionarios(self.master, self.funcionarios, self.salvar_dados, self.menu_principal).menu_funcionarios()

    def menu_vendas(self):
        GerenciadorVendas(self.master, self.servicos, self.vendas, self.salvar_dados, self.menu_principal).menu_vendas()

    def menu_agendamentos(self):
        GerenciadorAgendamentos(self.master, self.agenda, self.servicos, self.salvar_dados, self.menu_principal).menu_agendamentos()

    def menu_promocoes(self):
        GerenciadorPromocoes(self.master, self.promocoes, self.salvar_dados, self.menu_principal).menu_promocoes()

    def menu_avaliacoes(self):
        GerenciadorAvaliacoes(self.master, self.avaliacoes, self.salvar_dados, self.menu_principal).menu_avaliacoes()

    def menu_ver_horarios(self):
        GerenciadorAgendamentos(self.master, self.agenda, self.servicos, self.salvar_dados, self.menu_principal).ver_horarios_agendados()
