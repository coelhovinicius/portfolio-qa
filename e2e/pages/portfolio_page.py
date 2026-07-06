from e2e.pages.base_page import BasePage

# Por que: Aplicação estrita do padrão Page Object Model (POM). 
# Separa a lógica de negócios e as asserções (nos testes) dos seletores de CSS/DOM.
class PortfolioPage(BasePage):
    def __init__(self):
        super().__init__()
        
        # Por que: Centralização de Locators. Expansão para mapear as novas seções de Idiomas e Certificações.
        self.header_title = "header h1"
        self.social_links = "#social-links a"
        self.project_titles = "#projects .project-card h3"
        self.tech_stack_list = "#tech-stack ul li"
        self.certifications_list = "#certifications ul li"
        self.languages_list = "#languages ul li"
        self.summary_section = "#summary p"

    def get_header_text(self) -> str:
        """
        Extracts the text from the main header.
        """
        return self.page.locator(self.header_title).inner_text()

    def get_social_links_data(self) -> dict[str, str]:
        """
        Extracts social links as a dictionary containing the platform text as key and href as value.
        """
        elements = self.page.locator(self.social_links).all()
        links_data = {}
        for element in elements:
            platform = element.inner_text()
            href = element.get_attribute("href")
            if href:
                links_data[platform] = href
        return links_data

    def get_project_titles(self) -> list[str]:
        """
        Retrieves all project titles rendered in the UI.
        """
        return self.page.locator(self.project_titles).all_inner_texts()

    def get_tech_stack_items(self) -> list[str]:
        """
        Retrieves all items within the tech stack list as an array of strings.
        """
        return self.page.locator(self.tech_stack_list).all_inner_texts()

    def get_certification_items(self) -> list[str]:
        """
        Retrieves all items within the certifications list.
        """
        # Por que: Expansão do POM para garantir a cobertura visual do background acadêmico.
        return self.page.locator(self.certifications_list).all_inner_texts()

    def get_language_items(self) -> list[str]:
        """
        Retrieves all items within the languages list.
        """
        # Por que: Coleta o array de idiomas renderizados pelo SSR para asserção no runner.
        return self.page.locator(self.languages_list).all_inner_texts()

    def get_summary_text(self) -> str:
        """
        Extracts the summary paragraph text.
        """
        return self.page.locator(self.summary_section).inner_text()

# Por que: Exposição da instância Singleton do POM.
portfolio_page = PortfolioPage()