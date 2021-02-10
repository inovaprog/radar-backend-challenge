from flask import Flask
from flask_restplus import Api, Resource
from src.server.instance import server
import sqlite3
from ..tratamento.convert_salvar import ConverteLitros, ConverterTempo

app, api = server.app, server.api


@api.route("/resultados")
class Resultados(Resource):
    def post(self, ):
        # pegar dados enviados
        request = api.payload
        id_competicao = request['competicao']
        atleta = request['atleta']
        valor = request['valor']
        unidade = request['unidade']
        # verificar qual a modalidade
        conn = sqlite3.connect('radar.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM competicoes WHERE id=:id',
                       {"id": id_competicao})
        resultado = cursor.fetchone()
        if resultado == None:
            return "Id nao corresponde a nenhuma competição", 400
        modalidade = resultado[2]
        nome_competicao = resultado[1]

        # Tratar dados (cenverter para menor unidade de medida)
        if resultado[3] == 1:
            if modalidade == "yoga":
                valor = ConverterTempo(valor, unidade)

            if modalidade == "hidratacao":
                valor = ConverteLitros(valor, unidade)
        # Salvar na tabela de resultados
            if modalidade != "lancamento de dardos":
                cursor.execute(
                    'SELECT * FROM resultados WHERE atleta=:atleta AND modalidade=:modalidade', {"atleta": atleta, "modalidade": modalidade})
                if cursor.fetchall():
                    conn.close
                    return "Atleta já Participou dessa Competição", 400
            else:
                cursor.execute(
                    'SELECT count(1) FROM resultados WHERE atleta=:atleta AND modalidade=:modalidade', {"atleta": atleta, "modalidade": modalidade})
                c = cursor.fetchall()[0][0]
                if c >= 3:
                    conn.close
                    return "Atleta já teve 3 tentativas nessa competição", 400

            cursor.execute('INSERT INTO resultados VALUES (NULL, ?,?,?,?,?)',
                           (id_competicao, nome_competicao, modalidade, atleta, valor))
            conn.commit()
            return 200
        return "Essa Competição já foi finalizada", 400
