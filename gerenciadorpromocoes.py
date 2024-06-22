from tkinter import *
from tkinter import messagebox

class GerenciadorPromocoes:
    def __init__(self, master, promocoes, db, voltar_callback):
        self.master = master
        self.promocoes = promocoes
        self.db = db
        self.voltar_callback = voltar_callback

    def menu_promocoes(self):
        self.limpar_tela()

        lbl_titulo = Label(self.master, text="Gerenciamento de Promoções", font=("Albert Sans", 24, "bold"), bg="#FFC0CB", fg="black", padx=20, pady=10)
        lbl_titulo.pack(fill=X)

        frame_botoes = Frame(self.master, bg="#f0f0f0", padx=20, pady=20)
        frame_botoes.pack(pady=20)

        btn_adicionar_promocao = Button(frame_botoes, text="Adicionar Promoção", font=("Albert Sans", 14), command=self.adicionar_promocao)
        btn_adicionar_promocao.grid(row=0, column=0, padx=10)

        btn_listar_promocoes = Button(frame_botoes, text="Listar Promoções", font=("Albert Sans", 14), command=self.listar_promocoes)
        btn_listar_promocoes.grid(row=0, column=1, padx=10)

        btn_remover_promocao = Button(frame_botoes, text="Remover Promoção", font=("Albert Sans", 14), command=self.remover_promocao)
        btn_remover_promocao.grid(row=1, column=0, columnspan=2, pady=10)

        btn_voltar = Button(frame_botoes, text="Voltar", font=("Albert Sans", 14), command=self.voltar_callback)
        btn_voltar.grid(row=2, column=0, columnspan=2, pady=10)

    def adicionar_promocao(self):
        def adicionar():
            descricao = entry_descricao.get("1.0", "end-1c")
            if descricao:
                with self.db.conn:
                    self.db.conn.execute('''
                        INSERT INTO Promocoes (descricao)
                        VALUES (?)
                    ''', (descricao,))
                self.promocoes.append(descricao)
                messagebox.showinfo("Sucesso", "Promoção adicionada com sucesso.")
                window.destroy()
            else:
                messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")

        window = Toplevel(self.master)
        window.title("Adicionar Promoção")
        window.geometry("400x200")
        window.configure(bg="#f0f0f0")

        lbl_descricao = Label(window, text="Descrição:", font=("Albert Sans", 14), bg="#f0f0f0")
        lbl_descricao.pack(pady=10)

        entry_descricao = Text(window, font=("Albert Sans", 12), height=5, width=30)
        entry_descricao.pack()

        btn_adicionar = Button(window, text="Adicionar", font=("Albert Sans", 14), command=adicionar)
        btn_adicionar.pack(pady=10)

    def listar_promocoes(self):
        self.limpar_tela()

        lbl_titulo = Label(self.master, text="Lista de Promoções", font=("Albert Sans", 24, "bold"), bg="#FFC0CB", fg="black", padx=20, pady=10)
        lbl_titulo.pack(fill=X)

        frame_lista = Frame(self.master, bg="#f0f0f0", padx=20, pady=20)
        frame_lista.pack(pady=20)

        if self.promocoes:
            for i, promocao in enumerate(self.promocoes):
                lbl_promocao = Label(frame_lista, text=promocao, font=("Albert Sans", 14), bg="#f0f0f0", wraplength=600, justify="left")
                lbl_promocao.grid(row=i, column=0, padx=10, pady=5, sticky="w")
        else:
            lbl_aviso = Label(frame_lista, text="Não há promoções cadastradas.", font=("Albert Sans", 14), bg="#f0f0f0")
            lbl_aviso.grid(row=0, column=0, padx=10, pady=5)

        btn_voltar = Button(self.master, text="Voltar", font=("Albert Sans", 14), command=self.voltar_callback)
        btn_voltar.pack()

    def remover_promocao(self):
        def remover():
            index = listbox_promocoes.curselection()
            if index:
                descricao = self.promocoes.pop(index[0])
                with self.db.conn:
                    self.db.conn.execute('''
                        DELETE FROM Promocoes WHERE descricao = ?
                    ''', (descricao,))
                messagebox.showinfo("Sucesso", "Promoção removida com sucesso.")
                window.destroy()
            else:
                messagebox.showwarning("Erro", "Por favor, selecione uma promoção.")

        window = Toplevel(self.master)
        window.title("Remover Promoção")
        window.geometry("400x300")
        window.configure(bg="#f0f0f0")

        lbl_selecione = Label(window, text="Selecione a promoção:", font=("Albert Sans", 14), bg="#f0f0f0")
        lbl_selecione.pack(pady=10)

        listbox_promocoes = Listbox(window, font=("Albert Sans", 12), selectmode=SINGLE)
        listbox_promocoes.pack(expand=True, fill=BOTH)

        for promocao in self.promocoes:
            listbox_promocoes.insert(END, promocao)

        btn_remover = Button(window, text="Remover", font=("Albert Sans", 14), command=remover)
        btn_remover.pack(pady=20)

    def limpar_tela(self):
        for widget in self.master.winfo_children():
            widget.destroy()
