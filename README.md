# Projeto ETL COVID

## 📌 Objetivo
Este projeto tem como objetivo a construção de uma base analítica a partir dos datasets disponibilizados de forma denormalizada. Além da extração dos dados, realizamos o tratamento e a carga em um banco de dados, seguindo todas as etapas do processo ETL (Extract, Transform, Load).

Para automatização, utilizamos tanto o Rundeck quanto as bibliotecas `Logging` e `Schedule`, garantindo que o processo ocorra de forma eficiente e monitorável.

---

## 📂 Fonte de Dados
Os dados utilizados neste projeto foram obtidos a partir de [Fonte dos Dados](https://health.google.com/covid-19/opendata/raw-data). O dataset inclui informações sobre casos de COVID-19, óbitos, vacinação e outras métricas relevantes.

---

## 🛠️ Ferramentas Utilizadas
- **Python**: Linguagem principal para o desenvolvimento do ETL.
- **SQLite**: Banco de dados para armazenar a tabela analítica.
- **Pandas**: Manipulação e transformação de dados.
- **Schedule**: Automação do agendamento do ETL.
- **Logging**: Monitoramento e registro de logs do processo.
- **Rundeck**: Orquestração de jobs para automação do ETL.
- **Git/GitHub**: Controle de versão e armazenamento do código.

---

## 📜 Estrutura do Repositório
```
├── data/                 # Dados brutos e processados
│   ├── raw/              # Dados brutos
├── notebooks/            # Notebooks Jupyter com análises e testes
├── scripts/              # Scripts Python para o ETL e automação
│   ├── logs/             # Logs gerados pelo processo ETL
│   ├── etl_covid.py      # Script principal do ETL
│   ├── steps_rundeck.py  # Automação via Rundeck (steps)
│   ├── job_rundeck.py    # Automação via Rundeck (jobs)
├── requirements.txt      # Dependências do projeto
├── README.md             # Documentação do projeto
└── .gitignore            # Arquivos e pastas ignoradas pelo Git
```

---

## 📊 Tabelas Analítica

### Casos por país

| Coluna           | Tipo       | Descrição |
|------------------|-----------|-----------|
| location key     | TEXT      | País |
| total_casos      | INT       | Total de Casos |


### Mobilidade por país

| Coluna           | Tipo       | Descrição |
|------------------|-----------|-----------|
| location key     | TEXT      | País |
| media_mobilidade | FLOAT     | Média de mobilidade |



---

## 🚀 Como Executar o Projeto

### 1️⃣ Configurar o ambiente
```bash
python -m venv env
source env/bin/activate  # Linux/macOS
env\Scripts\activate    # Windows
pip install -r requirements.txt
```

### 2️⃣ Rodar o ETL manualmente
```bash
python scripts/etl_covid.py
```

### 3️⃣ Agendar o ETL automaticamente
```bash
python scripts/steps_rundeck.py  # Para automação via Rundeck
python scripts/job_rundeck.py    # Para execução remota via Rundeck
```

---

## 📝 Logs Gerados
Todos os logs do processo ETL são armazenados na pasta `scripts/logs/`. Eles podem ser usados para monitorar a execução e identificar possíveis erros.


---

📌 **Autor:** Pedro Cortez
📆 **Última Atualização:** [25/02/2025]
