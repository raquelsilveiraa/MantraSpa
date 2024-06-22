from tkinter import *
from tkinter import messagebox
from Agenda import Agenda

class GerenciadorAgendamentos:
    def __init__(self, master, agenda, servicos, salvar_dados_callback, voltar_callback):
        self.master = master
        self.agenda = agenda
        self.servicos = servicos
        self.salvar_dados_callback = salvar_dados_callback
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
                self.salvar_dados_callback()
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
        agendamentos = self.agenda.carregar_agendamentos()
        if agendamentos:
            window = Toplevel(self.master)
            window.title("Horários Agendados")
            window.geometry("400x400")
            window.configure(bg="#f0f0f0")

            frame_agendamentos = Frame(window, bg="#f0f0f0")
            frame_agendamentos.pack(padx=20, pady=20)

            lbl_titulo = Label(frame_agendamentos, text="Horários Agendados", font=("Albert Sans", 18, "bold"), bg="#f0f0f0")
            lbl_titulo.pack(pady=10)

            for agendamento in agendamentos:
                lbl_agendamento = Label(frame_agendamentos, text=f"{agendamento['data']} às {agendamento['horario']}: {agendamento['servico']['nome']} - Cliente: {agendamento['cliente']}", font=("Albert Sans", 12), bg="#f0f0f0")
                lbl_agendamento.pack(anchor="w", padx=10, pady=5)
        else:
            messagebox.showinfo("Informação", "Não há horários agendados.")

    def limpar_tela(self):
        for widget in self.master.winfo_children():
            widget.destroy()
