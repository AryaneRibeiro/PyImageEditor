from abc import ABC, abstractmethod

class Filtro(ABC):

    @abstractmethod
    def aplicar(self, imagem):
        raise NotImplementedError(
            "O filtro deve implementar o método aplicar()"
        )