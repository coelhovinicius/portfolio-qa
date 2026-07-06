from abc import ABC, abstractmethod

# Por que: Atualizacao do contrato da interface (Dependency Inversion Principle) para obrigar a implementacao a lidar com o parametro de estado de idioma.
class IPortfolioRepository(ABC):
    @abstractmethod
    def get_profile_data(self, language: str = "pt") -> dict:
        pass