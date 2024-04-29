from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime
import json

class Servico:
    def __init__(self, nome, descricao, beneficios):
        self.nome = nome
        self.descricao = descricao
        self.beneficios = beneficios

    def __str__(self):
        return f"Nome: {self.nome}\nDescrição: {self.descricao}\nBenefícios: {self.beneficios}"

class Funcionario:
    def __init__(self, nome, cargo, disponivel=True):
        self.nome = nome
        self.cargo = cargo
        self.disponivel = disponivel

    def __str__(self):
        return f"Nome: {self.nome}\nCargo: {self.cargo}\nDisponível: {'Sim' if self.disponivel else 'Não'}"

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

class Vendas:
    def __init__(self):
        self.fluxo_de_caixa = []

    def registrar_venda(self, valor, servico):
        self.fluxo_de_caixa.append((valor, servico))
        return "Venda registrada com sucesso."

    def exibir_fluxo_de_caixa(self):
        registros = []
        if self.fluxo_de_caixa:
            for valor, servico in self.fluxo_de_caixa:
                registros.append(f"Serviço: {servico.nome}, Valor: R${valor}")
        return registros

class GerenciadorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de Gerenciamento")
        self.master.geometry("800x600")

        self.servicos = []
        self.funcionarios = []
        self.agenda = Agenda()
        self.vendas = Vendas()

        self.carregar_dados()
        self.menu_principal()

    def carregar_dados(self):
        try:
            with open("dados.json", "r") as file:
                dados = json.load(file)
                self.servicos = [Servico(**servico) for servico in dados["servicos"]]
                self.funcionarios = [Funcionario(**funcionario) for funcionario in dados["funcionarios"]]
        except FileNotFoundError:
            pass

    def salvar_dados(self):
        dados = {
            "servicos": [vars(servico) for servico in self.servicos],
            "funcionarios": [vars(funcionario) for funcionario in self.funcionarios]
        }
        with open("dados.json", "w") as file:
            json.dump(dados, file, indent=4)

    def menu_principal(self):
        self.limpar_tela()

        lbl_titulo = Label(self.master, text="Menu Principal", font=("Helvetica", 24, "bold"), bg="#1E90FF", fg="white", padx=20, pady=10)
        lbl_titulo.pack(fill=X)

        frame_botoes = Frame(self.master, bg="#f0f0f0", padx=20, pady=20)
        frame_botoes.pack(pady=20)

        btn_servicos = Button(frame_botoes, text="Gerenciar Serviços", font=("Helvetica", 14), command=self.menu_servicos)
        btn_servicos.grid(row=0, column=0, padx=10)

        btn_agendamentos = Button(frame_botoes, text="Gerenciar Agendamentos", font=("Helvetica", 14), command=self.menu_agendamentos)
        btn_agendamentos.grid(row=0, column=1, padx=10)

        btn_funcionarios = Button(frame_botoes, text="Gerenciar Funcionários", font=("Helvetica", 14), command=self.menu_funcionarios)
        btn_funcionarios.grid(row=1, column=0, padx=10, pady=10)

        btn_vendas = Button(frame_botoes, text="Gerenciar Vendas", font=("Helvetica", 14), command=self.menu_vendas)
        btn_vendas.grid(row=1, column=1, padx=10, pady=10)

        self.master.protocol("WM_DELETE_WINDOW", self.fechar_aplicacao)

    def fechar_aplicacao(self):
        self.salvar_dados()
        self.master.destroy()

    def limpar_tela(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def menu_servicos(self):
        self.limpar_tela()

        lbl_titulo = Label(self.master, text="Gerenciamento de Serviços", font=("Helvetica", 24, "bold"), bg="#1E90FF", fg="white", padx=20, pady=10)
        lbl_titulo.pack(fill=X)

        frame_botoes = Frame(self.master, bg="#f0f0f0", padx=20, pady=20)
        frame_botoes.pack(pady=20)

        btn_adicionar_servico = Button(frame_botoes, text="Adicionar Serviço", font=("Helvetica", 14), command=self.adicionar_servico)
        btn_adicionar_servico.grid(row=0, column=0, padx=10)

        btn_listar_servicos = Button(frame_botoes, text="Listar Serviços", font=("Helvetica", 14), command=self.listar_servicos)
        btn_listar_servicos.grid(row=0, column=1, padx=10)

        btn_voltar = Button(frame_botoes, text="Voltar", font=("Helvetica", 14), command=self.menu_principal)
        btn_voltar.grid(row=1, column=0, columnspan=2, pady=10)

    def adicionar_servico(self):
        def adicionar():
            nome = entry_nome.get()
            descricao = entry_descricao.get("1.0", "end-1c")
            beneficios = entry_beneficios.get("1.0", "end-1c")
            servico = Servico(nome, descricao, beneficios)
            self.servicos.append(servico)
            messagebox.showinfo("Sucesso", "Serviço adicionado com sucesso.")
            window.destroy()

        window = Toplevel(self.master)
        window.title("Adicionar Serviço")
        window.geometry("400x400")

        frame = Frame(window, bg="#f0f0f0")
        frame.pack(pady=20)

        lbl_nome = Label(frame, text="Nome:", font=("Helvetica", 14), bg="#f0f0f0")
        lbl_nome.grid(row=0, column=0, padx=10, pady=5)
        entry_nome = Entry(frame, font=("Helvetica", 14))
        entry_nome.grid(row=0, column=1, padx=10, pady=5)

        lbl_descricao = Label(frame, text="Descrição:", font=("Helvetica", 14), bg="#f0f0f0")
        lbl_descricao.grid(row=1, column=0, padx=10, pady=5)
        entry_descricao = Text(frame, font=("Helvetica", 14), height=5, width=30)
        entry_descricao.grid(row=1, column=1, padx=10, pady=5)

        lbl_beneficios = Label(frame, text="Benefícios:", font=("Helvetica", 14), bg="#f0f0f0")
        lbl_beneficios.grid(row=2, column=0, padx=10, pady=5)
        entry_beneficios = Text(frame, font=("Helvetica", 14), height=5, width=30)
        entry_beneficios.grid(row=2, column=1, padx=10, pady=5)

        btn_adicionar = Button(window, text="Adicionar", font=("Helvetica", 14), command=adicionar)
        btn_adicionar.pack(pady=10)

    def listar_servicos(self):
        self.limpar_tela()

        lbl_titulo = Label(self.master, text="Lista de Serviços", font=("Helvetica", 24, "bold"), bg="#1E90FF", fg="white", padx=20, pady=10)
        lbl_titulo.pack(fill=X)

        frame_lista = Frame(self.master, bg="#f0f0f0", padx=20, pady=20)
        frame_lista.pack(pady=20)

        if self.servicos:
            for i, servico in enumerate(self.servicos):
                lbl_servico = Label(frame_lista, text=servico, font=("Helvetica", 14), bg="#f0f0f0", wraplength=600, justify="left")
                lbl_servico.grid(row=i, column=0, padx=10, pady=5, sticky="w")
        else:
            lbl_aviso = Label(frame_lista, text="Não há serviços cadastrados.", font=("Helvetica", 14), bg="#f0f0f0")
            lbl_aviso.grid(row=0, column=0, padx=10, pady=5)

        btn_voltar = Button(self.master, text="Voltar", font=("Helvetica", 14), command=self.menu_servicos)
        btn_voltar.pack()

    def menu_agendamentos(self):
        self.limpar_tela()

        lbl_titulo = Label(self.master, text="Gerenciamento de Agendamentos", font=("Helvetica", 24, "bold"), bg="#1E90FF", fg="white", padx=20, pady=10)
        lbl_titulo.pack(fill=X)

        frame_botoes = Frame(self.master, bg="#f0f0f0", padx=20, pady=20)
        frame_botoes.pack(pady=20)

        btn_fazer_agendamento = Button(frame_botoes, text="Fazer Agendamento", font=("Helvetica", 14), command=self.fazer_agendamento)
        btn_fazer_agendamento.grid(row=0, column=0, padx=10)

        btn_listar_agendamentos = Button(frame_botoes, text="Listar Agendamentos", font=("Helvetica", 14), command=self.listar_agendamentos)
        btn_listar_agendamentos.grid(row=0, column=1, padx=10)

        btn_voltar = Button(frame_botoes, text="Voltar", font=("Helvetica", 14), command=self.menu_principal)
        btn_voltar.grid(row=1, column=0, columnspan=2, pady=10)

    def fazer_agendamento(self):
        def agendar():
            data = entry_data.get()
            horario = entry_horario.get()
            servico = self.servicos[combo_servicos.current()]
            if data and horario:
                resultado = self.agenda.agendar_servico(servico, data, horario)
                messagebox.showinfo("Sucesso", resultado)
                window.destroy()
            else:
                messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")

        window = Toplevel(self.master)
        window.title("Fazer Agendamento")
        window.geometry("400x300")

        frame = Frame(window, bg="#f0f0f0")
        frame.pack(pady=20)

        lbl_servico = Label(frame, text="Serviço:", font=("Helvetica", 14), bg="#f0f0f0")
        lbl_servico.grid(row=0, column=0, padx=10, pady=5)
        combo_servicos = ttk.Combobox(frame, values=[servico.nome for servico in self.servicos], font=("Helvetica", 14))
        combo_servicos.grid(row=0, column=1, padx=10, pady=5)

        lbl_data = Label(frame, text="Data (DD/MM/AAAA):", font=("Helvetica", 14), bg="#f0f0f0")
        lbl_data.grid(row=1, column=0, padx=10, pady=5)
        entry_data = Entry(frame, font=("Helvetica", 14))
        entry_data.grid(row=1, column=1, padx=10, pady=5)

        lbl_horario = Label(frame, text="Horário:", font=("Helvetica", 14), bg="#f0f0f0")
        lbl_horario.grid(row=2, column=0, padx=10, pady=5)
        entry_horario = Entry(frame, font=("Helvetica", 14))
        entry_horario.grid(row=2, column=1, padx=10, pady=5)

        btn_agendar = Button(window, text="Agendar", font=("Helvetica", 14), command=agendar)
        btn_agendar.pack(pady=10)

    def listar_agendamentos(self):
        self.limpar_tela()

        lbl_titulo = Label(self.master, text="Lista de Agendamentos", font=("Helvetica", 24, "bold"), bg="#1E90FF", fg="white", padx=20, pady=10)
        lbl_titulo.pack(fill=X)

        frame_lista = Frame(self.master, bg="#f0f0f0", padx=20, pady=20)
        frame_lista.pack(pady=20)

        agendamentos = self.agenda.listar_horarios_disponiveis()

        if agendamentos:
            for i, agendamento in enumerate(agendamentos):
                lbl_agendamento = Label(frame_lista, text=agendamento, font=("Helvetica", 14), bg="#f0f0f0", wraplength=600, justify="left")
                lbl_agendamento.grid(row=i, column=0, padx=10, pady=5, sticky="w")
        else:
            lbl_aviso = Label(frame_lista, text="Não há agendamentos.", font=("Helvetica", 14), bg="#f0f0f0")
            lbl_aviso.grid(row=0, column=0, padx=10, pady=5)

        btn_voltar = Button(self.master, text="Voltar", font=("Helvetica", 14), command=self.menu_agendamentos)
        btn_voltar.pack()

    def menu_funcionarios(self):
        self.limpar_tela()

        lbl_titulo = Label(self.master, text="Gerenciamento de Funcionários", font=("Helvetica", 24, "bold"), bg="#1E90FF", fg="white", padx=20, pady=10)
        lbl_titulo.pack(fill=X)

        frame_botoes = Frame(self.master, bg="#f0f0f0", padx=20, pady=20)
        frame_botoes.pack(pady=20)

        btn_adicionar_funcionario = Button(frame_botoes, text="Adicionar Funcionário", font=("Helvetica", 14), command=self.adicionar_funcionario)
        btn_adicionar_funcionario.grid(row=0, column=0, padx=10)

        btn_listar_funcionarios = Button(frame_botoes, text="Listar Funcionários", font=("Helvetica", 14), command=self.listar_funcionarios)
        btn_listar_funcionarios.grid(row=0, column=1, padx=10)

        btn_remover_funcionario = Button(frame_botoes, text="Remover Funcionário", font=("Helvetica", 14), command=self.remover_funcionario)
        btn_remover_funcionario.grid(row=1, column=0, columnspan=2, pady=10)

        btn_voltar = Button(frame_botoes, text="Voltar", font=("Helvetica", 14), command=self.menu_principal)
        btn_voltar.grid(row=2, column=0, columnspan=2, pady=10)

    def adicionar_funcionario(self):
        def adicionar():
            nome = entry_nome.get()
            cargo = entry_cargo.get()
            if nome and cargo:
                funcionario = Funcionario(nome, cargo)
                self.funcionarios.append(funcionario)
                messagebox.showinfo("Sucesso", "Funcionário adicionado com sucesso.")
                window.destroy()
            else:
                messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")

        window = Toplevel(self.master)
        window.title("Adicionar Funcionário")
        window.geometry("400x300")

        frame = Frame(window, bg="#f0f0f0")
        frame.pack(pady=20)

        lbl_nome = Label(frame, text="Nome:", font=("Helvetica", 14), bg="#f0f0f0")
        lbl_nome.grid(row=0, column=0, padx=10, pady=5)
        entry_nome = Entry(frame, font=("Helvetica", 14))
        entry_nome.grid(row=0, column=1, padx=10, pady=5)

        lbl_cargo = Label(frame, text="Cargo:", font=("Helvetica", 14), bg="#f0f0f0")
        lbl_cargo.grid(row=1, column=0, padx=10, pady=5)
        entry_cargo = Entry(frame, font=("Helvetica", 14))
        entry_cargo.grid(row=1, column=1, padx=10, pady=5)

        btn_adicionar = Button(window, text="Adicionar", font=("Helvetica", 14), command=adicionar)
        btn_adicionar.pack(pady=10)

    def listar_funcionarios(self):
        self.limpar_tela()

        lbl_titulo = Label(self.master, text="Lista de Funcionários", font=("Helvetica", 24, "bold"), bg="#1E90FF", fg="white", padx=20, pady=10)
        lbl_titulo.pack(fill=X)

        frame_lista = Frame(self.master, bg="#f0f0f0", padx=20, pady=20)
        frame_lista.pack(pady=20)

        if self.funcionarios:
            for i, funcionario in enumerate(self.funcionarios):
                lbl_funcionario = Label(frame_lista, text=funcionario, font=("Helvetica", 14), bg="#f0f0f0", wraplength=600, justify="left")
                lbl_funcionario.grid(row=i, column=0, padx=10, pady=5, sticky="w")
        else:
            lbl_aviso = Label(frame_lista, text="Não há funcionários cadastrados.", font=("Helvetica", 14), bg="#f0f0f0")
            lbl_aviso.grid(row=0, column=0, padx=10, pady=5)

        btn_voltar = Button(self.master, text="Voltar", font=("Helvetica", 14), command=self.menu_funcionarios)
        btn_voltar.pack()

    def remover_funcionario(self):
        def remover():
            index = combo_funcionarios.current()
            if index >= 0:
                del self.funcionarios[index]
                messagebox.showinfo("Sucesso", "Funcionário removido com sucesso.")
                window.destroy()
            else:
                messagebox.showwarning("Erro", "Por favor, selecione um funcionário.")

        window = Toplevel(self.master)
        window.title("Remover Funcionário")
        window.geometry("300x150")

        frame = Frame(window, bg="#f0f0f0")
        frame.pack(pady=20)

        lbl_funcionario = Label(frame, text="Selecione o funcionário:", font=("Helvetica", 14), bg="#f0f0f0")
        lbl_funcionario.grid(row=0, column=0, padx=10, pady=5)
        combo_funcionarios = ttk.Combobox(frame, values=[funcionario.nome for funcionario in self.funcionarios], font=("Helvetica", 14))
        combo_funcionarios.grid(row=0, column=1, padx=10, pady=5)

        btn_remover = Button(window, text="Remover", font=("Helvetica", 14), command=remover)
        btn_remover.pack(pady=10)

    def menu_vendas(self):
        self.limpar_tela()

        lbl_titulo = Label(self.master, text="Gerenciamento de Vendas", font=("Helvetica", 24, "bold"), bg="#1E90FF", fg="white", padx=20, pady=10)
        lbl_titulo.pack(fill=X)

        frame_botoes = Frame(self.master, bg="#f0f0f0", padx=20, pady=20)
        frame_botoes.pack(pady=20)

        btn_registrar_venda = Button(frame_botoes, text="Registrar Venda", font=("Helvetica", 14), command=self.registrar_venda)
        btn_registrar_venda.grid(row=0, column=0, padx=10)

        btn_exibir_fluxo = Button(frame_botoes, text="Exibir Fluxo de Caixa", font=("Helvetica", 14), command=self.exibir_fluxo)
        btn_exibir_fluxo.grid(row=0, column=1, padx=10)

        btn_voltar = Button(frame_botoes, text="Voltar", font=("Helvetica", 14), command=self.menu_principal)
        btn_voltar.grid(row=1, column=0, columnspan=2, pady=10)

    def registrar_venda(self):
        def registrar():
            valor = entry_valor.get()
            servico = self.servicos[combo_servicos.current()]
            if valor:
                resultado = self.vendas.registrar_venda(valor, servico)
                messagebox.showinfo("Sucesso", resultado)
                window.destroy()
            else:
                messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")

        window = Toplevel(self.master)
        window.title("Registrar Venda")
        window.geometry("400x300")

        frame = Frame(window, bg="#f0f0f0")
        frame.pack(pady=20)

        lbl_servico = Label(frame, text="Serviço:", font=("Helvetica", 14), bg="#f0f0f0")
        lbl_servico.grid(row=0, column=0, padx=10, pady=5)
        combo_servicos = ttk.Combobox(frame, values=[servico.nome for servico in self.servicos], font=("Helvetica", 14))
        combo_servicos.grid(row=0, column=1, padx=10, pady=5)

        lbl_valor = Label(frame, text="Valor (R$):", font=("Helvetica", 14), bg="#f0f0f0")
        lbl_valor.grid(row=1, column=0, padx=10, pady=5)
        entry_valor = Entry(frame, font=("Helvetica", 14))
        entry_valor.grid(row=1, column=1, padx=10, pady=5)

        btn_registrar = Button(window, text="Registrar", font=("Helvetica", 14), command=registrar)
        btn_registrar.pack(pady=10)

    def exibir_fluxo(self):
        self.limpar_tela()

        lbl_titulo = Label(self.master, text="Fluxo de Caixa", font=("Helvetica", 24, "bold"), bg="#1E90FF", fg="white", padx=20, pady=10)
        lbl_titulo.pack(fill=X)

        frame_lista = Frame(self.master, bg="#f0f0f0", padx=20, pady=20)
        frame_lista.pack(pady=20)

        fluxo = self.vendas.exibir_fluxo_de_caixa()

        if fluxo:
            for i, registro in enumerate(fluxo):
                lbl_registro = Label(frame_lista, text=registro, font=("Helvetica", 14), bg="#f0f0f0", wraplength=600, justify="left")
                lbl_registro.grid(row=i, column=0, padx=10, pady=5, sticky="w")
        else:
            lbl_aviso = Label(frame_lista, text="Não há registros de vendas.", font=("Helvetica", 14), bg="#f0f0f0")
            lbl_aviso.grid(row=0, column=0, padx=10, pady=5)

        btn_voltar = Button(self.master, text="Voltar", font=("Helvetica", 14), command=self.menu_vendas)
        btn_voltar.pack()

root = Tk()
app = GerenciadorApp(root)
root.mainloop()
