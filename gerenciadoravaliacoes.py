from tkinter import *

class GerenciadorAvaliacoes:
    def __init__(self, master, avaliacoes, salvar_dados_callback, voltar_callback):
        self.master = master
        self.avaliacoes = avaliacoes
        self.salvar_dados_callback = salvar_dados_callback
        self.voltar_callback = voltar_callback

    def menu_avaliacoes(self):
        self.limpar_tela()

        lbl_titulo = Label(self.master, text="Avaliações dos Serviços", font=("Albert Sans", 24, "bold"), bg="#FFC0CB", fg="black", padx=20, pady=10)
        lbl_titulo.pack(fill=X)

        frame_lista = Frame(self.master, bg="#f0f0f0", padx=20, pady=20)
        frame_lista.pack(pady=20)

        if self.avaliacoes:
            for i, avaliacao in enumerate(self.avaliacoes):
                lbl_avaliacao = Label(frame_lista, text=f"{avaliacao['cliente']}: {avaliacao['avaliacao']}", font=("Albert Sans", 14), bg="#f0f0f0", wraplength=600, justify="left")
                lbl_avaliacao.grid(row=i, column=0, padx=10, pady=5, sticky="w")
        else:
            lbl_aviso = Label(frame_lista, text="Não há avaliações cadastradas.", font=("Albert Sans", 14), bg="#f0f0f0")
            lbl_aviso.grid(row=0, column=0, padx=10, pady=5)

        btn_voltar = Button(self.master, text="Voltar", font=("Albert Sans", 14), command=self.voltar_callback)
        btn_voltar.pack()

    def limpar_tela(self):
        for widget in self.master.winfo_children():
            widget.destroy()
