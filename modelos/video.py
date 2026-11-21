from modelos.midia import Midia
from modelos.interfaces import Baixavel, Avaliavel


class Filme(Midia, Baixavel, Avaliavel):
    def __init__(self, titulo, duracao, classificacao, diretor):
        super().__init__(titulo, duracao, classificacao)
        self.diretor = diretor
        self.baixado = False
        self.avaliacoes = []

    def reproduzir(self):
        return f"Reproduzindo o filme '{self.titulo}' (Direção: {self.diretor})"

    def tempo_total(self):
        return self.duracao

    def descrever(self):
        return f"{super().descrever()} | Diretor: {self.diretor}"

    def baixar(self):
        if self.baixado:
            return f"O filme '{self.titulo}' já está baixado."
        self.baixado = True
        return f"Filme '{self.titulo}' baixado com sucesso."

    def remover_download(self):
        if not self.baixado:
            return f"O filme '{self.titulo}' não possui download salvo."
        self.baixado = False
        return f"Download do filme '{self.titulo}' removido."

    def avaliar(self, nota):
        if 1 <= nota <= 5:
            self.avaliacoes.append(nota)
            return f"Avaliação {nota} registrada para '{self.titulo}'."
        return "Nota inválida: informe um valor entre 1 e 5."

    def media_avaliacoes(self):
        if len(self.avaliacoes) == 0:
            return 0.0
        return sum(self.avaliacoes) / len(self.avaliacoes)

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


class Serie(Midia, Avaliavel):
    def __init__(self, titulo, duracao, classificacao, temporadas, episodios):
        super().__init__(titulo, duracao, classificacao)
        self.temporadas = temporadas
        self.episodios = episodios
        self.avaliacoes = []

    def reproduzir(self):
        return (
            f"Reproduzindo a série '{self.titulo}' "
            f"({self.temporadas} temporada(s), {self.episodios} episódio(s) por temporada)"
        )

    def tempo_total(self):
        return self.duracao * self.temporadas * self.episodios

    def descrever(self):
        return (
            f"{super().descrever()} | Temporadas: {self.temporadas} | "
            f"Episódios por temporada: {self.episodios}"
        )

    def avaliar(self, nota):
        if 1 <= nota <= 5:
            self.avaliacoes.append(nota)
            return f"Avaliação {nota} registrada para a série '{self.titulo}'."
        return "Nota inválida: informe um valor entre 1 e 5."

    def media_avaliacoes(self):
        if len(self.avaliacoes) == 0:
            return 0.0
        return sum(self.avaliacoes) / len(self.avaliacoes)

    def __str__(self):
        return (
            f"{super().__str__()} - Série "
            f"({self.temporadas} temp. x {self.episodios} ep.)"
        )