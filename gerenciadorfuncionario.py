from tkinter import *
from tkinter import messagebox
from Funcionario import Funcionario

class GerenciadorFuncionarios:
    def __init__(self, master, funcionarios, db, voltar_callback):
        self.master = master
        self.funcionarios = funcionarios
        self.db = db
        self.voltar_callback = voltar_callback

    def menu_funcionarios(self):
        self.limpar_tela()

        lbl_titulo = Label(self.master, text="Gerenciamento de Funcionários", font=("Albert Sans", 24, "bold"), bg="#FFC0CB", fg="black", padx=20, pady=10)
        lbl_titulo.pack(fill=X)

        frame_botoes = Frame(self.master, bg="#f0f0f0", padx=20, pady=20)
        frame_botoes.pack(pady=20)

        btn_adicionar_funcionario = Button(frame_botoes, text="Adicionar Funcionário", font=("Albert Sans", 14), command=self.adicionar_funcionario)
        btn_adicionar_funcionario.grid(row=0, column=0, padx=10)

        btn_listar_funcionarios = Button(frame_botoes, text="Listar Funcionários", font=("Albert Sans", 14), command=self.listar_funcionarios)
        btn_listar_funcionarios.grid(row=0, column=1, padx=10)

        btn_remover_funcionario = Button(frame_botoes, text="Remover Funcionário", font=("Albert Sans", 14), command=self.remover_funcionario)
        btn_remover_funcionario.grid(row=1, column=0, columnspan=2, pady=10)

        btn_voltar = Button(frame_botoes, text="Voltar", font=("Albert Sans", 14), command=self.voltar_callback)
        btn_voltar.grid(row=2, column=0, columnspan=2, pady=10)

    def adicionar_funcionario(self):
        def adicionar():
            nome = entry_nome.get()
            cargo = entry_cargo.get()
            if nome and cargo:
                funcionario = Funcionario(nome, cargo)
                funcionario.salvar(self.db)
                self.funcionarios.append(funcionario)
                messagebox.showinfo("Sucesso", "Funcionário adicionado com sucesso.")
                window.destroy()
            else:
                messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")

        window = Toplevel(self.master)
        window.title("Adicionar Funcionário")
        window.geometry("400x300")
        window.configure(bg="#f0f0f0")

        frame = Frame(window, bg="#f0f0f0")
        frame.pack(pady=20)

        lbl_nome = Label(frame, text="Nome:", font=("Albert Sans", 14), bg="#f0f0f0")
        lbl_nome.grid(row=0, column=0, padx=10, pady=5)
        entry_nome = Entry(frame, font=("Albert Sans", 14))
        entry_nome.grid(row=0, column=1, padx=10, pady=5)

        lbl_cargo = Label(frame, text="Cargo:", font=("Albert Sans", 14), bg="#f0f0f0")
        lbl_cargo.grid(row=1, column=0, padx=10, pady=5)
        entry_cargo = Entry(frame, font=("Albert Sans", 14))
        entry_cargo.grid(row=1, column=1, padx=10, pady=5)

        btn_adicionar = Button(window, text="Adicionar", font=("Albert Sans", 14), command=adicionar)
        btn_adicionar.pack(pady=10)

    def listar_funcionarios(self):
        self.limpar_tela()

        lbl_titulo = Label(self.master, text="Lista de Funcionários", font=("Albert Sans", 24, "bold"), bg="#FFC0CB", fg="black", padx=20, pady=10)
        lbl_titulo.pack(fill=X)

        frame_lista = Frame(self.master, bg="#f0f0f0", padx=20, pady=20)
        frame_lista.pack(pady=20)

        if self.funcionarios:
            for i, funcionario in enumerate(self.funcionarios):
                lbl_funcionario = Label(frame_lista, text=funcionario, font=("Albert Sans", 14), bg="#f0f0f0", wraplength=600, justify="left")
                lbl_funcionario.grid(row=i, column=0, padx=10, pady=5, sticky="w")
        else:
            lbl_aviso = Label(frame_lista, text="Não há funcionários cadastrados.", font=("Albert Sans", 14), bg="#f0f0f0")
            lbl_aviso.grid(row=0, column=0, padx=10, pady=5)

        btn_voltar = Button(self.master, text="Voltar", font=("Albert Sans", 14), command=self.voltar_callback)
        btn_voltar.pack()

    def remover_funcionario(self):
        def remover():
            index = combo_funcionarios.current()
            if index >= 0:
                funcionario = self.funcionarios.pop(index)
                funcionario.deletar(self.db)
                messagebox.showinfo("Sucesso", "Funcionário removido com sucesso.")
                window.destroy()
            else:
                messagebox.showwarning("Erro", "Por favor, selecione um funcionário.")

        window = Toplevel(self.master)
        window.title("Remover Funcionário")
        window.geometry("300x150")
        window.configure(bg="#f0f0f0")

        frame = Frame(window, bg="#f0f0f0")
        frame.pack(pady=20)

        lbl_funcionario = Label(frame, text="Selecione o funcionário:", font=("Albert Sans", 14), bg="#f0f0f0")
        lbl_funcionario.grid(row=0, column=0, padx=10, pady=5)
        combo_funcionarios = ttk.Combobox(frame, values=[funcionario.nome for funcionario in self.funcionarios], font=("Albert Sans", 14))
        combo_funcionarios.grid(row=0, column=1, padx=10, pady=5)

        btn_remover = Button(window, text="Remover", font=("Albert Sans", 14), command=remover)
        btn_remover.pack(pady=10)

    def limpar_tela(self):
        for widget in self.master.winfo_children():
            widget.destroy()
