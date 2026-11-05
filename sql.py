import mysql.connector
import pandas as pd
from mysql.connector import Error

try:
    #Estabelece a conexão
    conexao = mysql.connector.connect(
        host='sql10.freesqldatabase.com',       # ou o IP do servidor
        user='sql10840023',
        password='PAutaXirUL',
        database='sql10840023'
    )

    if conexao.is_connected():
        print("Conectado com sucesso!")         

except Error as e:
    print(f"Erro ao conectar ou executar: {e}")

finally:
    
    #Fecha a conexão (se foi criada e ainda está conectada)
    if 'conexao' in locals() and conexao.is_connected():
        conexao.close()
        print("Conexão encerrada.")