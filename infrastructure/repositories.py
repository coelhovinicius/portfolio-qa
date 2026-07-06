from core.interfaces import IPortfolioRepository

# Por que: Atualizacao do DTO para refletir a profundidade tecnica do curriculo.
# A inclusao de novas chaves ('languages') e expansao das listas ('tech_stack', 'certifications') ocorre sem quebrar o contrato da interface.
class LocalPortfolioRepository(IPortfolioRepository):
    
    def get_profile_data(self) -> dict:
        return {
            "name": "Vinícius Coelho Bemfica",
            "role": "Senior Quality Assurance Mentor & IT Support",
            "location": "Guarulhos, São Paulo, Brazil",
            "social_links": {
                "LinkedIn": "https://www.linkedin.com/in/coelhovinicius",
                "GitHub": "https://github.com/coelhovinicius"
            },
            # Por que: O resumo agora vende a arquitetura completa, focando em performance, Shift-Left e resolucao de incidentes.
            "summary": "Automação de testes, performance e cultura Shift-Left. Especialista na criação de frameworks (Web, Mobile, API) e integração de esteiras CI/CD automatizadas no Azure DevOps. Sólida atuação em sustentação N1 a N3, gestão de incidentes, análise de logs para causa raiz, Governança ágil (CAB/GMUD) e otimização de entregas utilizando IA e plataformas Low-Code.",
            "projects": [
                {
                    "name": "Refuturiza - Ecossistema de Aplicações",
                    "description": "Automação E2E e API (Price up, RH Summit, Rebranding 360°, Gamification e Vagas). Integração de testes no Azure DevOps, triagem N1-N3 via GLPI e defesa técnica em reuniões de CAB."
                },
                {
                    "name": "Mentoria & Code Review em Python",
                    "description": "Revisão arquitetural (Clean Code), correção de sintaxe e resolução de bugs complexos em tempo real focados em automação de tarefas e processamento de dados."
                },
                {
                    "name": "Automação Assistida por IA",
                    "description": "Desenvolvimento de fluxos inteligentes com n8n e plataformas Low-Code (Lovable, Bubble) integrados a geradores de código por IA para acelerar ciclos de testes e rotinas de suporte."
                }
            ],
            "tech_stack": [
                "Cypress", "Playwright", "Selenium", "Appium", "K6", "WireMock", "Python", "JavaScript", "TypeScript", "Azure DevOps", "Postman"
            ],
            "certifications": [
                "MBA em Gestão da Qualidade de Software (Em andamento)",
                "Pós-Graduação em Engenharia de Software: Qualidade e Testes (Em andamento)",
                "ITIL 4: Governança e Gestão de Serviços",
                "Agentes de IA Google: Criação e Integração",
                "Especialista Python: Automação e Processamento de Dados",
                "Testes Automatizados Profissionais"
            ],
            "interests": [
                "System Monitoring Automation", 
                "Financial Data Processing", 
                "AI Agent Integration for Ticket Triage"
            ],
            "languages": [
                "Inglês: Fluente / Proficiência Profissional Completa (Certificado TOEIC)",
                "Espanhol: Avançado / Fluência para Negócios"
            ]
        }