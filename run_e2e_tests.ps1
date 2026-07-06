# Por que: Automação nativa de setup e execução do Playwright em ambiente Windows.
# Isola o processo de instalação de navegadores e garante que o servidor backend esteja em execução paralelamente.

Write-Output "Ativando ambiente virtual isolado..."
.\venv\Scripts\Activate.ps1

Write-Output "Instalando bindings do Playwright para Python e o plugin Pytest..."
python -m pip install playwright pytest-playwright

Write-Output "Instalando dependencias binarias do Chromium..."
# Por que: Instalação direcionada apenas ao Chromium para otimizar o tempo de execução local.
playwright install chromium

Write-Output "Acionando suite de testes End-to-End da UI..."
# Por que: A utilização de 'python -m pytest' injeta o contexto da raiz no sys.path,
# permitindo a resolução de dependências internas como 'from e2e.pages.portfolio_page import portfolio_page'.
python -m pytest e2e/tests/ -v --browser chromium