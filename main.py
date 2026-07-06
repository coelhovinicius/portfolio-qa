import os
from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
from core.interfaces import IPortfolioRepository
from infrastructure.repositories import LocalPortfolioRepository

# Por que: Carrega as variáveis definidas no arquivo .env no startup da aplicação.
load_dotenv()

# Por que: Inicialização do framework com metadados recuperados das variáveis de ambiente.
app = FastAPI(title=os.getenv("PROJECT_TITLE", "QA Portfolio"))

# Por que: Configuração do motor de templates Jinja2. Separa a lógica de backend (Python) da camada de apresentação (HTML).
templates = Jinja2Templates(directory="templates")

# Por que: Função provedora para Injeção de Dependência.
# O framework FastAPI invocará esta função para instanciar o repositório, facilitando a injeção de Mocks durante testes unitários.
def get_portfolio_repository() -> IPortfolioRepository:
    return LocalPortfolioRepository()

@app.get("/")
async def render_portfolio(request: Request, repository: IPortfolioRepository = Depends(get_portfolio_repository)):
    """
    Renders the main portfolio page.
    """
    # Por que: O endpoint atua apenas como um Controller. Ele delega a busca de dados para o repositório injetado.
    profile_data = repository.get_profile_data()
    
    # Por que: Retorna o template HTML populado com o dicionário de dados. 
    # Assinatura de parâmetros atualizada para evitar DeprecationWarning do Starlette.
    return templates.TemplateResponse(
        request=request,
        name="index.html", 
        context={"profile": profile_data}
    )