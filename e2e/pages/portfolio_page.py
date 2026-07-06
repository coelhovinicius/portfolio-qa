from e2e.pages.base_page import BasePage

# Por que: Aplicação estrita do padrão Page Object Model (POM). 
# Separa a lógica de negócios e as asserções (nos testes) dos seletores de CSS/DOM.
class PortfolioPage(BasePage):
    def __init__(self):
        super().__init__()
        
        # Por que: Centralização de Locators. Se o layout mudar, a manutenção é feita em um único ponto.
        self.header_title = "header h1"
        self.tech_stack_list = "#tech-stack ul li"
        self.summary_section = "#summary p"

    def get_header_text(self) -> str:
        """
        Extracts the text from the main header.
        """
        return self.page.locator(self.header_title).inner_text()

    def get_tech_stack_items(self) -> list[str]:
        """
        Retrieves all items within the tech stack list as an array of strings.
        """
        # Por que: Retorna dados puros e serializados para a camada de teste. A página nunca faz assertividade,
        # sua única responsabilidade é prover o estado atual do DOM.
        return self.page.locator(self.tech_stack_list).all_inner_texts()

    def get_summary_text(self) -> str:
        """
        Extracts the summary paragraph text.
        """
        return self.page.locator(self.summary_section).inner_text()

# Por que: Exposição da instância Singleton do POM, mimetizando a sintaxe 'export default new Page()'
# utilizada frequentemente em TS/JS. Garante que os testes consumam o mesmo objeto estrutural em memória.
portfolio_page = PortfolioPage()