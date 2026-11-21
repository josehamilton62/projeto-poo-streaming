from modelos.midia import Midia
from modelos.interfaces import Baixavel


class Audio(Midia):
    def __init__(self, titulo, duracao, classificacao, formato):
        super().__init__(titulo, duracao, classificacao)
        self.formato = formato

    def reproduzir(self):
        return f"Reproduzindo áudio '{self.titulo}' em formato {self.formato}"

    def tempo_total(self):
        return self.duracao

    def descrever(self):
        return f"{super().descrever()} | Formato de áudio: {self.formato}"

    def __str__(self):
        return f"{super().__str__()} [Áudio {self.formato}]"


class Musica(Audio, Baixavel):
    def __init__(self, titulo, duracao, classificacao, formato, artista):
        super().__init__(titulo, duracao, classificacao, formato)
        self.artista = artista
        self.baixado = False

    def reproduzir(self):
        return f"{super().reproduzir()} - Música de {self.artista}"

    def descrever(self):
        return f"{super().descrever()} | Artista: {self.artista}"

    def baixar(self):
        if self.baixado:
            return f"A música '{self.titulo}' já está baixada."
        self.baixado = True
        return f"Música '{self.titulo}' baixada com sucesso."

    def remover_download(self):
        if not self.baixado:
            return f"A música '{self.titulo}' não possui download salvo."
        self.baixado = False
        return f"Download da música '{self.titulo}' removido."

    def __str__(self):
        return f"{super().__str__()} - Música (Artista: {self.artista})"


class Podcast(Audio, Baixavel):
    def __init__(self, titulo, duracao, classificacao, formato, apresentador):
        super().__init__(titulo, duracao, classificacao, formato)
        self.apresentador = apresentador
        self.baixado = False

    def reproduzir(self):
        return f"{super().reproduzir()} - Podcast apresentado por {self.apresentador}"

    def descrever(self):
        return f"{super().descrever()} | Apresentador(a): {self.apresentador}"

    def baixar(self):
        if self.baixado:
            return f"O podcast '{self.titulo}' já está baixado."
        self.baixado = True
        return f"Podcast '{self.titulo}' baixado com sucesso."

    def remover_download(self):
        if not self.baixado:
            return f"O podcast '{self.titulo}' não possui download salvo."
        self.baixado = False
        return f"Download do podcast '{self.titulo}' removido."

    def __str__(self):
        return f"{super().__str__()} - Podcast (Apresentação: {self.apresentador})"