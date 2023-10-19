import sqlite3

class Atendimento:
    def __init__(self, periodo, assinatura, data, horario, atendente, comentario):
        self.periodo = periodo
        self.assinatura = assinatura
        self.data = data
        self.horario = horario
        self.atendente = atendente
        self.comentario = comentario

class Database:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS atendimentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            periodo TEXT,
            assinatura TEXT,
            data TEXT,
            horario TEXT,
            atendente TEXT,
            comentario TEXT
        )''')
        self.conn.commit()

    def insert_atendimento(self, atendimento):
        self.cur.execute('''INSERT INTO atendimentos (periodo, assinatura, data, horario, atendente, comentario)
            VALUES (?, ?, ?, ?, ?, ?)''', (atendimento.periodo, atendimento.assinatura, atendimento.data,
                                           atendimento.horario, atendimento.atendente, atendimento.comentario))
        self.conn.commit()

    def get_all_atendimentos(self):
        self.cur.execute("SELECT * FROM atendimentos")
        return self.cur.fetchall()

    def get_atendimento_by_id(self, id):
        self.cur.execute("SELECT * FROM atendimentos WHERE id=?", (id,))
        return self.cur.fetchone()

    def update_atendimento(self, id, atendimento):
        self.cur.execute('''UPDATE atendimentos
            SET periodo=?, assinatura=?, data=?, horario=?, atendente=?, comentario=?
            WHERE id=?''', (atendimento.periodo, atendimento.assinatura, atendimento.data,
                            atendimento.horario, atendimento.atendente, atendimento.comentario, id))
        self.conn.commit()

    def delete_atendimento(self, id):
        self.cur.execute("DELETE FROM atendimentos WHERE id=?", (id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
