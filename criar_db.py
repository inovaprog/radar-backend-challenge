import sqlite3


conn = sqlite3.connect('radar.db')
cursor = conn.cursor()

cursor.executescript("""
DROP TABLE IF EXISTS competicoes;
DROP TABLE IF EXISTS resultados;
CREATE TABLE competicoes(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        modalidade TEXT NOT NULL,
        em_andamento INTEGER NOT NULL
        );
""")

cursor.executescript("""
CREATE TABLE resultados (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        id_competicao INTEGER NOT NULL,
        competicao TEXT NOT NULL,
        modalidade TEXT NOT NULL,
        atleta TEXT NOT NULL,
        valor REAL NOT NULL);
""")

print('Tabela criada com sucesso.')

conn.close()


