from modelos.midia import Midia


class Audio(Midia):
    def __init__(self, titulo, duracao, classificacao, formato):
        super().__init__(titulo, duracao, classificacao)
        self.formato = formato

    def reproduzir(self):
        return f"{super().reproduzir()} [Áudio em formato {self.formato}]"

    def descrever(self):
        return f"{super().descrever()} | Formato de áudio: {self.formato}"

    def __str__(self):
        return f"{super().__str__()} [Áudio {self.formato}]"


class Musica(Audio):
    def __init__(self, titulo, duracao, classificacao, formato, artista):
        super().__init__(titulo, duracao, classificacao, formato)
        self.artista = artista

    def reproduzir(self):
        return f"{super().reproduzir()} - Música de {self.artista}"

    def descrever(self):
        return f"{super().descrever()} | Artista: {self.artista}"

    def __str__(self):
        return f"{super().__str__()} - Música (Artista: {self.artista})"


class Podcast(Audio):
    def __init__(self, titulo, duracao, classificacao, formato, apresentador):
        super().__init__(titulo, duracao, classificacao, formato)
        self.apresentador = apresentador

    def reproduzir(self):
        return f"{super().reproduzir()} - Podcast apresentado por {self.apresentador}"

    def descrever(self):
        return f"{super().descrever()} | Apresentador(a): {self.apresentador}"

    def __str__(self):
        return f"{super().__str__()} - Podcast (Apresentação: {self.apresentador})"