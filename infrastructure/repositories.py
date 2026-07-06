from core.interfaces import IPortfolioRepository

# Por que: Implementação concreta da interface. Mantém a responsabilidade única de fornecer os dados (SRP).
# Os dados refletem o seu profile técnico e background.

class LocalPortfolioRepository(IPortfolioRepository):
    
    def get_profile_data(self) -> dict:
        # Por que: Retorno estruturado em dicionário simulando um DTO (Data Transfer Object).
        return {
            "name": "Vinícius Coelho Bemfica",
            "role": "Senior Quality Assurance Mentor & IT Support",
            "location": "Guarulhos, São Paulo, Brazil",
            "summary": "Technology professional focused on IT automation and software engineering. Expertise in creating custom AI agents, CI/CD pipelines, and robust automated test suites.",
            "tech_stack": [
                "Cypress", "Playwright", "Selenium", "Python", "Azure DevOps"
            ],
            "certifications": [
                "ITIL 4", 
                "Google IA Agents", 
                "Advanced Software Testing", 
                "MBA in Software Quality Management"
            ],
            "interests": [
                "System Monitoring Automation", 
                "Financial Data Processing", 
                "AI Agent Integration for Ticket Triage"
            ]
        }