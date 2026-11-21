from abc import ABC, abstractmethod


class Midia(ABC):
    def __init__(self, titulo, duracao, classificacao):
        self.titulo = titulo
        self.duracao = duracao
        self.classificacao = classificacao

    @abstractmethod
    def reproduzir(self):
        pass

    @abstractmethod
    def tempo_total(self):
        pass

    def descrever(self):
        return (
            f"Título: {self.titulo} | Duração base: {self.duracao} min | "
            f"Classificação: {self.classificacao}"
        )

    def __str__(self):
        return f"{self.titulo} ({self.duracao} min, Classificação: {self.classificacao})"