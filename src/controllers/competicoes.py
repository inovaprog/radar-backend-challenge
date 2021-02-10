from flask import Flask
from flask_restplus import Api, Resource
from src.server.instance import server
import sqlite3

app, api = server.app, server.api
MODALIDADES = ["hidratacao", "yoga", "perda de peso", "lancamento de dardos"]


@api.route("/competicoes")
class Competicoes(Resource):
    def get(self,):
        conn = sqlite3.connect('radar.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM competicoes')
        resultado = cursor.fetchall()
        res_final = []
        for row in resultado:
           d = {
               "id": row[0],
               "nome": row[1],
               "modalidade": row[2],
               "em_andamento": row[3]
           }
           res_final.append(d)

        return res_final, 200
        conn.close()

    def post(self,):
        # pegar dados enviados
        request = api.payload
        nome = request['nome']
        modalidade = request['modalidade']

        # Conferir se modalidade existe
        if modalidade in MODALIDADES:
            # conferir se não há confito de nome
            conn = sqlite3.connect('radar.db')
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM competicoes WHERE nome=:nome AND modalidade=:modalidade',
                           {"nome": nome, "modalidade": modalidade})
            if cursor.fetchall():
                conn.close()
                return "Competição já cadastrada", 400

            # Enviar dados para o banco
            cursor.execute("INSERT INTO competicoes VALUES (NULL, ?, ?, 1)",
                           (nome, modalidade))
            conn.commit()

            cursor.execute('SELECT * FROM competicoes WHERE nome=:nome AND modalidade=:modalidade',
                           {"nome": nome, "modalidade": modalidade})

            resultado = cursor.fetchall()
            res_final = []
            for row in resultado:
                d = {
                "id": row[0],
                "nome": row[1],
                "modalidade": row[2],
                "em_andamento": row[3]
                }
                res_final.append(d)

            return res_final, 200

            conn.close()

        else:
            return "Modalidade nao existe! Utilize no campo Modalidade: ('hidratacao', 'yoga', 'perda de peso' ou 'lancamento de dardos')", 400

    def put(self,):
        # Bpegar os dados (id da competicao)
        request = api.payload
        id_competicao = int(request['id'])
        print(id_competicao)
        # Setar em_andamento para 0
        conn = sqlite3.connect('radar.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE competicoes SET em_andamento = 0 WHERE id=:id',{"id": id_competicao})
        conn.commit()
        conn.close()
        return "Competição Finalizada com Sucesso", 200
