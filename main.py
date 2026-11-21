from modelos.midia import Midia
from modelos.interfaces import Baixavel, Avaliavel
from modelos.video import Filme, Documentario, Serie
from modelos.audio import Musica, Podcast


def main():
    print("===== TESTE DE INSTANCIAÇÃO DA CLASSE ABSTRATA =====")
    try:
        Midia("Mídia Genérica", 60, "Livre")
    except TypeError as erro:
        print(erro)

    # Lista com objetos das classes concretas da hierarquia
    catalogo = [
        Filme("O Auto da Compadecida", 104, "12", "Guel Arraes"),
        Documentario(
            "Nosso Planeta", 50, "Livre", "Alastair Fothergill", "Conservação Ambiental"
        ),
        Serie("Ruptura", 45, "16", 2, 9),
        Musica("Anunciação", 5, "Livre", "FLAC", "Alceu Valença"),
        Podcast("Café da Manhã", 35, "Livre", "MP3", "Gabriela Mayer"),
    ]

    print("\n===== CATÁLOGO DA PLATAFORMA DE STREAMING (PARTE 2) =====\n")

    # Um unico for demonstrando polimorfismo e checagem de interfaces com isinstance()
    for item in catalogo:
        print(item)
        print(f"  Ação: {item.reproduzir()}")
        print(f"  Detalhes: {item.descrever()}")
        print(f"  Tempo total: {item.tempo_total()} min")

        if isinstance(item, Baixavel):
            print(f"  [Baixavel] {item.baixar()}")
            print(f"  [Baixavel] {item.remover_download()}")

        if isinstance(item, Avaliavel):
            print(f"  [Avaliavel] {item.avaliar(5)}")
            print(f"  [Avaliavel] {item.avaliar(4)}")
            print(f"  [Avaliavel] Média de avaliações: {item.media_avaliacoes():.2f}")

        print("-" * 65)

    # Confirmacao explicita dos contratos assumidos por cada tipo
    print("\n===== VERIFICAÇÃO DE CONTRATOS COM isinstance() =====")
    print(f"Filme é Baixavel e Avaliavel? {isinstance(catalogo[0], Baixavel)} / {isinstance(catalogo[0], Avaliavel)}")
    print(f"Série é Baixavel e Avaliavel? {isinstance(catalogo[2], Baixavel)} / {isinstance(catalogo[2], Avaliavel)}")
    print(f"Música é Baixavel e Avaliavel? {isinstance(catalogo[3], Baixavel)} / {isinstance(catalogo[3], Avaliavel)}")
    print(f"Podcast é Baixavel e Avaliavel? {isinstance(catalogo[4], Baixavel)} / {isinstance(catalogo[4], Avaliavel)}")


if __name__ == "__main__":
    main()