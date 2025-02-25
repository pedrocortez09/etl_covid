import os
import subprocess
import logging

import sys

# Criar a pasta de logs caso não exista
log_dir = "C:\\Users\\Pedro\\repos\\etl_covid\\scripts\\logs"
os.makedirs(log_dir, exist_ok=True)

# Configuração do logging
logging.basicConfig(
    filename=os.path.join(log_dir, "etl_rundeck.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def executar_etl():
    """Executa o ETL chamando o script principal"""
    logging.info("Iniciando ETL via Rundeck...")
    
    try:
        subprocess.run([r"C:\Users\Pedro\repos\etl_covid\etl_covid\Scripts\python.exe", "C:\\Users\\Pedro\\repos\\etl_covid\\scripts\\etl_covid.py"], check=True) 
        logging.info("ETL concluído com sucesso.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Erro ao executar ETL: {e}")

if __name__ == "__main__":
    executar_etl()