import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

class BancoDeDadosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualizar Banco de Dados")
        self.root.geometry("1000x600")

        self.conn = self.conectar_banco()
        
        self.frame_tabelas = ttk.Frame(self.root)
        self.frame_tabelas.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        self.frame_dados = ttk.Frame(self.root)
        self.frame_dados.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.frame_detalhes = ttk.Frame(self.root)
        self.frame_detalhes.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

        self.tabelas = ["Servicos", "Funcionarios", "Vendas", "Promocoes", "Avaliacoes", "Agendamentos"]
        self.criar_lista_tabelas()
        self.treeview = None

        self.criar_botoes()

    def conectar_banco(self):
        conn = sqlite3.connect("mantra_spa.db")
        return conn

    def criar_lista_tabelas(self):
        label = ttk.Label(self.frame_tabelas, text="Tabelas", font=("Arial", 16))
        label.pack(pady=5)
        
        self.lista_tabelas = tk.Listbox(self.frame_tabelas, font=("Arial", 14))
        self.lista_tabelas.pack(fill=tk.BOTH, expand=True)
        
        for tabela in self.tabelas:
            self.lista_tabelas.insert(tk.END, tabela)

        self.lista_tabelas.bind("<<ListboxSelect>>", self.mostrar_tabela)

    def criar_botoes(self):
        btn_atualizar = ttk.Button(self.frame_detalhes, text="Atualizar", command=self.atualizar_visualizacao)
        btn_atualizar.pack(side=tk.LEFT, padx=5, pady=5)

        btn_fechar = ttk.Button(self.frame_detalhes, text="Fechar", command=self.fechar_aplicacao)
        btn_fechar.pack(side=tk.RIGHT, padx=5, pady=5)

    def mostrar_tabela(self, event):
        if not self.lista_tabelas.curselection():
            return
        
        tabela_selecionada = self.lista_tabelas.get(self.lista_tabelas.curselection())
        
        cursor = self.conn.execute(f"SELECT * FROM {tabela_selecionada}")
        colunas = [descricao[0] for descricao in cursor.description]
        registros = cursor.fetchall()

        if self.treeview:
            self.treeview.destroy()

        self.treeview = ttk.Treeview(self.frame_dados, columns=colunas, show="headings")
        self.treeview.pack(fill=tk.BOTH, expand=True)

        for coluna in colunas:
            self.treeview.heading(coluna, text=coluna)
            self.treeview.column(coluna, width=100, anchor=tk.CENTER)

        for registro in registros:
            self.treeview.insert("", tk.END, values=registro)

        self.treeview.bind("<ButtonRelease-1>", self.mostrar_detalhes)

    def mostrar_detalhes(self, event):
        for item in self.treeview.selection():
            item_text = self.treeview.item(item, "values")
            detalhe_texto = "\n".join(f"{col}: {val}" for col, val in zip(self.treeview["columns"], item_text))
            messagebox.showinfo("Detalhes do Registro", detalhe_texto)

    def atualizar_visualizacao(self):
        if self.lista_tabelas.curselection():
            self.mostrar_tabela(None)

    def fechar_aplicacao(self):
        self.conn.close()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = BancoDeDadosApp(root)
    root.mainloop()
