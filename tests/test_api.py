import pytest
from fastapi.testclient import TestClient
from main import app

# Por que: Instanciação em escopo global de módulo do TestClient do FastAPI.
# Permite realizar chamadas HTTP simuladas diretamente na stack da aplicação em memória, 
# sem necessidade de alocar portas ou subir o servidor ASGI (Uvicorn) paralelamente.
client = TestClient(app)

def test_render_portfolio_endpoint_returns_200_ok():
    """
    Validates if the root endpoint is accessible and returns the correct HTTP status 200.
    """
    # Por que: Estruturação padronizada de testes de integração via AAA (Arrange, Act, Assert).
    # Act
    response = client.get("/")
    
    # Por que: Validação estrita de contrato HTTP. O status 200 garante que a rota está resolvida e acessível.
    # Assert
    assert response.status_code == 200

def test_render_portfolio_endpoint_contains_profile_data():
    """
    Validates if the HTML response accurately renders the expected user profile injected via dependency.
    """
    # Act
    response = client.get("/")
    
    # Por que: Conversão explícita do payload binário da resposta para string UTF-8.
    # Garante que caracteres especiais (como acentuação em PT-BR) sejam validados corretamente no fluxo de SSR.
    html_content = response.content.decode("utf-8")
    
    # Assert
    # Por que: Valida a integração completa ponta-a-ponta no backend: 
    # Rota -> Injeção do Repositório -> Jinja2 -> Output Final.
    assert "Vinícius Coelho Bemfica" in html_content
    assert "Senior Quality Assurance Mentor" in html_content