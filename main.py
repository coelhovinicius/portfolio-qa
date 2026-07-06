from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from infrastructure.repositories import LocalPortfolioRepository

# Por que: Inicializacao do servidor ASGI e do motor de Server-Side Rendering (SSR).
app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Por que: Inversao de Dependencia instanciando o repositorio que contem as arvores de dados isoladas.
repository = LocalPortfolioRepository()

@app.get("/")
def get_portfolio(request: Request, lang: str = "pt"):
    """
    Renders the portfolio page based on the selected language via query parameters.
    Default fallback is Portuguese ('pt').
    """
    # Por que: A rota intercepta o 'lang' na URL (ex: /?lang=en) e aciona o DTO correspondente.
    profile_data = repository.get_profile_data(language=lang)
    
    # Por que: O contexto do Jinja2 agora recebe os dados localizados e o estado atual da lingua para definir o estilo ativo no front-end.
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "profile": profile_data,
        "current_lang": lang
    })