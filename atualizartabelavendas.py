import sqlite3

def atualizar_tabela_vendas():
    conn = sqlite3.connect("mantra_spa.db")
    cursor = conn.execute("PRAGMA table_info(Vendas)")
    columns = [info[1] for info in cursor.fetchall()]
    if 'servico' not in columns:
        conn.execute('''
            ALTER TABLE Vendas ADD COLUMN servico TEXT
        ''')
    conn.close()

if __name__ == "__main__":
    atualizar_tabela_vendas()
