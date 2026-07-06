from abc import ABC, abstractmethod

# Por que: Aplicação do Interface Segregation Principle (ISP) e Dependency Inversion Principle (DIP) do SOLID.
# Criamos um contrato abstrato para o repositório de dados. Isso permite substituir a fonte de dados 
# (por exemplo, de um arquivo local para um banco de dados) sem alterar a regra de negócio que os consome.

class IPortfolioRepository(ABC):
    
    @abstractmethod
    def get_profile_data(self) -> dict:
        """
        Retrieves the main profile information.
        """
        pass