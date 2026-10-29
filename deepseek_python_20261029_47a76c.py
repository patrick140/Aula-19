# ============================================================
# IMPORTAÇÕES
# ============================================================
import mysql.connector          # Driver oficial do MySQL para Python (conexão e execução de SQL)
import pandas as pd             # Biblioteca para manipulação de dados (DataFrame, CSV, etc.)
from mysql.connector import Error  # Classe de exceção específica do conector MySQL


# ============================================================
# BLOCO PRINCIPAL — try/except/finally garante limpeza dos recursos
# ============================================================
try:
    # Estabelece a conexão com o banco de dados MySQL
    conexao = mysql.connector.connect(
        host='localhost',       # Endereço do servidor (localhost = máquina local; ou um IP)
        user='root',            # Usuário do MySQL
        password='',            # Senha (vazia neste caso — típico em XAMPP/WAMP local)
        database='novo'         # Nome do banco onde a tabela "aluno" está
    )

    # Verifica se a conexão foi realmente estabelecida antes de prosseguir
    if conexao.is_connected():
        print("Conectado com sucesso!")

        # Cria o cursor — objeto que executa comandos SQL e armazena resultados
        cursor = conexao.cursor()

        # Define a query de INSERT usando placeholders (%s) — evita SQL injection
        sql = "INSERT INTO aluno (matricula, nome, Data_de_nascimento, endereço) VALUES (%s, %s, %s, %s)"

        # Valores que serão substituídos nos placeholders, na mesma ordem
        # ATENÇÃO: "NULL" entre aspas é string, não NULL do SQL. Use None se quiser NULL real.
        valores = ("NULL", 'joana', '1990-01-03', 'Rua do Carmo, 344')

        # ⚠️ COMENTADO — o INSERT NÃO está sendo executado!
        # Enquanto esta linha estiver comentada, nada é gravado no banco.
        #cursor.execute(sql, valores)

        # Confirma (grava) as alterações da transação no banco
        # Sem commit(), o INSERT ficaria só na memória e seria descartado
        conexao.commit()

        # Mostra o ID (AUTO_INCREMENT) gerado na última inserção
        # ⚠️ Aqui retornará 0 ou valor antigo porque o execute() acima está comentado
        print(f"Linha inserida. ID gerado: {cursor.lastrowid}")

        # Executa uma consulta SELECT — traz até 5 linhas da tabela aluno
        cursor.execute("SELECT * FROM aluno LIMIT 5")

        # Busca todos os resultados da consulta e armazena em uma lista de tuplas
        # Cada tupla = uma linha da tabela; cada elemento = um campo
        resultados = cursor.fetchall()

        # ✅ Forma mais limpa: o pandas executa o SELECT diretamente na conexão
        # Já traz os nomes reais das colunas como cabeçalho do DataFrame
        df = pd.read_sql("SELECT * FROM aluno LIMIT 5", conexao)

        # Exporta o DataFrame para um arquivo CSV
        # index=False = não grava o índice (0,1,2...) como coluna no arquivo
        df.to_csv("sql.csv", index=False)

        # Imprime o DataFrame formatado no console
        print(df)

        # Loop que imprime cada linha (tupla) dos resultados "crus" do cursor
        # É redundante com o print(df), pois os dados já foram mostrados acima
        for linha in resultados:
            print(linha)


# ============================================================
# BLOCO DE EXCEÇÃO — captura erros de conexão ou execução SQL
# ============================================================
except Error as e:
    # Exibe a mensagem do erro capturado (conexão recusada, tabela inexistente, etc.)
    print(f"Erro ao conectar ou executar: {e}")


# ============================================================
# BLOCO FINAL — executa SEMPRE, com ou sem erro
# Responsável por liberar os recursos (cursor e conexão)
# ============================================================
finally:
    # Fecha o cursor (se ele chegou a ser criado)
    # 'cursor' in locals() evita erro caso a conexão tenha falhado antes da criação
    if 'cursor' in locals():
        try:
            cursor.close()          # Libera o cursor no servidor MySQL
        except Exception:
            pass                    # Se já estiver fechado ou der erro, ignora silenciosamente

    # Fecha a conexão (se foi criada e ainda está ativa)
    if 'conexao' in locals() and conexao.is_connected():
        conexao.close()             # Encerra a conexão com o servidor
        print("Conexão encerrada.") # Confirmação visual do encerramento