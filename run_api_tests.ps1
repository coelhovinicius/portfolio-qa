# Por que: Automação da execução de validação no ambiente nativo Windows.
# Isola o processo garantindo que o contexto do ambiente virtual esteja presente antes de acionar a suíte do Pytest.

Write-Output "Ativando ambiente virtual isolado..."
.\venv\Scripts\Activate.ps1

Write-Output "Validando/Instalando dependencias do framework de testes..."
# Por que: O httpx e pytest são pacotes requeridos pelo TestClient do FastAPI.
python -m pip install pytest httpx

Write-Output "Acionando suite de testes de integracao via Pytest..."
# Por que: A utilização de 'python -m pytest' ao invés do executável direto adiciona 
# implicitamente a raiz do projeto no sys.path, resolvendo o erro de importação do main.py.
python -m pytest tests/ -v