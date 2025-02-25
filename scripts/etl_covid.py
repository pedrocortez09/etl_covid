import sqlite3
import logging
import os
import requests
import pandas as pd
import schedule
import time

log_dir = "C:\\Users\\Pedro\\repos\\etl_covid\\scripts\\logs"  # Caminho para a pasta de logs

# Configuração do Logging
logging.basicConfig(
    filename=os.path.join(log_dir, "etl_log.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

url_base = "https://storage.googleapis.com/covid19-open-data/v3/"
diretorio_dados = "../data/raw"

# Criação do diretório se não existir
os.makedirs(diretorio_dados, exist_ok=True)

arquivos_csv = [
    #"index.csv",
    #"demographics.csv",
    "economy.csv",
    "epidemiology.csv",
    #"lawatlas-emergency-declarations.csv",
    #"geography.csv",
    #"health.csv",
    #"hospitalizations.csv",
    "mobility.csv"
    #"oxford-government-response.csv",
    #"worldbank.csv",
    #"vaccinations.csv",
    #"Global_vaccination_search_insights.csv",
    #"by-sex.csv",
    #"by-age.csv",
    #"weather.csv",
    #"google-search-trends.csv",
    #"facility-boundary-us-all.csv"
]

banco_dados = "../covid_data.db"

def baixar_arquivos():
    """ Baixar arquivos do site """
    for arquivo in arquivos_csv:
        url = url_base + arquivo
        caminho_arquivo = os.path.join(diretorio_dados, arquivo)

        try:
            logging.info(f"Baixando {arquivo}...")
            response = requests.get(url)
            response.raise_for_status()

            with open(caminho_arquivo, "wb") as file:
                file.write(response.content)
            logging.info(f"{arquivo} baixado com sucesso!")

        except requests.RequestException as e:
            logging.error(f"Erro ao baixar {arquivo}: {e}")


def salvar_no_banco():
    """ Transforma os CSV's em dataframe e salva no banco de dados """
    conexao = sqlite3.connect(banco_dados)
    total_arquivos_processados = 0

    for arquivo in arquivos_csv:
        caminho_arquivo = os.path.join(diretorio_dados, arquivo)

        if os.path.exists(caminho_arquivo):
            try:
                df = pd.read_csv(caminho_arquivo)
                tabela_nome = arquivo.replace(".csv", "").replace("-", "_")
                df.to_sql(tabela_nome, conexao, if_exists="replace", index=False, chunksize=1000000)
                logging.info(f"{arquivo} salvo no banco de dados com {len(df)} registros.")
                total_arquivos_processados += 1
            except Exception as e:
                logging.error(f"Erro ao salvar {arquivo} no banco: {e}")

    conexao.close()
    logging.info(f"Total de {total_arquivos_processados} arquivos processados no banco.")


def criar_tabelas():
    """ Criação de tabelas analíticas a partir dos dados brutos """
    conexao = sqlite3.connect(banco_dados)
    cursor = conexao.cursor()

    try:
        # Criar uma tabela agregada de total de casos por país
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS casos_por_pais AS
            SELECT location_key, SUM(new_confirmed) AS total_casos
            FROM epidemiology
            GROUP BY location_key
        """)
        logging.info("Tabela 'casos_por_pais' criada com sucesso.")

        # Média de mobilidade por país
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS mobilidade_media AS
            SELECT location_key, AVG(mobility_retail_and_recreation) AS media_mobilidade
            FROM mobility
            GROUP BY location_key
        """)
        logging.info("Tabela 'mobilidade_media' criada com sucesso.")

    except Exception as e:
        logging.error(f"Erro ao criar tabelas analíticas: {e}")

    conexao.commit()
    conexao.close()


def executar_etl():
    logging.info("Iniciando processo de ETL...")
    baixar_arquivos()
    salvar_no_banco()
    criar_tabelas()
    logging.info("Processo ETL concluído.")


if __name__ == "__main__":
    # Rodar manualmente caso o script seja executado diretamente
    executar_etl()

    # Agendamento para rodar todo dia às 13:00
    schedule.every().day.at("13:00").do(executar_etl)

    # Loop para manter o script rodando
    while True:
        schedule.run_pending()
        time.sleep(60)  # Verifica a cada minuto
