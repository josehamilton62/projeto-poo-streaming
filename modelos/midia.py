class Midia:
    def __init__(self, titulo, duracao, classificacao):
        self.titulo = titulo
        self.duracao = duracao
        self.classificacao = classificacao

    def reproduzir(self):
        return f"Reproduzindo '{self.titulo}'"

    def tempo_total(self):
        return self.duracao

    def descrever(self):
        return (
            f"Título: {self.titulo} | Duração base: {self.duracao} min | "
            f"Classificação: {self.classificacao}"
        )

    def __str__(self):
        return f"{self.titulo} ({self.duracao} min, Classificação: {self.classificacao})"