import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("mantra_spa.db")
        self.criar_tabelas()
        self.atualizar_tabelas()

    def criar_tabelas(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS Servicos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    descricao TEXT NOT NULL,
                    beneficios TEXT NOT NULL,
                    local TEXT NOT NULL
                )
            ''')
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS Funcionarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    cargo TEXT NOT NULL
                )
            ''')
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS Vendas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    valor REAL NOT NULL,
                    servico TEXT NOT NULL
                )
            ''')
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS Promocoes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    descricao TEXT NOT NULL
                )
            ''')
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS Avaliacoes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cliente TEXT NOT NULL,
                    avaliacao TEXT NOT NULL
                )
            ''')
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS Agendamentos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    data TEXT NOT NULL,
                    horario TEXT NOT NULL,
                    servico_id INTEGER NOT NULL,
                    cliente TEXT NOT NULL,
                    FOREIGN KEY (servico_id) REFERENCES Servicos(id)
                )
            ''')

    def atualizar_tabelas(self):
        with self.conn:
            # Adiciona a coluna 'servico' se ela não existir na tabela Vendas
            cursor = self.conn.execute("PRAGMA table_info(Vendas)")
            columns = [info[1] for info in cursor.fetchall()]
            if 'servico' not in columns:
                self.conn.execute('''
                    ALTER TABLE Vendas ADD COLUMN servico TEXT
                ''')
