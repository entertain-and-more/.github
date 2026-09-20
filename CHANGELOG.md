# Changelog — entertain-and-more/.github

All notable changes to the `entertain-and-more/.github` organization profile repository will be documented in this file.

## [2026-09-20]

### Added & Updated
- **Org Profile Health & Startseiten-Audit (Routine: GITHUBBOT_ORGA_README_MD_STARTSEITE_HEALTH):** Vollständige Revalidierung des gesamten Organisationsprofils gegen die Live-GitHub-API.
- **Öffentliches vs. Privates Inventar (Zero-Leak Defense):** Bestätigung von exakt 4 öffentlichen Repositories (`ChatAndChess`, `rpx`, `KlangpultLight`, `.github`). Alle 16 internen Repositories verbleiben strikt ungenannt und werden im öffentlichen Profil nicht beworben.
- **Live-Aktivitäts-Snapshot 2026-09-20:** Aktualisierung der Push-Aktivitätsdaten in `profile/README.md`, `profile/README_de.md`, `README.md` und `llms.txt`:
  - `rpx`: Letzter Push am `2026-09-20` (PushedAt `2026-09-20T02:52:40Z`, Commit `00fa31b`: Bundle Export Crashfix & Cascade Cleanup)
  - `KlangpultLight`: Letzter Push am `2026-09-19` (PushedAt `2026-09-19T20:56:37Z`, Commit `12ab8d2`: `projects_api` Path Traversal & Payload Härtung)
  - `ChatAndChess`: Letzter Push am `2026-07-27`
  - `.github`: Stand und Prüfung aktualisiert auf `2026-09-20`
- **Discoverability & SEO-Topic Enrichment (20/20 Parität):** Alle 3 öffentlichen Software-Repositories via GitHub CLI auf das Maximum von 20 Topics optimiert:
  - `ChatAndChess`: Ergänzt um `uci-chess`, `local-first`, `zero-egress`, `tactics-analyzer` (20/20)
  - `rpx`: Ergänzt um `roleplay-xtreme`, `rpx-pro`, `local-first`, `zero-egress`, `soundboard` (20/20)
  - `KlangpultLight`: Ergänzt um `podcast-studio`, `episode-planner`, `ai-monitor`, `multitrack-recording`, `zero-egress`, `offline-first` (20/20)
- **Badges & Härtung:** Shields.io Badges für `Verified-2026--09--20-blue` (EN) und `Geprüft-2026--09--20-blue` (DE) synchronisiert.
- **Automatisierte Vertragstestsuite (`tests/test_profile_parity.py`):** Test-Denylist auf alle 16 identifizierten internen Repositories erweitert; Zeitstempel- und Aktivitäts-Assertions auf den Prüfstand `2026-09-20` aktualisiert (9/9 Pytest Tests bestanden).
- **Privacy Regression Test (`tests/profile_privacy.ps1`):** Erfolgreich validiert (0 Leaks über alle 7 Profildateien).

## [2026-09-12]

### Added & Updated
- **Org Profile Health & Startseiten-Audit (Routine: GITHUBBOT_ORGA_README_MD_STARTSEITE_HEALTH):** Revalidierung des gesamten Organisationsprofils gegen die Live-GitHub-API.
- **Live-Aktivitäts-Snapshot 2026-09-12:** Aktualisierung der Push-Aktivitätsdaten in `profile/README.md`, `profile/README_de.md`, `README.md` und `llms.txt` (`rpx`: 2026-09-11, `KlangpultLight`: 2026-09-11, `ChatAndChess`: 2026-07-27, `.github`: 2026-09-12).
- **Discoverability & Topics:** Ergänzung der Homepage `https://github.com/entertain-and-more/KlangpultLight#readme` und Erweiterung der GitHub Topics (`pyside6`, `audio-recorder`, `teleprompter`, `live-transcription`) für `KlangpultLight`.
- **Badges & Härtung:** Neue Shields.io Badges für `Security_SLA-48h_Response` und Verifikation `2026-09-12` in EN und DE.
- **Ökosystem-Netzwerk:** Erweiterung der Schwester-Organisationstabelle um `um-bruch` auf 11 Einheiten.
- **Sicherheitsrichtlinie (`SECURITY.md`):** Modernisierung auf das standardisierte zweisprachige Format mit 48h Response SLA, 5 Werktage Triage, offiziellen Maintainer-Kontakten und Sicherheitsinvarianten (Zero-Egress, Non-Elevation, Data Integrity).
- **Automatisierte Vertragstestsuite (`tests/test_profile_parity.py`):** Implementierung einer 9-Punkte Pytest Contract-Suite zur Sicherung von Fence-Balance, Inventar-Vollständigkeit, Leak-Freiheit privater Repositories, Zeitstempeln und Mermaid-Syntax.
- **Repository-Härtung:** `.gitignore` für Multi-Host-Konfliktschutz, Lock-Marker und Pytest-Caches angelegt.

## [2026-09-11]

### Updated & Enhanced
- **Org Profile Freshness & Health Audit:** Revalidated full repository inventory via GitHub API against public-only policy. Confirmed 4 public repositories (`ChatAndChess`, `rpx`, `KlangpultLight`, `.github`) and verified 13 private repositories remain strictly unadvertised.
- **KlangpultLight Activity Sync:** Updated latest public push timestamp to `2026-09-10` following its latest multi-OS CI hardening and hygiene release (`cfce2b5`).
- **Showcase Expansion:** Added `ChatAndChess` gameplay screenshot banner with direct navigation link to the showcase carousel in both English and German profile pages (now featuring 3 visual product cards).
- **Mermaid Syntax Hardening:** Quoted edge labels with special characters (`&`) in system architecture diagrams to satisfy `HOOK-BANNER-ASSET-01` and guarantee clean rendering across all markdown viewers.
- **Context & Health Files Sync:** Refreshed `llms.txt`, root `README.md`, `BEFUNDE.md`, `profile/README.md`, and `profile/README_de.md` to `2026-09-11`.
- **Privacy & Safety Verification:** Passed automated privacy test `tests/profile_privacy.ps1` with 0 leaks across all 7 indexed files.

## [2026-08-24]

### Updated
- **Org Profile Freshness Audit:** Revalidated the public-only repository index against live GitHub metadata. The public profile still contains `ChatAndChess`, `rpx`, `KlangpultLight`, and `.github`; no public repository is missing.
- **KlangpultLight Discovery Sync:** Updated the latest public activity timestamp to `2026-08-24` and expanded podcast-production discovery terms for live transcription, teleprompter, USB podcast studio workflows, and local audio/video recording.
- **Machine Context Sync:** Refreshed `llms.txt`, root `README.md`, and both profile READMEs to the 2026-08-24 check date while preserving the public-only privacy boundary.

## [2026-08-14]

### Added & Updated
- **Privacy correction:** Removed private repository names from the current public profile, machine context, findings, and historical summary text; sister-organization tables now list public repositories only. Added an identifier-free privacy regression check with public URL allowlists and optional external denylist input.
- **Discoverability & Profile Parity Audit (Path B):** Verified live GitHub API inventory for all public repositories in `entertain-and-more` (`ChatAndChess`, `rpx`, `KlangpultLight`, `.github`).
- **Full Parity German Profile (`profile/README_de.md`):** Expanded `profile/README_de.md` to 100% structural parity with `profile/README.md`, including complete Shields.io badge bar, bilingual language switcher (`[🇩🇪 Deutsch](README_de.md) | [🇬🇧 English Version](README.md)`), showcase section with linked banners, updated Mermaid system architecture flow, complete public repository directory, ecosystem sister network table, project families descriptions, and German SEO discovery search terms.
- **Profile Enhancements (`profile/README.md`):** Updated hero badge bar with language switcher link, updated live push timestamps (`2026-08-14` for `rpx` and `KlangpultLight`), harmonized banner presentation, and synchronized audit date to `2026-08-14`.
- **Machine Context Sync (`llms.txt`):** Updated `Last-checked: 2026-08-14`, synchronized public push timestamps, cleaned search phrase indentation, and validated sister org cross-links.
- **Root README Sync (`README.md`):** Synchronized public repository index table, push timestamps, and files structure table referencing bilingual profile documents.

## [2026-08-01]

### Added & Updated
- **Public repository directory:** Added the newly public `KlangpultLight` repository to `README.md`, `profile/README.md`, `profile/README_de.md`, and `llms.txt`.
- **Bilingual profile:** Added the German organization start page and synchronized the public count to 4 repositories (3 applications plus profile infrastructure).
- **Verification:** Live GitHub API inventory, `git diff --check`, UTF-8/Umlaut scan, and public-index parity check completed.

## [2026-07-29]

### Corrected
- **Public-only inventory:** Revalidated repository visibility through the authenticated GitHub API. The public organization contains `ChatAndChess`, `rpx`, and `.github`; private repositories are no longer advertised in `README.md`, `profile/README.md`, or `llms.txt`.
- **Private product boundary:** The private commercial edition remains intentionally absent from the public organization profile.
- **Count correction:** Replaced the incorrect `6 repositories` claim with the current public count of 3 (2 applications plus the profile repository).

## [2026-07-28]

### Added & Updated
- **Public Repo Directory Audit:** Resolved `llms.txt` merge conflicts and updated `Last-checked` timestamps to `2026-07-28` across `profile/README.md`, `README.md`, and `llms.txt`.
- **Shared Community Health & Issue Templates Audit:** Created organization-wide default templates under `.github/ISSUE_TEMPLATE/` (`bug_report.md`, `feature_request.md`) and `.github/PULL_REQUEST_TEMPLATE.md` for seamless GitHub org-wide default template discovery.

## [2026-07-27]

### Added & Updated
- **Comprehensive Public Repository Audit:** Verified 100% live GitHub API metadata across all 6 public repositories in `entertain-and-more`.
- **Repo Directory Expansion:** Integrated the then-public repository entries into `profile/README.md`, `README.md`, and `llms.txt`; later audits reduced the index to currently public repositories only.
- **Profile Enhancements (`profile/README.md`):**
  - Updated hero badges (`Flask`, `Dart`, `Freeware`).
  - Added new Start Here entry points for audio podcasting, media availability tracking, and live audio/video recording.
  - Expanded Mermaid architecture flowchart to detail Media Production & Streaming sub-suite alongside Gaming & RPG workflows.
  - Added structured project family sections for local audio studio tools and streaming content discovery.
  - Expanded SEO keywords and discovery terms for internal & external search optimization.
- **Machine Context Sync (`llms.txt`):** Updated `Last-checked: 2026-07-27`, updated public repo count to 6 (5 apps + 1 profile repo), and added structured entries & search phrases for all 5 apps.
- **Root README Sync (`README.md`):** Synchronized audit timestamps and full repository table.

## [2026-07-26]

### Updated & Enhanced
- **Audit & Selection:** `entertain-and-more/.github` identified as the furthest back in time checked organization profile (`2026-07-21T22:07:58Z`).
- **Live Metadata Sync:** Verified live GitHub API metadata for all 3 public repositories (`ChatAndChess`, `rpx`, `.github`). Updated push timestamps to `2026-07-25` for `ChatAndChess` and `rpx`.
- **Profile Enhancements (`profile/README.md`):**
  - Integrated visual Shields.io Badges (`GitHub Org Profile`, `Ecosystem ellmos-ai`, `Umbrella open-bricks`, `LLM-Context llms.txt`, `Architecture Local-First`, `Stack Python / PySide6 / Minimax`, `License MIT`).
  - Added GFM Callouts (`> [!NOTE]`, `> [!TIP]`) emphasizing local-first offline play resilience and optional AI capabilities.
  - Added Ecosystem Network matrix referencing all 10 sister organizations.
  - Enhanced Mermaid system architecture and interaction flow diagram.
  - Updated Public Repository Directory table with live timestamps and discovery terms.
- **Machine Context Sync (`llms.txt`):** Updated `Last-checked: 2026-07-26` and expanded sister org references.
- **Root README Sync (`README.md`):** Synchronized audit timestamps, public repository index, and directory structure listing.
