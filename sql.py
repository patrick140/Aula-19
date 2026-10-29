import mysql.connector
import pandas as pd
from mysql.connector import Error

try:
    #Estabelece a conexão
    conexao = mysql.connector.connect(
        host='localhost',       # ou o IP do servidor
        user='root',
        password='',
        database='novo'
    )

    if conexao.is_connected():
        print("Conectado com sucesso!")

        #Cria um cursor (objeto que permite executar comandos)
        cursor = conexao.cursor()
        sql = "INSERT INTO aluno (matricula, nome, Data_de_nascimento, endereço) VALUES (%s, %s, %s, %s)"
        valores = ("NULL", 'joana', '1990-01-03', 'Rua do Carmo, 344')

        #cursor.execute(sql, valores)
        conexao.commit()   # <-- ESSENCIAL para gravar
        print(f"Linha inserida. ID gerado: {cursor.lastrowid}")

        #Executa uma consulta
        cursor.execute("SELECT * FROM aluno LIMIT 5")
        

        #Busca os resultados
        resultados = cursor.fetchall()
        df = pd.read_sql("SELECT * FROM aluno LIMIT 5", conexao)
        df.to_csv("sql.csv", index=False)
        print(df)
        for linha in resultados:
            print(linha)
            

except Error as e:
    print(f"Erro ao conectar ou executar: {e}")

finally:
    #Fecha o cursor (se foi criado)
    if 'cursor' in locals():
        try:
            cursor.close()
        except Exception:
            pass  #Se já estiver fechado ou ocorrer erro, ignora
    
    #Fecha a conexão (se foi criada e ainda está conectada)
    if 'conexao' in locals() and conexao.is_connected():
        conexao.close()
        print("Conexão encerrada.")