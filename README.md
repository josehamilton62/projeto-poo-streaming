# Plataforma de Streaming — Grupo 1

**Tema:** Streaming

**Disciplina:** Programação Orientada a Objetos (IFCE Maranguape)

## Integrantes

- José Hamilton Meneses Filho (`josehamilton62`)
- Ana Maria Gonçalves Alves (`anaalves67`)

## Objetivo do sistema

Gerenciar uma plataforma de streaming de filmes, documentários, séries, músicas e podcasts, permitindo controlar o catálogo de mídias, downloads, avaliações, assinantes, playlists e histórico de reprodução no terminal.

## Diagrama de classes

O diagrama de classes está em [docs/diagrama.md](docs/diagrama.md).

## Parte 1: hierarquia

A classe base `Midia` centraliza os dados comuns de qualquer conteúdo (`titulo`, `duracao` e `classificacao`), especializando-se em três níveis de herança: `Filme` → `Documentario`, `Serie`, e `Audio` → `Musica` e `Podcast`.

## Parte 2: classes abstratas e interfaces

- **Classe abstrata:** `Midia`, com os métodos abstratos `reproduzir()` e `tempo_total()` e os métodos concretos `descrever()` e `__str__()`.
- **Interfaces e quem as implementa:**

| Interface   | Métodos                               | Classes que implementam                         |
| ----------- | ------------------------------------- | ----------------------------------------------- |
| `Baixavel`  | `baixar()`, `remover_download()`      | `Filme` (e `Documentario`), `Musica`, `Podcast` |
| `Avaliavel` | `avaliar(nota)`, `media_avaliacoes()` | `Filme` (e `Documentario`), `Serie`             |

## Como executar

Abra o terminal na pasta do projeto e execute:

```bash
python main.py
```
