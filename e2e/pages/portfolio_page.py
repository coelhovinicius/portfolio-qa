from e2e.pages.base_page import BasePage

class PortfolioPage(BasePage):
    def __init__(self):
        super().__init__()
        
        # Por que: Atualizacao dos locators devido a migracao das tags HTML (de .project-card h3 para .accordion-header span).
        self.header_title = "header h1"
        self.social_links = "#social-links a"
        self.project_titles = ".accordion-header span:first-child"
        self.tech_stack_list = "#tech-stack ul li.tech-tag"
        self.certifications_list = "#certifications ul li"
        self.languages_list = "#languages ul li"
        self.summary_section = "#summary p"

    def get_header_text(self) -> str:
        return self.page.locator(self.header_title).inner_text()

    def get_social_links_data(self) -> dict[str, str]:
        elements = self.page.locator(self.social_links).all()
        links_data = {}
        for element in elements:
            platform = element.inner_text()
            href = element.get_attribute("href")
            if href:
                links_data[platform] = href
        return links_data

    def get_project_titles(self) -> list[str]:
        return self.page.locator(self.project_titles).all_inner_texts()

    def get_tech_stack_items(self) -> list[str]:
        # Por que: O inner_text agora retorna o texto da tag E do tooltip oculto (ex: 'Cypress\nDescricao...'). 
        # A camada de teste lidara com esse parse.
        return self.page.locator(self.tech_stack_list).all_inner_texts()

    def get_certification_items(self) -> list[str]:
        return self.page.locator(self.certifications_list).all_inner_texts()

    def get_language_items(self) -> list[str]:
        return self.page.locator(self.languages_list).all_inner_texts()

    def get_summary_text(self) -> str:
        return self.page.locator(self.summary_section).inner_text()

portfolio_page = PortfolioPage()