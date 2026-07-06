import os
import pytest
from playwright.sync_api import Page
from e2e.pages.portfolio_page import portfolio_page
from dotenv import load_dotenv

# Por que: Carregamento de Environment Management via .env.
# Permite que o teste E2E consuma dinamicamente a URL base do ambiente atual sem chumbamento de strings no código.
load_dotenv()
BASE_URL = f"http://{os.getenv('HOST', '127.0.0.1')}:{os.getenv('PORT', '8000')}"

# Por que: Fixture global de escopo de função executada automaticamente (autouse=True).
# Injeta o contexto da página do browser fornecido pelo pytest-playwright na instância Singleton do nosso POM
# e executa a navegação de setup antes da execução do bloco Act/Assert de cada teste.
@pytest.fixture(autouse=True)
def setup_test_context(page: Page):
    portfolio_page.set_page(page)
    portfolio_page.navigate(BASE_URL)
    yield

def test_portfolio_header_displays_correct_profile_name():
    """
    Validates if the header renders the correct profile name from the backend.
    """
    # Act
    header_text = portfolio_page.get_header_text()
    
    # Assert
    # Por que: Validação de ponta a ponta garantindo que o DTO do Python backend 
    # foi renderizado com sucesso no SSR (Jinja2) e está visível no DOM do browser.
    assert "Vinícius Coelho Bemfica" in header_text

def test_portfolio_tech_stack_contains_expected_frameworks():
    """
    Validates if the Tech Stack list in the UI contains the core frameworks.
    """
    # Act
    tech_stack = portfolio_page.get_tech_stack_items()
    
    # Assert
    # Por que: Validação granular do array injetado.
    assert "Python" in tech_stack
    assert "Playwright" in tech_stack
    assert "Azure DevOps" in tech_stack