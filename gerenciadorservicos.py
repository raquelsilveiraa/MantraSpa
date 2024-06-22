from tkinter import *
from tkinter import messagebox
from Servico import Servico

class GerenciadorServicos:
    def __init__(self, master, servicos, db, voltar_callback):
        self.master = master
        self.servicos = servicos
        self.db = db
        self.voltar_callback = voltar_callback

    def menu_servicos(self):
        self.limpar_tela()

        lbl_titulo = Label(self.master, text="Gerenciamento de Serviços", font=("Albert Sans", 36, "bold"), bg="#FFC0CB", fg="black", padx=20, pady=10)
        lbl_titulo.pack(fill=X)

        frame_botoes = Frame(self.master, bg="#f0f0f0", padx=20, pady=20)
        frame_botoes.pack(pady=20)

        btn_adicionar_servico = Button(frame_botoes, text="Adicionar Serviço", font=("Albert Sans", 14), command=self.adicionar_servico)
        btn_adicionar_servico.grid(row=0, column=0, padx=10)

        btn_listar_servicos = Button(frame_botoes, text="Listar Serviços", font=("Albert Sans", 14), command=self.listar_servicos)
        btn_listar_servicos.grid(row=0, column=1, padx=10)

        btn_remover_servico = Button(frame_botoes, text="Remover Serviço", font=("Albert Sans", 14), command=self.remover_servico)
        btn_remover_servico.grid(row=1, column=0, columnspan=2, pady=10)

        btn_voltar = Button(frame_botoes, text="Voltar", font=("Albert Sans", 14), command=self.voltar_callback)
        btn_voltar.grid(row=2, column=0, columnspan=2, pady=10)

    def adicionar_servico(self):
        def adicionar():
            nome = entry_nome.get()
            descricao = entry_descricao.get("1.0", "end-1c")
            beneficios = entry_beneficios.get("1.0", "end-1c")
            local = entry_localizacao.get("1.0", "end-1c")

            if not nome or not descricao or not beneficios:
                messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
                return

            servico = Servico(nome, descricao, beneficios, local)
            servico.salvar(self.db)
            self.servicos.append(servico)
            messagebox.showinfo("Sucesso", "Serviço adicionado com sucesso.")
            window_add_servico.destroy()

        window_add_servico = Toplevel(self.master)
        window_add_servico.title("Adicionar Serviço")
        window_add_servico.geometry("400x400")
        window_add_servico.configure(bg="#f0f0f0")

        lbl_nome = Label(window_add_servico, text="Nome:", font=("Albert Sans", 14), bg="#f0f0f0")
        lbl_nome.pack(pady=10)

        entry_nome = Entry(window_add_servico, font=("Albert Sans", 12))
        entry_nome.pack()

        lbl_descricao = Label(window_add_servico, text="Descrição:", font=("Albert Sans", 14), bg="#f0f0f0")
        lbl_descricao.pack(pady=10)

        entry_descricao = Text(window_add_servico, font=("Albert Sans", 12), height=5, width=30)
        entry_descricao.pack()

        lbl_beneficios = Label(window_add_servico, text="Benefícios:", font=("Albert Sans", 14), bg="#f0f0f0")
        lbl_beneficios.pack(pady=10)

        entry_beneficios = Text(window_add_servico, font=("Albert Sans", 12), height=5, width=30)
        entry_beneficios.pack()

        lbl_localizacao = Label(window_add_servico, text="Localização:", font=("Albert Sans", 14), bg="#f0f0f0")
        lbl_localizacao.pack(pady=10)

        entry_localizacao = Text(window_add_servico, font=("Albert Sans", 12), height=5, width=30)
        entry_localizacao.pack()

        btn_adicionar = Button(window_add_servico, text="Adicionar", font=("Albert Sans", 14), command=adicionar)
        btn_adicionar.pack(pady=20)

    def listar_servicos(self):
        self.limpar_tela()

        lbl_titulo = Label(self.master, text="Lista de Serviços", font=("Albert Sans", 24, "bold"), bg="#FFC0CB", fg="black", padx=20, pady=10)
        lbl_titulo.pack(fill=X)

        frame_servicos = Frame(self.master, bg="#f0f0f0", padx=20, pady=20)
        frame_servicos.pack()

        if self.servicos:
            for i, servico in enumerate(self.servicos):
                servico_info = Label(frame_servicos, text=servico.__str__(), font=("Albert Sans", 12), bg="#f0f0f0")
                servico_info.grid(row=i, column=0, sticky="w", pady=5)
        else:
            lbl_aviso = Label(frame_servicos, text="Não há serviços cadastrados.", font=("Albert Sans", 14), bg="#f0f0f0")
            lbl_aviso.grid(row=0, column=0, padx=10, pady=5)

        btn_voltar = Button(self.master, text="Voltar", font=("Albert Sans", 14), command=self.voltar_callback)
        btn_voltar.pack()

    def remover_servico(self):
        def remover():
            servico_selecionado = listbox_servicos.curselection()
            if not servico_selecionado:
                messagebox.showerror("Erro", "Por favor, selecione um serviço.")
                return
            indice = servico_selecionado[0]
            servico = self.servicos.pop(indice)
            servico.deletar(self.db)
            messagebox.showinfo("Sucesso", "Serviço removido com sucesso.")
            window_remover_servico.destroy()
            self.menu_servicos()

        window_remover_servico = Toplevel(self.master)
        window_remover_servico.title("Remover Serviço")
        window_remover_servico.geometry("400x300")
        window_remover_servico.configure(bg="#f0f0f0")

        lbl_selecione = Label(window_remover_servico, text="Selecione o serviço:", font=("Albert Sans", 14), bg="#f0f0f0")
        lbl_selecione.pack(pady=10)

        listbox_servicos = Listbox(window_remover_servico, font=("Albert Sans", 12), selectmode=SINGLE)
        listbox_servicos.pack(expand=True, fill=BOTH)

        for servico in self.servicos:
            listbox_servicos.insert(END, servico.nome)

        btn_remover = Button(window_remover_servico, text="Remover", font=("Albert Sans", 14), command=remover)
        btn_remover.pack(pady=20)

    def limpar_tela(self):
        for widget in self.master.winfo_children():
            widget.destroy()
