# Diagrama de classes

Este diagrama representa a modelagem do **Projeto Final (Grupo 1 — Plataforma de Streaming)** e é atualizado a cada parte da disciplina.

```mermaid
classDiagram
    class Midia {
        <<abstract>>
        +titulo
        +duracao
        +classificacao
        +reproduzir()*
        +tempo_total()*
        +descrever()
        +__str__()
    }

    class Baixavel {
        <<interface>>
        +baixar()
        +remover_download()
    }

    class Avaliavel {
        <<interface>>
        +avaliar(nota)
        +media_avaliacoes()
    }

    class Filme {
        +diretor
        +baixado
        +avaliacoes
        +reproduzir()
        +tempo_total()
        +descrever()
        +baixar()
        +remover_download()
        +avaliar(nota)
        +media_avaliacoes()
        +__str__()
    }

    class Documentario {
        +assunto
        +reproduzir()
        +descrever()
        +__str__()
    }

    class Serie {
        +temporadas
        +episodios
        +avaliacoes
        +reproduzir()
        +tempo_total()
        +descrever()
        +avaliar(nota)
        +media_avaliacoes()
        +__str__()
    }

    class Audio {
        +formato
        +reproduzir()
        +tempo_total()
        +descrever()
        +__str__()
    }

    class Musica {
        +artista
        +baixado
        +reproduzir()
        +descrever()
        +baixar()
        +remover_download()
        +__str__()
    }

    class Podcast {
        +apresentador
        +baixado
        +reproduzir()
        +descrever()
        +baixar()
        +remover_download()
        +__str__()
    }

    Midia <|-- Filme
    Filme <|-- Documentario
    Midia <|-- Serie
    Midia <|-- Audio
    Audio <|-- Musica
    Audio <|-- Podcast

    Baixavel <|.. Filme
    Baixavel <|.. Musica
    Baixavel <|.. Podcast
    Avaliavel <|.. Filme
    Avaliavel <|.. Serie
```

## Como ler

- Seta contínua com ponta vazada (`<|--`): **herança** ("é um").
- Seta tracejada com ponta vazada (`<|..`): a classe **implementa** a interface ("sabe fazer").
- `<<abstract>>`: classe abstrata. Os métodos abstratos levam `*` depois do nome e aparecem em itálico.
- `<<interface>>`: interface, apenas com métodos.

## Histórico

- **Parte 1:** classes, atributos, métodos e herança.
- **Parte 2:** classe abstrata (`Midia`) e interfaces (`Baixavel` e `Avaliavel`).
