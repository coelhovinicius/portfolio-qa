import os
import pytest
from playwright.sync_api import Page
from e2e.pages.portfolio_page import portfolio_page
from dotenv import load_dotenv

# Por que: Carregamento de Environment Management via .env.
load_dotenv()
BASE_URL = f"http://{os.getenv('HOST', '127.0.0.1')}:{os.getenv('PORT', '8000')}"

# Por que: Fixture global de escopo de função executada automaticamente (autouse=True).
@pytest.fixture(autouse=True)
def setup_test_context(page: Page):
    portfolio_page.set_page(page)
    portfolio_page.navigate(BASE_URL)
    yield

def test_portfolio_header_displays_correct_profile_name():
    """
    Validates if the header renders the correct profile name from the backend.
    """
    header_text = portfolio_page.get_header_text()
    assert "Vinícius Coelho Bemfica" in header_text

def test_portfolio_social_links_contain_valid_hrefs():
    """
    Validates if the social links section correctly renders the LinkedIn and GitHub URLs.
    """
    # Act
    social_links = portfolio_page.get_social_links_data()
    
    # Assert
    # Por que: Valida a injeção correta da URL no atributo href da âncora, garantindo a navegação funcional de recrutadores.
    assert "LinkedIn" in social_links
    assert social_links["LinkedIn"] == "https://www.linkedin.com/in/coelhovinicius"
    assert "GitHub" in social_links
    assert social_links["GitHub"] == "https://github.com/coelhovinicius"

def test_portfolio_renders_featured_projects():
    """
    Validates if the featured projects section is rendering the correct project titles.
    """
    # Act
    project_titles = portfolio_page.get_project_titles()
    
    # Assert
    assert "Price up" in project_titles

def test_portfolio_tech_stack_contains_expected_frameworks():
    """
    Validates if the Tech Stack list in the UI contains the core frameworks.
    """
    tech_stack = portfolio_page.get_tech_stack_items()
    assert "Python" in tech_stack
    assert "Playwright" in tech_stack
    assert "Azure DevOps" in tech_stack