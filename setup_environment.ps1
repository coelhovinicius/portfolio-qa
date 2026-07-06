# Por que: Automação da configuração do ambiente no Windows via PowerShell. 
# Garante um setup determinístico, isolando dependências do sistema global (Boas práticas de Python).

Write-Output "Iniciando configuracao do ambiente virtual..."

# Por que: Cria o ambiente virtual local na pasta do projeto.
python -m venv venv

# Por que: Ativa o ambiente virtual restrito a este terminal PowerShell.
.\venv\Scripts\Activate.ps1

Write-Output "Instalando dependencias via requirements.txt..."

# Por que: Atualiza o pip para evitar falhas de resolucao de pacotes antes de instalar as libs do projeto.
python -m pip install --upgrade pip
pip install -r requirements.txt

Write-Output "Setup concluido. Para iniciar o servidor, execute: uvicorn main:app --reload --env-file .env"