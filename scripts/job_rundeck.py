import requests

# URL do Rundeck
RUNDECK_URL = "http://localhost:4440/project/ETL_COVID/job/show/50457b86-15b1-4712-b98f-220a8986b64c"

# Token de autenticação do Rundeck
API_TOKEN = "sto8JnEb7HWopLQocxhqzFWM0PoPhnsr"

# Cabeçalhos da requisição
HEADERS = {
    "X-Rundeck-Auth-Token": API_TOKEN,
    "Accept": "application/json"
}

def executar_job():
    """Executa um job no Rundeck"""
    response = requests.post(RUNDECK_URL, headers=HEADERS)

    if response.status_code == 200:
        print("✅ Job do Rundeck iniciado com sucesso!")
    else:
        print(f"❌ Erro ao iniciar job: {response.status_code} - {response.text}")

if __name__ == "__main__":
    executar_job()
