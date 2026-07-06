from core.interfaces import IPortfolioRepository

# Por que: Atualizacao do DTO para suportar a nova renderizacao da interface.
# A stack tecnologica agora e um objeto complexo contendo a descricao detalhada para alimentar os modais e tooltips.
class LocalPortfolioRepository(IPortfolioRepository):
    
    def get_profile_data(self, language: str = "pt") -> dict:
        
        data_store = {
            "pt": {
                "name": "VINÍCIUS COELHO BEMFICA",
                "role": "ANALISTA DE QA / ENGENHEIRO DE AUTOMAÇÃO DE TESTES",
                "location": "Guarulhos, SP, Brasil",
                "contact": "(11) 98198-2433 | coelhovinicius@yahoo.com.br",
                "social_links": {
                    "LinkedIn": "https://www.linkedin.com/in/coelhovinicius/",
                    "GitHub": "https://github.com/coelhovinicius/"
                },
                "summary": "Automação de Testes e Performance: Criação e manutenção de frameworks de testes automatizados para Web, Mobile e APIs usando Cypress, Playwright, Appium, K6, WireMock e Selenium, seguindo padrões de Clean Code e Page Object Model (POM). Processos de QA e DevOps: Atuação estruturada sob a abordagem Shift-Left, integração e configuração de esteiras de CI/CD automatizadas no Azure DevOps e escrita de especificações técnicas funcionais. Automação com IA e Ferramentas No-Code/Low-Code: Desenvolvimento de fluxos inteligentes de automação de processos usando n8n e plataformas assistidas por inteligência artificial (Lovable, Bubble). Sustentação N1 a N3 e Incidentes: Monitoria de ambientes de produção, análise detalhada de logs para causa raiz e triagem de chamados.",
                "experience_title": "Experiência Profissional",
                "projects": [
                    {
                        "name": "Refuturiza Empreendimento Educacional S.A | Analista de QA e Sustentação",
                        "description": "Planejamento e execução de testes automatizados (E2E e API REST) utilizando Cypress, Postman e Python, integrados diretamente em pipelines de CI/CD via Azure DevOps para grandes projetos (Price up, RH Summit, Rebranding 360°, Gamification). Criação de fluxos de automação no n8n integrados a geradores de código por IA. Triagem N1 a N3 e atuação em War Rooms para indisponibilidades (SSO, AVA e IPs)."
                    },
                    {
                        "name": "Hashtag Treinamentos | Suporte Técnico em Python",
                        "description": "Revisão de Código (Code Review): Avaliação e correção de lógica de programação, erros de sintaxe e arquitetura de scripts. Solução de bugs complexos em tempo real envolvendo automação de tarefas e manipulação de dados."
                    },
                    {
                        "name": "Consultor Independente de TI e QA | Desenvolvedor de Automações",
                        "description": "Prestação de serviços de consultoria em infraestrutura de TI, desenvolvimento de ferramentas personalizadas de automação de dados e estruturação de processos de testes manuais e automatizados."
                    }
                ],
                "tech_stack_title": "Stack Tecnológico",
                "tech_stack": [
                    {"name": "Cypress", "description": "Criação e manutenção de frameworks de testes automatizados E2E seguindo padrões de Clean Code e POM."},
                    {"name": "Playwright", "description": "Desenvolvimento de suítes de testes automatizados robustas e integração em esteiras de CI/CD."},
                    {"name": "Selenium", "description": "Automação de testes funcionais para aplicações Web com foco em cobertura estrutural."},
                    {"name": "Appium", "description": "Automação de testes para plataformas Mobile garantindo a estabilidade em múltiplas resoluções."},
                    {"name": "K6", "description": "Modelagem e execução de testes de carga e performance para validação de resiliência de sistemas."},
                    {"name": "WireMock", "description": "Mocking de APIs para isolamento de testes e aplicação da abordagem Shift-Left."},
                    {"name": "Python", "description": "Construção de scripts funcionais, automação de tarefas, processamento de dados e Code Review."},
                    {"name": "JavaScript", "description": "Desenvolvimento de scripts de suporte e manutenção de frameworks baseados em Node.js."},
                    {"name": "TypeScript", "description": "Implementação de tipagem estática em frameworks de automação para maior governança do código."},
                    {"name": "Azure DevOps", "description": "Integração e configuração de pipelines CI/CD automatizados e homologação de processos GMUD."},
                    {"name": "Postman", "description": "Planejamento e execução de testes automatizados de API REST integrados às esteiras de deploy."},
                    {"name": "n8n", "description": "Desenvolvimento de fluxos inteligentes de automação de processos assistidos por inteligência artificial."}
                ],
                "certifications_title": "Formação e Certificações",
                "certifications": [
                    "MBA em Gestão da Qualidade de Software (Em andamento) - Anhanguera Educacional",
                    "Pós-Graduação em Engenharia de Software: Qualidade e Testes (Em andamento) - Anhanguera Educacional",
                    "Tecnologia em Sistemas de Informação (Concluído) - ENIAC - Centro Universitário",
                    "Testes de Software com Selenium WebDriver (Concluído) - USP - ICMC",
                    "DevOps & Agile Culture (Concluído) - FIAP - Centro Universitário",
                    "Cultura Ágil com Atlassian Jira (Concluído) - Atlassian University",
                    "Especialista Python: Automação e Processamento de Dados (Concluído) - Hashtag Tecnologia",
                    "Testes Automatizados Profissionais"
                ],
                "languages_title": "Idiomas",
                "languages": [
                    "Inglês: Fluente / Proficiência Profissional Completa (Certificado TOEIC)",
                    "Espanhol: Avançado / Fluência para Negócios"
                ]
            },
            "en": {
                "name": "VINÍCIUS COELHO BEMFICA",
                "role": "QA ANALYST / TEST AUTOMATION ENGINEER",
                "location": "Guarulhos, SP, Brazil",
                "contact": "(11) 98198-2433 | coelhovinicius@yahoo.com.br",
                "social_links": {
                    "LinkedIn": "https://www.linkedin.com/in/coelhovinicius/",
                    "GitHub": "https://github.com/coelhovinicius/"
                },
                "summary": "Test Automation & Performance: Creation and maintenance of automated test frameworks for Web, Mobile, and APIs using Cypress, Playwright, Appium, K6, WireMock, and Selenium, following Clean Code and POM standards. QA Processes & DevOps: Structured operation under the Shift-Left approach, integration of CI/CD pipelines in Azure DevOps. AI Automation & No-Code/Low-Code Tools: Development of intelligent process automation workflows using n8n and AI-assisted platforms. L1 to L3 Support & Incidents: Monitoring of production environments, detailed log analysis for root cause diagnosis, and technical triage of critical tickets.",
                "experience_title": "Professional Experience",
                "projects": [
                    {
                        "name": "Refuturiza Empreendimento Educacional S.A | Software QA & Support Analyst",
                        "description": "Execution of automated tests (E2E and REST API) using Cypress, Postman, and Python, integrated into CI/CD pipelines via Azure DevOps for major projects (Price up, RH Summit, Gamification). Creation of automation workflows in n8n integrated with AI code generators. Technical triage and response for L1 to L3 tickets, frontline action in War Rooms."
                    },
                    {
                        "name": "Hashtag Treinamentos | Python Technical Support",
                        "description": "Code Review: Evaluation and correction of programming logic, syntax errors, and script architecture. Real-time resolution of complex bugs involving task automation, data manipulation, and backend script failures."
                    },
                    {
                        "name": "Independent IT & QA Consultant | Automation Developer",
                        "description": "Provision of IT infrastructure consulting services, development of custom data automation tools, and structuring of manual and automated testing processes for direct clients."
                    }
                ],
                "tech_stack_title": "Technical Stack",
                "tech_stack": [
                    {"name": "Cypress", "description": "Creation and maintenance of automated E2E test frameworks following Clean Code and POM standards."},
                    {"name": "Playwright", "description": "Development of robust automated test suites and integration into CI/CD pipelines."},
                    {"name": "Selenium", "description": "Functional test automation for Web applications focusing on structural coverage."},
                    {"name": "Appium", "description": "Test automation for Mobile platforms ensuring stability across multiple resolutions."},
                    {"name": "K6", "description": "Modeling and execution of load and performance tests to validate system resilience."},
                    {"name": "WireMock", "description": "API mocking for test isolation and application of the Shift-Left approach."},
                    {"name": "Python", "description": "Development of functional scripts, task automation, data processing, and Code Review."},
                    {"name": "JavaScript", "description": "Development of support scripts and maintenance of Node.js based frameworks."},
                    {"name": "TypeScript", "description": "Implementation of static typing in automation frameworks for better code governance."},
                    {"name": "Azure DevOps", "description": "Integration and configuration of automated CI/CD pipelines and approval of GMUD processes."},
                    {"name": "Postman", "description": "Planning and execution of automated REST API tests integrated into deployment pipelines."},
                    {"name": "n8n", "description": "Development of intelligent process automation workflows using AI-assisted platforms."}
                ],
                "certifications_title": "Education & Certifications",
                "certifications": [
                    "MBA in Software Quality Management (In Progress)",
                    "Software Engineering - Quality and Testing (In Progress)",
                    "Bachelor's Degree: Information Systems Technology (Concluded)",
                    "ITIL 4 Foundation Overview: Governance & Service Management",
                    "Google AI Agents: Creation and Integration",
                    "Python Specialist: Automation and Data Processing",
                    "Professional Automated Testing"
                ],
                "languages_title": "Languages",
                "languages": [
                    "English: Fluent / Full Professional Proficiency (TOEIC Certified)",
                    "Spanish: Advanced / Business Fluency",
                    "Portuguese: Native Speaker"
                ]
            }
        }
        
        return data_store.get(language, data_store["pt"])