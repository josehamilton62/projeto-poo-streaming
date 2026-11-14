from modelos.midia import Midia
from modelos.video import Filme, Documentario, Serie
from modelos.audio import Audio, Musica, Podcast


def main():
    # Criando objetos das classes da hierarquia e guardando em uma unica lista
    catalogo = [
        Filme("O Auto da Compadecida", 104, "12", "Guel Arraes"),
        Documentario(
            "Nosso Planeta", 50, "Livre", "Alastair Fothergill", "Conservação Ambiental"
        ),
        Serie("Ruptura", 45, "16", 2, 9),
        Musica("Anunciação", 5, "Livre", "FLAC", "Alceu Valença"),
        Podcast("Café da Manhã", 35, "Livre", "MP3", "Gabriela Mayer"),
    ]

    print("===== CATÁLOGO DA PLATAFORMA DE STREAMING (GRUPO 1) =====\n")

    # Percorrendo a lista com um unico laco for (demonstracao de polimorfismo)
    for item in catalogo:
        print(item)
        print(f"Ação: {item.reproduzir()}")
        print(f"Detalhes: {item.descrever()}")
        print(f"Tempo total: {item.tempo_total()} min")
        print("-" * 65)

    # Demonstracao do uso de isinstance() verificando que objetos de classes folha
    # tambem sao instancias das superclasses intermediarias e da classe base Midia
    print("\n===== VERIFICAÇÃO DE HERANÇA COM isinstance() =====")
    doc_teste = catalogo[1]
    musica_teste = catalogo[3]

    print(
        f"'{doc_teste.titulo}' é instância de Documentario? "
        f"{isinstance(doc_teste, Documentario)}"
    )
    print(
        f"'{doc_teste.titulo}' também é instância de Filme? "
        f"{isinstance(doc_teste, Filme)}"
    )
    print(
        f"'{doc_teste.titulo}' também é instância de Midia? "
        f"{isinstance(doc_teste, Midia)}"
    )
    print(
        f"'{musica_teste.titulo}' é instância de Audio e de Midia? "
        f"{isinstance(musica_teste, Audio) and isinstance(musica_teste, Midia)}"
    )


if __name__ == "__main__":
    main()