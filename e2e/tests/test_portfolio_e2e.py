import os
import pytest
from playwright.sync_api import Page
from e2e.pages.portfolio_page import portfolio_page
from dotenv import load_dotenv

# Por que: Carregamento de Environment Management via .env.
load_dotenv()
BASE_URL = f"http://{os.getenv('HOST', '127.0.0.1')}:{os.getenv('PORT', '8000')}"

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
    # Por que: Adequacao ao uppercase inserido no novo DTO.
    assert "VINÍCIUS COELHO BEMFICA" in header_text

def test_portfolio_social_links_contain_valid_hrefs():
    """
    Validates if the social links section correctly renders the LinkedIn and GitHub URLs.
    """
    social_links = portfolio_page.get_social_links_data()
    assert "LinkedIn" in social_links
    assert social_links["LinkedIn"] == "https://www.linkedin.com/in/coelhovinicius/"
    assert "GitHub" in social_links
    assert social_links["GitHub"] == "https://github.com/coelhovinicius/"

def test_portfolio_renders_featured_projects():
    """
    Validates if the featured projects section is rendering the correct project titles based on the updated CV.
    """
    project_titles = portfolio_page.get_project_titles()
    
    # Por que: Atualizacao das assercoes para validar o mapeamento exato das chaves de projetos atualizadas.
    assert "Refuturiza Empreendimento Educacional S.A | Analista de QA e Sustentação" in project_titles
    assert "Hashtag Treinamentos | Suporte Técnico em Python" in project_titles
    assert "Consultor Independente de TI e QA | Desenvolvedor de Automações" in project_titles

def test_portfolio_tech_stack_contains_expected_frameworks():
    """
    Validates if the Tech Stack list in the UI contains the core and advanced frameworks.
    """
    tech_stack = portfolio_page.get_tech_stack_items()
    assert "Python" in tech_stack
    assert "Playwright" in tech_stack
    assert "Appium" in tech_stack
    assert "K6" in tech_stack
    assert "WireMock" in tech_stack
    # Por que: Inclusao da ferramenta low-code na cobertura da stack.
    assert "n8n" in tech_stack

def test_portfolio_renders_certifications_and_academic_background():
    """
    Validates if the certifications and academic degrees are present.
    """
    certifications = portfolio_page.get_certification_items()
    # Por que: Assercao estrita atestando a concatenacao do nome da instituicao (Anhanguera Educacional).
    assert "MBA em Gestão da Qualidade de Software (Em andamento) - Anhanguera Educacional" in certifications
    assert "Testes Automatizados Profissionais" in certifications

def test_portfolio_renders_languages():
    """
    Validates if the language proficiency levels are displayed correctly.
    """
    languages = portfolio_page.get_language_items()
    assert any("Inglês: Fluente" in lang for lang in languages)
    assert any("Espanhol: Avançado" in lang for lang in languages)