<p align="center">
  <img src="logo.jpg" alt="entertain-and-more logo" width="925">
</p>

<p align="center">
  <a href="https://github.com/entertain-and-more"><img src="https://img.shields.io/badge/GitHub-Organization--Profile-blue?style=flat-square&logo=github" alt="GitHub Org Profile"></a>
  <a href="https://github.com/ellmos-ai"><img src="https://img.shields.io/badge/Ecosystem-ellmos--ai-purple?style=flat-square" alt="Ecosystem ellmos-ai"></a>
  <a href="https://github.com/open-bricks"><img src="https://img.shields.io/badge/Umbrella-open--bricks-teal?style=flat-square" alt="Open Bricks"></a>
  <a href="https://github.com/entertain-and-more/.github/blob/main/llms.txt"><img src="https://img.shields.io/badge/LLM--Context-llms.txt-green?style=flat-square" alt="llms.txt"></a>
  <img src="https://img.shields.io/badge/Architecture-Local--First-informational?style=flat-square" alt="Local First">
  <img src="https://img.shields.io/badge/Stack-Python%20%7C%20PySide6%20%7C%20Minimax-orange?style=flat-square" alt="Stack">
  <img src="https://img.shields.io/badge/License-MIT-brightgreen?style=flat-square" alt="License MIT">
</p>

# entertain-and-more

**Local-first play tools for chess, tabletop RPG sessions, and AI-assisted game-master workflows.**

entertain-and-more is the playful software branch of the `ellmos` ecosystem. The repositories here focus on small, inspectable game and entertainment projects: terminal chess with optional Claude integration, tabletop role-playing support, game-master tooling, maps, soundboards, campaign bundles, and experiments where AI assists human players and Game Masters without taking control away from the player.

> [!NOTE]
> **Public Navigation Index:** Refreshed against live GitHub API metadata on **2026-07-26**. Every public repository visible in `entertain-and-more` is 100% indexed here. Private or internal work is intentionally omitted.

> [!TIP]
> **Local-First & Offline Resilience:** All applications in `entertain-and-more` operate fully offline by default. AI features (such as Anthropic API modes, Claude Code file-worker integration, and JSON-RPC control bridges) are optional layers designed to enhance tabletop preparation and gameplay without requiring cloud connectivity for core functions.

## Start Here

| Need | Repository | Best Entry Point |
|---|---|---|
| Play or study a Python chess game with local play, Minimax, and optional Claude modes | [ChatAndChess](https://github.com/entertain-and-more/ChatAndChess) | Rules, tactics analyzer, worker mode, and test workflow |
| Run a tabletop RPG control center for sessions, maps, music, player screens, and AI prompts | [rpx](https://github.com/entertain-and-more/rpx) | RPX Pro dashboard, campaign bundle, JSON-RPC, and PWA companion |
| Understand this organization profile and shared community files | [.github](https://github.com/entertain-and-more/.github) | Organization profile, issue templates, and community health files |

## System Architecture & Interaction Flow

```mermaid
graph TD
    subgraph Org ["entertain-and-more (Public Games & RPG Suite)"]
        subgraph CC ["ChatAndChess"]
            CC_Core["Python Standard Library Core Engine"]
            CC_Bot["Minimax Bot & UCI Protocol Interface"]
            CC_AI["Claude API Mode & Claude Code File Worker"]
            CC_Core --> CC_Bot
            CC_Core --> CC_AI
        end

        subgraph RPX ["rpx (RolePlay Xtreme)"]
            RPX_GUI["PySide6 Desktop Control Center"]
            RPX_Tools["Maps, Audio, Soundboard & Notes"]
            RPX_View["Second-Screen Player View & PWA Companion"]
            RPX_RPC["JSON-RPC LLM Bridge & Campaign Bundles (v1 ZIP)"]
            RPX_GUI --> RPX_Tools
            RPX_GUI --> RPX_View
            RPX_GUI --> RPX_RPC
        end
    end

    subgraph Eco ["Ecosystem Integration Network"]
        ELLMOS["ellmos-ai (Agent & LLM Infrastructure)"]
        OPEN["open-bricks (Open Software Suite Dach-Org)"]
        DESK["file-bricks & dev-bricks (Desktop Apps & Dev Tools)"]
    end

    CC_AI -.-> ELLMOS
    RPX_RPC -.-> ELLMOS
    Org -.-> OPEN
    Org -.-> DESK
```

## Public Repository Directory

Checked **2026-07-26**: the public organization currently contains these three repositories. No public repository is missing from this directory.

| Project | Focus | Stack | Discovery Terms | Public Activity |
|---|---|---|---|---|
| [ChatAndChess](https://github.com/entertain-and-more/ChatAndChess) | Terminal chess with local play, Minimax depth, optional Claude API mode, Claude Code worker mode, full chess rules, UCI input, engine-hint modes, and a tactics analyzer | Python standard library, optional Anthropic API | `terminal chess`, `Python Minimax chess`, `Claude Code chess worker`, `UCI chess moves`, `engine hint chess`, `chess tactics analyzer` | Public repo; last public push **2026-07-25** |
| [rpx](https://github.com/entertain-and-more/rpx) | RPX Pro / RolePlay Xtreme: offline tabletop RPG control center for worlds, maps, characters, sound, player screens, AI prompts, JSON-RPC control, and import/exportable campaign bundles | Python, PySide6, JSON-RPC, static PWA companion | `RPX Pro`, `RolePlay Xtreme`, `tabletop RPG control center`, `game-master tools`, `rpx-campaign-bundle-v1`, `offline RPG PWA`, `JSON-RPC LLM control` | Public repo; last public push **2026-07-25** |
| [.github](https://github.com/entertain-and-more/.github) | Organization profile, shared issue templates, PR template, llms.txt, and community defaults | GitHub profile repo | `entertain-and-more`, `organization profile`, `llms.txt`, `public repo directory` | Public profile repo; checked **2026-07-26** |

## Ecosystem Network

`entertain-and-more` operates as the dedicated gaming and entertainment branch within a larger open-source software and research network:

| Organization | Domain Focus | Key Repositories / Role |
|---|---|---|
| [open-bricks](https://github.com/open-bricks) | Umbrella / Dach-Organisation | Central catalog, open-source software umbrella |
| [ellmos-ai](https://github.com/ellmos-ai) | AI Agent Infrastructure | `bach`, `rinnsal`, `MarbleRun`, `skills`, `n8n-workflow-manager` |
| [file-bricks](https://github.com/file-bricks) | Desktop Data Tools | `ProFiler`, `ExplorerPro`, `ProSync`, `AmpelClip`, `ProfiPrompt` |
| [doc-bricks](https://github.com/doc-bricks) | Document & Media Systems | `DokuReader`, `MediaBrain`, `UniversalInvoiceMail` |
| [dev-bricks](https://github.com/dev-bricks) | Developer & Code Tools | `DevCenter`, `ApiProber`, `lock-master`, `pythonbox` |
| [research-line](https://github.com/research-line) | Open Science & Math Physics | `crm-cosmology`, `fst-nash`, `epstein-network`, `multiaxial-diagnostic-system` |
| [biotec-line](https://github.com/biotec-line) | Bioinformatics | `VFDistiller`, `genotype-to-vcf` |
| [assistassets-ai](https://github.com/assistassets-ai) | Local Financial Analytics | `FinancialProof` |
| [entertain-and-more](https://github.com/entertain-and-more) | Games & TTRPG Tools | `ChatAndChess`, `rpx`, `.github` |
| [lukisch](https://github.com/lukisch) | Personal GitHub Profile | Developer portal & flagship showcases |

## Discovery Notes & SEO Optimization

- [ChatAndChess](https://github.com/entertain-and-more/ChatAndChess) is the chess project: use `ChatAndChess`, `terminal chess`, `Python Minimax chess`, `Claude API chess`, `Claude Code worker chess`, `UCI chess moves`, and `chess tactics analyzer`.
- [rpx](https://github.com/entertain-and-more/rpx) is the RPG project: use `RPX Pro`, `RolePlay Xtreme`, `offline tabletop RPG control center`, `game-master dashboard`, `JSON-RPC LLM control`, `import campaign bundle`, and `rpx campaign bundle PWA companion`.
- The name `rpx` also appears in unrelated reverse-proxy tooling. In this organization, `rpx` means **RolePlay Xtreme**, a tabletop RPG and game-master application.
- Searches for `entertain-and-more` should resolve to this organization profile, then route users to the specific chess or RPG project rather than treating the org as a single monolithic game.

## Project Families

### Board games and AI-assisted play

[ChatAndChess](https://github.com/entertain-and-more/ChatAndChess) explores a compact terminal chess interface with chat-driven interaction patterns. It is useful as a small Python game codebase, a rules-and-engine testbed, and a testbed for AI-assisted play modes, including Claude API play and file-based Claude Code worker runs.

### Tabletop and game-master tooling

[rpx](https://github.com/entertain-and-more/rpx) is a local-first control center for pen-and-paper role-playing sessions. It centers the human game master and supports practical session work such as maps, ambience, notes, character state, missions, a second-screen player view, JSON-RPC control for LLM workflows, import/exportable `rpx-campaign-bundle-v1` ZIP files, and an offline PWA companion for campaign bundles.

## Design Principles

- **Player first:** AI features should support human play, not replace player agency.
- **Local-first:** Tools should remain useful without hosted platforms or mandatory cloud accounts.
- **Readable codebases:** Small entertainment projects should be easy to inspect, fork, test, and adapt.
- **Session utility:** Features are prioritized when they help an actual game table, playtest, or solo experiment.
- **Ecosystem links:** Game tools should connect cleanly to the broader [ellmos-ai](https://github.com/ellmos-ai), [open-bricks](https://github.com/open-bricks), and local-first desktop-tool ecosystem.

## For Developers and LLMs

- Machine-readable organization context: [llms.txt](https://github.com/entertain-and-more/.github/blob/main/llms.txt)
- Main organization page: [github.com/entertain-and-more](https://github.com/entertain-and-more)
- Related AI infrastructure: [ellmos-ai](https://github.com/ellmos-ai)
- Broader software suite: [open-bricks](https://github.com/open-bricks)

Search phrases that should lead here: `ChatAndChess terminal chess`, `Python Minimax chess tactics analyzer`, `Claude Code chess worker`, `UCI chess moves Python`, `engine hint chess terminal`, `RPX Pro tabletop RPG control center`, `RolePlay Xtreme game master tools`, `offline RPG campaign bundle`, `rpx-campaign-bundle-v1`, `JSON-RPC LLM control for RPG sessions`, `entertain-and-more ChatAndChess`, `entertain-and-more rpx`.
