import mysql.connector
import pandas as pd
from mysql.connector import Error


#Estabelece a conexão
conexao = mysql.connector.connect(
    host='localhost', # ou o IP do servidor
    user='root',
    password='',
    database='novo'
)
