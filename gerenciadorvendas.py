from tkinter import *
from tkinter import messagebox
from Vendas import Vendas
from tkinter import ttk

class GerenciadorVendas:
    def __init__(self, master, servicos, vendas, db, voltar_callback):
        self.master = master
        self.servicos = servicos
        self.vendas = vendas
        self.db = db
        self.voltar_callback = voltar_callback

    def menu_vendas(self):
        self.limpar_tela()

        lbl_titulo = Label(self.master, text="Gerenciamento de Vendas", font=("Albert Sans", 24, "bold"), bg="#FFC0CB", fg="black", padx=20, pady=10)
        lbl_titulo.pack(fill=X)

        frame_botoes = Frame(self.master, bg="#f0f0f0", padx=20, pady=20)
        frame_botoes.pack(pady=20)

        btn_registrar_venda = Button(frame_botoes, text="Registrar Venda", font=("Albert Sans", 14), command=self.registrar_venda)
        btn_registrar_venda.grid(row=0, column=0, padx=10)

        btn_exibir_fluxo_de_caixa = Button(frame_botoes, text="Exibir Fluxo de Caixa", font=("Albert Sans", 14), command=self.exibir_fluxo_de_caixa)
        btn_exibir_fluxo_de_caixa.grid(row=0, column=1, padx=10)

        btn_voltar = Button(frame_botoes, text="Voltar", font=("Albert Sans", 14), command=self.voltar_callback)
        btn_voltar.grid(row=1, column=0, columnspan=2, pady=10)

    def registrar_venda(self):
        def registrar():
            valor = entry_valor.get()
            servico_selecionado = combo_servicos.current()
            if valor and servico_selecionado >= 0:
                servico = self.servicos[servico_selecionado]
                resultado = self.vendas.registrar_venda(valor, servico)
                messagebox.showinfo("Sucesso", resultado)
                window.destroy()
            else:
                messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")

        window = Toplevel(self.master)
        window.title("Registrar Venda")
        window.geometry("400x300")
        window.configure(bg="#f0f0f0")

        frame = Frame(window, bg="#f0f0f0")
        frame.pack(pady=20)

        lbl_servico = Label(frame, text="Serviço:", font=("Albert Sans", 14), bg="#f0f0f0")
        lbl_servico.grid(row=0, column=0, padx=10, pady=5)
        combo_servicos = ttk.Combobox(frame, values=[servico.nome for servico in self.servicos], font=("Albert Sans", 14))
        combo_servicos.grid(row=0, column=1, padx=10, pady=5)

        lbl_valor = Label(frame, text="Valor:", font=("Albert Sans", 14), bg="#f0f0f0")
        lbl_valor.grid(row=1, column=0, padx=10, pady=5)
        entry_valor = Entry(frame, font=("Albert Sans", 14))
        entry_valor.grid(row=1, column=1, padx=10, pady=5)

        btn_registrar = Button(window, text="Registrar", font=("Albert Sans", 14), command=registrar)
        btn_registrar.pack(pady=10)

    def exibir_fluxo_de_caixa(self):
        self.limpar_tela()

        lbl_titulo = Label(self.master, text="Fluxo de Caixa", font=("Albert Sans", 24, "bold"), bg="#FFC0CB", fg="black", padx=20, pady=10)
        lbl_titulo.pack(fill=X)

        frame_lista = Frame(self.master, bg="#f0f0f0", padx=20, pady=20)
        frame_lista.pack(pady=20)

        registros = self.vendas.exibir_fluxo_de_caixa()

        if registros:
            for i, registro in enumerate(registros):
                frame_registro = Frame(frame_lista, bg="#f0f0f0")
                frame_registro.pack(fill=X, pady=5)

                lbl_registro = Label(frame_registro, text=registro['texto'], font=("Albert Sans", 14), bg="#f0f0f0", wraplength=600, justify="left")
                lbl_registro.pack(side=LEFT, padx=10)

                btn_remover = Button(frame_registro, text="Remover", font=("Albert Sans", 12), command=lambda reg_id=registro['id']: self.remover_venda(reg_id))
                btn_remover.pack(side=RIGHT, padx=10)
        else:
            lbl_aviso = Label(frame_lista, text="Não há registros de vendas.", font=("Albert Sans", 14), bg="#f0f0f0")
            lbl_aviso.grid(row=0, column=0, padx=10, pady=5)

        btn_voltar = Button(self.master, text="Voltar", font=("Albert Sans", 14), command=self.voltar_callback)
        btn_voltar.pack()

    def remover_venda(self, venda_id):
        self.vendas.remover_venda(venda_id)
        messagebox.showinfo("Sucesso", "Venda removida com sucesso.")
        self.exibir_fluxo_de_caixa()

    def limpar_tela(self):
        for widget in self.master.winfo_children():
            widget.destroy()
