import os
import pytest
from playwright.sync_api import Page
from e2e.pages.portfolio_page import portfolio_page
from dotenv import load_dotenv

load_dotenv()
BASE_URL = f"http://{os.getenv('HOST', '127.0.0.1')}:{os.getenv('PORT', '8000')}"

@pytest.fixture(autouse=True)
def setup_test_context(page: Page):
    portfolio_page.set_page(page)
    portfolio_page.navigate(BASE_URL)
    yield

def test_portfolio_header_displays_correct_profile_name():
    header_text = portfolio_page.get_header_text()
    assert "VINÍCIUS COELHO BEMFICA" in header_text

def test_portfolio_social_links_contain_valid_hrefs():
    social_links = portfolio_page.get_social_links_data()
    assert "LinkedIn" in social_links
    assert social_links["LinkedIn"] == "https://www.linkedin.com/in/coelhovinicius/"
    assert "GitHub" in social_links
    assert social_links["GitHub"] == "https://github.com/coelhovinicius/"

def test_portfolio_renders_featured_projects_in_accordion():
    """
    Validates if the Accordion titles are rendering correctly.
    """
    project_titles = portfolio_page.get_project_titles()
    assert any("Refuturiza Empreendimento Educacional" in title for title in project_titles)
    assert any("Hashtag Treinamentos" in title for title in project_titles)
    assert any("Consultor Independente de TI" in title for title in project_titles)

def test_portfolio_tech_stack_contains_expected_frameworks_with_tooltip():
    """
    Validates if the Tech Stack list in the UI contains the frameworks, parsing out the hidden tooltip text.
    """
    tech_stack = portfolio_page.get_tech_stack_items()
    # Por que: A string capturada vem como 'Ferramenta\nTooltip'. Validamos a contencao parcial.
    assert any("Python" in tech for tech in tech_stack)
    assert any("Playwright" in tech for tech in tech_stack)
    assert any("Appium" in tech for tech in tech_stack)
    assert any("n8n" in tech for tech in tech_stack)

def test_portfolio_renders_certifications_and_academic_background():
    certifications = portfolio_page.get_certification_items()
    assert any("MBA em Gestão da Qualidade" in cert for cert in certifications)
    assert any("Testes Automatizados Profissionais" in cert for cert in certifications)

def test_portfolio_renders_languages():
    languages = portfolio_page.get_language_items()
    assert any("Inglês: Fluente" in lang for lang in languages)
    assert any("Espanhol: Avançado" in lang for lang in languages)