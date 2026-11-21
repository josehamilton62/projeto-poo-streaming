from abc import ABC, abstractmethod


class Baixavel(ABC):
    @abstractmethod
    def baixar(self):
        pass

    @abstractmethod
    def remover_download(self):
        pass


class Avaliavel(ABC):
    @abstractmethod
    def avaliar(self, nota):
        pass

    @abstractmethod
    def media_avaliacoes(self):
        pass