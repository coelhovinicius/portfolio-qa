from core.interfaces import IPortfolioRepository

# Por que: Implementação concreta da interface. Mantém a responsabilidade única de fornecer os dados (SRP).
# Os dados refletem o seu profile técnico e background.

class LocalPortfolioRepository(IPortfolioRepository):
    
    def get_profile_data(self) -> dict:
        # Por que: Retorno estruturado em dicionário simulando um DTO (Data Transfer Object).
        # A inclusão do nó 'projects' e 'social_links' expande a carga de dados sem quebrar o contrato da interface.
        return {
            "name": "Vinícius Coelho Bemfica",
            "role": "Senior Quality Assurance Mentor & IT Support",
            "location": "Guarulhos, São Paulo, Brazil",
            "social_links": {
                "LinkedIn": "https://linkedin.com/br/coelhovinicius",
                "GitHub": "https://github.com/coelhovinicius"
            },
            "summary": "Technology professional focused on IT automation and software engineering. Expertise in creating custom AI agents, CI/CD pipelines, and robust automated test suites.",
            "projects": [
                {
                    "name": "Price up",
                    "description": "Atuação focada no mapeamento de qualidade, cobertura de automação de testes e rastreamento de métricas de performance dentro da arquitetura do sistema."
                }
            ],
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