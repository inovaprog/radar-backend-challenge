# Desafio de Backend RadarFit

- [Instalação](#instalação)
- [Parametrização](#dados)
- [EndPoints](#endpoints)
  - [Competições](#competições)  
  - [Resultados](#resultados)
  - [Ranking](#ranking)
    


## Instruções de Execução

### Instalação

0. Requisitos:
  - git
  - Python3
  - pip3

1. Clonar esse repositório:
`$ git clone https://github.com/inovaprog/radar-backend-challenge.git`

2. Entrar na pasta do projeto:
`$ cd radar-backend-challenge/`

3. Instalar as Dependências:
`$ pip3 install -r requirements.txt`

4. Criar Banco de Dados:
`$ python3 criar_db.py`

4. Executar:
`$ python3 main.py`

**Será executado em** `http://127.0.0.1:5000`

### Dados:
#### As unidades de medidas aceitas são:
Todos os resultados são um JSON com Chave e Valor

- Modalidade Hidratação: L e ml
- Modalidade Perda de Peso: cal
- Modalidade Yoga: s, m ou h
- Modalidade Lancamento de Dardos: m

Para modalidade de Lançamento de dardos deve-se cadastrar 3 resultados para cada atleta. (O maior valor será utilizado para o resultado).

O Resultado da modalidade Yoga será dado hora, minutos e segundos.

A varival em_andamento: 0 - Competição encerrada / 1 - Competição em andamento


### Endpoints:
### Competições:
#### 1. Adicionar nova competição:  **POST** `/competicoes` 
Corpo da requisição:
```json
{
"nome" : "Campionato Brasileiro de Lancamento de Dardo",
"modalidade" : "lancamento de dardos"
}
```
Modalidades permitidas: ('hidratacao', 'yoga', 'perda de peso' ou 'lancamento de dardos')

Cadastro com sucesso: **STATUS: 200 OK**
```json
[
    {
    "id": 2,
    "nome": "Campeonato Itabirano de Dardo 2",
    "modalidade": "lancamento de dardos",
    "em_andamento": 1
  }
]
```
Cadastro com erro: **STATUS: 400 Bad Request**
- Competição já cadastrada

#### 2. Ver Todos as competições:  **GET** `/competicoes` 


Consulta realizada com sucesso: **STATUS: 200 OK**
```json
[
    {
    "id": 1,
    "nome": "Campeonato Itabirano de Dardo",
    "modalidade": "lancamento de dardos",
    "em_andamento": 1
  },
  {
    "id": 2,
    "nome": "Campeonato Itabirano de Dardo 2",
    "modalidade": "lancamento de dardos",
    "em_andamento": 1
  }
]
```
#### 3. Finalizar uma Competição:  **PUT** `/competicoes` 
Corpo da requisição:
```json
{
"id" : 1
}
```
Consulta realizada com sucesso: **STATUS: 200 OK**
```javascript
    "Competição Finalizada com Sucesso"
 ```


### Resultados:
#### 1. Adicionar novo resultado:  **POST** `/resultados` 
Corpo da requisição:
```json
{
	"competicao":1,
	"atleta": "Paula",
	"valor": 10,
	"unidade": "m"
}
```

Cadastro com sucesso: **STATUS: 200 OK**

Cadastro com erro: **STATUS: 400 Bad Request**
- Id não pertence a nenhuma competição
- Competição Finalizada
- Atleta já participou da competição
- Atleta já cadastrou 3 resultados (Lançamento de Dardos)

### Ranking:
#### 3. Ver Resultado Parcial ou Final de uma Competição:  **POST** `/ranking` 
Corpo da requisição:
```json
{
"id" : 1
}
```
```json
  Consulta realizada com sucesso: **STATUS: 200
    "atleta": "Paula",
    "Pontuação": 100.0
  },
  {
    "atleta": "Carlos",
    "Pontuação": 50.0
  }
 ```
 Consulta com erro: **STATUS: 400 Bad Request**
- Id não pertence a nenhuma competição

