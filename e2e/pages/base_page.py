from playwright.sync_api import Page

# Por que: Implementação do conceito DRY (Don't Repeat Yourself) na camada de UI Automation.
# A BasePage centraliza as operações fundamentais que toda página web compartilha, 
# removendo a necessidade de reinjetar a classe Page do Playwright em cada objeto específico.

class BasePage:
    def __init__(self):
        self.page: Page = None

    def set_page(self, page: Page):
        """
        Injects the active Playwright Page instance into the POM.
        """
        # Por que: Desacoplamento da inicialização. Permite que o framework de testes (Pytest) 
        # gerencie o ciclo de vida do browser e repasse a sessão ativa para o objeto de página.
        self.page = page

    def navigate(self, url: str):
        """
        Navigates to the specified URL.
        """
        self.page.goto(url)