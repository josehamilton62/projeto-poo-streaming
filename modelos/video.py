from modelos.midia import Midia


class Filme(Midia):
    def __init__(self, titulo, duracao, classificacao, diretor):
        super().__init__(titulo, duracao, classificacao)
        self.diretor = diretor

    def reproduzir(self):
        return f"{super().reproduzir()} [Filme dirigido por {self.diretor}]"

    def descrever(self):
        return f"{super().descrever()} | Diretor: {self.diretor}"

    def __str__(self):
        return f"{super().__str__()} - Filme (Direção: {self.diretor})"


class Documentario(Filme):
    def __init__(self, titulo, duracao, classificacao, diretor, assunto):
        super().__init__(titulo, duracao, classificacao, diretor)
        self.assunto = assunto

    def reproduzir(self):
        return f"{super().reproduzir()} [Documentário sobre {self.assunto}]"

    def descrever(self):
        return f"{super().descrever()} | Assunto: {self.assunto}"

    def __str__(self):
        return f"{super().__str__()} - Documentário (Tema: {self.assunto})"


class Serie(Midia):
    def __init__(self, titulo, duracao, classificacao, temporadas, episodios):
        super().__init__(titulo, duracao, classificacao)
        self.temporadas = temporadas
        self.episodios = episodios

    def reproduzir(self):
        return (
            f"{super().reproduzir()} [Série: {self.temporadas} temporada(s), "
            f"{self.episodios} episódio(s) por temporada]"
        )

    def tempo_total(self):
        return super().tempo_total() * self.temporadas * self.episodios

    def descrever(self):
        return (
            f"{super().descrever()} | Temporadas: {self.temporadas} | "
            f"Episódios por temporada: {self.episodios}"
        )

    def __str__(self):
        return (
            f"{super().__str__()} - Série "
            f"({self.temporadas} temp. x {self.episodios} ep.)"
        )