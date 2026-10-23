import mysql.connector
from mysql.connector import Error

try:
    #Estabelece a conexão
    conexao = mysql.connector.connect(
        host='localhost',       # ou o IP do servidor
        user='root',
        password='',
        database='teste'
    )

    if conexao.is_connected():
        print("Conectado com sucesso!")

        #Cria um cursor (objeto que permite executar comandos)
        cursor = conexao.cursor()

        #Executa uma consulta
        cursor.execute("SELECT * FROM aluno LIMIT 5")

        #Busca os resultados
        resultados = cursor.fetchall()
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