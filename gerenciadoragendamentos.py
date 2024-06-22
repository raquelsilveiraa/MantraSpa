from tkinter import *
from tkinter import messagebox
from Agenda import Agenda

class GerenciadorAgendamentos:
    def __init__(self, master, agenda, servicos, db, voltar_callback):
        self.master = master
        self.agenda = agenda
        self.servicos = servicos
        self.db = db
        self.voltar_callback = voltar_callback
        self.data_var = StringVar()
        self.horario_var = StringVar()
        self.cliente_var = StringVar()

    def menu_agendamentos(self):
        self.limpar_tela()

        lbl_titulo = Label(self.master, text="Gerenciamento de Agendamentos", font=("Albert Sans", 36, "bold"), bg="#FFC0CB", fg="black", padx=20, pady=10)
        lbl_titulo.pack(fill=X)

        frame_botoes = Frame(self.master, bg="#f0f0f0", padx=20, pady=20)
        frame_botoes.pack(pady=20)

        btn_agendar_servico = Button(frame_botoes, text="Agendar Serviço", font=("Albert Sans", 18), command=self.agendar_servico, bg="#FFC0CB", fg="black", padx=20, pady=10, bd=0, relief=FLAT)
        btn_agendar_servico.grid(row=0, column=0, padx=10)

        btn_ver_horarios = Button(frame_botoes, text="Ver Horários Agendados", font=("Albert Sans", 18), command=self.ver_horarios_agendados, bg="#FFC0CB", fg="black", padx=20, pady=10, bd=0, relief=FLAT)
        btn_ver_horarios.grid(row=0, column=1, padx=10)

        btn_voltar = Button(frame_botoes, text="Voltar", font=("Albert Sans", 18), command=self.voltar_callback, bg="#FFC0CB", fg="black", padx=20, pady=10, bd=0, relief=FLAT)
        btn_voltar.grid(row=1, column=0, columnspan=2, pady=10)

    def agendar_servico(self):
        def agendar():
            servico_selecionado = listbox_servicos.curselection()
            if not servico_selecionado:
                messagebox.showerror("Erro", "Por favor, selecione um serviço.")
                return
            servico = self.servicos[servico_selecionado[0]]
            data = entry_data.get()
            horario = entry_horario.get()
            cliente = entry_cliente.get()

            if not data or not horario or not cliente:
                messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
                return

            mensagem = self.agenda.agendar_servico(servico, data, horario, cliente)

            if "sucesso" in mensagem:
                window_agendar.destroy()
            messagebox.showinfo("Informação", mensagem)

        window_agendar = Toplevel(self.master)
        window_agendar.title("Agendar Serviço")
        window_agendar.geometry("400x400")
        window_agendar.configure(bg="#f0f0f0")

        lbl_selecione_servico = Label(window_agendar, text="Selecione o serviço:", font=("Albert Sans", 14), bg="#f0f0f0")
        lbl_selecione_servico.pack(pady=10)

        listbox_servicos = Listbox(window_agendar, font=("Albert Sans", 12), selectmode=SINGLE)
        listbox_servicos.pack(expand=True, fill=BOTH)

        for servico in self.servicos:
            listbox_servicos.insert(END, servico.nome)

        frame_data_horario = Frame(window_agendar, bg="#f0f0f0")
        frame_data_horario.pack(pady=20)

        lbl_data = Label(frame_data_horario, text="Data:", font=("Albert Sans", 14), bg="#f0f0f0")
        lbl_data.grid(row=0, column=0, padx=10, pady=5)
        entry_data = Entry(frame_data_horario, textvariable=self.data_var, font=("Albert Sans", 12))
        entry_data.grid(row=0, column=1, padx=10, pady=5)

        lbl_horario = Label(frame_data_horario, text="Horário:", font=("Albert Sans", 14), bg="#f0f0f0")
        lbl_horario.grid(row=1, column=0, padx=10, pady=5)
        entry_horario = Entry(frame_data_horario, textvariable=self.horario_var, font=("Albert Sans", 12))
        entry_horario.grid(row=1, column=1, padx=10, pady=5)

        lbl_cliente = Label(frame_data_horario, text="Cliente:", font=("Albert Sans", 14), bg="#f0f0f0")
        lbl_cliente.grid(row=2, column=0, padx=10, pady=5)
        entry_cliente = Entry(frame_data_horario, textvariable=self.cliente_var, font=("Albert Sans", 12))
        entry_cliente.grid(row=2, column=1, padx=10, pady=5)

        btn_agendar = Button(window_agendar, text="Agendar", font=("Albert Sans", 14), command=agendar)
        btn_agendar.pack(pady=20)

    def ver_horarios_agendados(self):
        self.limpar_tela()

        lbl_titulo = Label(self.master, text="Horários Agendados", font=("Albert Sans", 36, "bold"), bg="#FFC0CB", fg="black", padx=20, pady=10)
        lbl_titulo.pack(fill=X)

        frame_lista = Frame(self.master, bg="#f0f0f0", padx=20, pady=20)
        frame_lista.pack(pady=20)

        agendamentos = self.agenda.carregar_agendamentos()

        if agendamentos:
            for i, agendamento in enumerate(agendamentos):
                frame_agendamento = Frame(frame_lista, bg="#f0f0f0")
                frame_agendamento.pack(fill=X, pady=5)

                servico_nome = next((servico.nome for servico in self.servicos if servico.id == agendamento["servico_id"]), "Desconhecido")
                lbl_agendamento = Label(frame_agendamento, text=f"{agendamento['data']} às {agendamento['horario']}: {servico_nome} - Cliente: {agendamento['cliente']}", font=("Albert Sans", 14), bg="#f0f0f0", wraplength=600, justify="left")
                lbl_agendamento.pack(side=LEFT, padx=10)

                btn_remover = Button(frame_agendamento, text="Remover", font=("Albert Sans", 12), command=lambda ag_id=agendamento['id']: self.remover_agendamento(ag_id))
                btn_remover.pack(side=RIGHT, padx=10)
        else:
            lbl_aviso = Label(frame_lista, text="Não há horários agendados.", font=("Albert Sans", 14), bg="#f0f0f0")
            lbl_aviso.grid(row=0, column=0, padx=10, pady=5)

        btn_voltar = Button(self.master, text="Voltar", font=("Albert Sans", 14), command=self.voltar_callback)
        btn_voltar.pack()

    def remover_agendamento(self, agendamento_id):
        self.agenda.remover_agendamento(agendamento_id)
        messagebox.showinfo("Sucesso", "Agendamento removido com sucesso.")
        self.ver_horarios_agendados()

    def limpar_tela(self):
        for widget in self.master.winfo_children():
            widget.destroy()
