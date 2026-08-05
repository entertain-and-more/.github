# entertain-and-more

[English version](README.md)

**Lokale Spiele-, RPG- und Podcast-Werkzeuge mit optionalen KI-Funktionen.**

entertain-and-more ist der Unterhaltungszweig des `open-bricks`- und `ellmos`-Ökosystems. Die öffentlichen Projekte sind lokal zuerst, nachvollziehbar und für den praktischen Einsatz gedacht: Terminal-Schach, Pen-and-Paper-RPG-Unterstützung und lokale Podcast-Produktion.

> [!HINWEIS]
> **Öffentlicher Navigationsindex:** Abgeglichen mit der Live-GitHub-API am **2026-08-06**. Alle 3 öffentlichen Softwareprojekte und das Profil-Repository sind hier erfasst; private oder interne Projekte werden bewusst nicht genannt.

## Showcase

Die Banner sind die Links; Details stehen in der Tabelle unten.

<p align="center"><a href="https://github.com/entertain-and-more/rpx"><img src="https://raw.githubusercontent.com/entertain-and-more/rpx/master/assets/banner.svg" alt="rpx — RolePlay Xtreme" width="680" style="border:2px solid #a78bfa;border-radius:8px;display:block;margin:0 auto"></a><a href="https://github.com/entertain-and-more/KlangpultLight"><img src="https://raw.githubusercontent.com/entertain-and-more/KlangpultLight/main/docs/assets/banner.svg" alt="KlangpultLight — Klangpult light" width="680" style="border:2px solid #2dd4bf;border-radius:8px;display:block;margin:0 auto"></a></p>

[ChatAndChess](https://github.com/entertain-and-more/ChatAndChess) hat noch kein eigenes Banner-Artwork; es steht in der Tabelle unten.

## Einstieg

| Bedarf | Repository | Schwerpunkt |
|---|---|---|
| Schach im Terminal spielen oder untersuchen | [ChatAndChess](https://github.com/entertain-and-more/ChatAndChess) | Python, Minimax, optionale Claude- und Worker-Modi |
| Pen-and-Paper-RPG-Sitzungen steuern | [rpx](https://github.com/entertain-and-more/rpx) | Karten, Figuren, Sound, Spielschirm, JSON-RPC und PWA |
| Eine Podcast-Folge lokal aufnehmen und planen (Freeware-Funnel-Edition) | [KlangpultLight](https://github.com/entertain-and-more/KlangpultLight) | Recorder + Planer, Live-Transkription, Teleprompter |
| Organisationsprofil und Community-Dateien verstehen | [.github](https://github.com/entertain-and-more/.github) | Profil, Vorlagen und maschinenlesbarer Index |

## Architektur und Zusammenspiel

```mermaid
graph TD
    subgraph Org["entertain-and-more (Spiele, RPG- und Podcast-Werkzeuge)"]
        subgraph Gaming["Spiele & RPG"]
            CC["ChatAndChess (Terminal-Schach und Minimax)"]
            RPX["rpx (RolePlay Xtreme und PWA)"]
        end
        subgraph Content["Podcast & Content"]
            KLANG["KlangpultLight (Recorder + Planer, Freeware-Funnel-Edition)"]
        end
    end
    ELLMOS["ellmos-ai (Agenten- und LLM-Infrastruktur)"]
    OPEN["open-bricks (Software-Dach)"]
    CC -.-> ELLMOS
    RPX -.-> ELLMOS
    KLANG -.-> ELLMOS
    Org --> OPEN
```

## Öffentlicher Repository-Index

| Projekt | Zweck | Öffentliche Aktivität |
|---|---|---|
| [ChatAndChess](https://github.com/entertain-and-more/ChatAndChess) | Terminal-Schach mit Minimax, Regeln, Taktikanalyse und optionalen Claude-Modi | Letzter Push: **2026-07-27** |
| [rpx](https://github.com/entertain-and-more/rpx) | Lokales RPG-Kontrollzentrum für Spielleitung, Karten, Sound, Spielschirm und LLM-Steuerung | Letzter Push: **2026-08-05** |
| [KlangpultLight](https://github.com/entertain-and-more/KlangpultLight) | Klangpult light: kostenlose Recorder- und Planer-Podcast-Produktion (Freeware-Funnel-Edition des kostenpflichtigen, privaten `Klangpult`) | Letzter Push: **2026-08-03** |
| [.github](https://github.com/entertain-and-more/.github) | Organisationsprofil, Community-Vorlagen und `llms.txt` | Geprüft: **2026-08-06** |

## Grundsätze

- **Menschen und Spielleitung zuerst:** KI unterstützt Spiel und Vorbereitung, ersetzt aber keine menschliche Gestaltung.
- **Lokal zuerst und offline-fähig:** Die Kernfunktionen benötigen keine Cloud-Abonnements.
- **Nachvollziehbar und anpassbar:** Kleine, verständliche Projekte erleichtern Prüfung, Forks und Erweiterungen.
- **Ökosystem-kompatibel:** Die Werkzeuge verweisen sauber auf [ellmos-ai](https://github.com/ellmos-ai) und [open-bricks](https://github.com/open-bricks).

Maschinenlesbarer Kontext: [llms.txt](../llms.txt) · Organisation: [github.com/entertain-and-more](https://github.com/entertain-and-more)
