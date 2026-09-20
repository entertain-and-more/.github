# -*- coding: utf-8 -*-
"""Contract tests for entertain-and-more organization profile parity and integrity."""

import os
import re
import pytest

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

PUBLIC_REPOS = [
    ".github",
    "ChatAndChess",
    "rpx",
    "KlangpultLight",
]

SISTER_ORGS = [
    "open-bricks",
    "ellmos-ai",
    "file-bricks",
    "doc-bricks",
    "dev-bricks",
    "research-line",
    "biotec-line",
    "assistassets-ai",
    "entertain-and-more",
    "um-bruch",
    "lukisch",
]

PRIVATE_REPOS = [
    "ChainReaction",
    "StreetRacer",
    "CultureEvolution",
    "RescueMe",
    "HauntedHouse",
    "BattleStage",
    "StreamingGuide",
    "BattleChess3D",
    "RealmWars",
    "CuteStrike",
    "MafiaCastle",
    "GhostTrain",
    "TreasureIsland",
    "DungeonMaster",
    "EscapeRoomBuilder",
]


def get_file_content(relative_path: str) -> str:
    path = os.path.join(REPO_ROOT, relative_path)
    assert os.path.exists(path), f"File not found: {path}"
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def test_markdown_fence_balance():
    """Verify all markdown files have balanced code fences."""
    md_files = [
        "README.md",
        "profile/README.md",
        "profile/README_de.md",
        "CHANGELOG.md",
        "CONTRIBUTING.md",
        "SECURITY.md",
        "BEFUNDE.md",
    ]
    for rel_path in md_files:
        content = get_file_content(rel_path)
        fence_count = len(re.findall(r"^```", content, flags=re.MULTILINE))
        assert fence_count % 2 == 0, f"Unbalanced code fences in {rel_path} (found {fence_count})"


def test_public_repo_inventory():
    """Verify all 4 public repos are cataloged in core profile documents."""
    target_files = [
        "profile/README.md",
        "profile/README_de.md",
        "README.md",
        "llms.txt",
    ]
    for rel_path in target_files:
        content = get_file_content(rel_path)
        for repo in PUBLIC_REPOS:
            assert repo in content, f'Public repo "{repo}" missing from {rel_path}'


def test_private_repo_leak_guard():
    """Verify 0 private/internal repos are leaked into public profile documents."""
    target_files = [
        "profile/README.md",
        "profile/README_de.md",
        "README.md",
        "llms.txt",
        "SECURITY.md",
        "CONTRIBUTING.md",
    ]
    for rel_path in target_files:
        content = get_file_content(rel_path)
        for priv in PRIVATE_REPOS:
            assert priv not in content, f'Leak violation: private repo "{priv}" found in {rel_path}'

        # Ensure standalone private Klangpult (not KlangpultLight) is not referenced
        klangpult_matches = re.findall(r"\bKlangpult\b(?!Light)", content)
        assert len(klangpult_matches) == 0, f'Leak violation: standalone private "Klangpult" found in {rel_path}'


def test_check_timestamp_parity():
    """Verify verification date 2026-09-20 across profile files."""
    expected_iso = "2026-09-20"

    en_content = get_file_content("profile/README.md")
    assert expected_iso in en_content

    de_content = get_file_content("profile/README_de.md")
    assert expected_iso in de_content

    root_content = get_file_content("README.md")
    assert expected_iso in root_content

    llms_content = get_file_content("llms.txt")
    assert expected_iso in llms_content


def test_activity_snapshot_integrity():
    """Verify recent push activity entries in profile READMEs."""
    en_content = get_file_content("profile/README.md")
    de_content = get_file_content("profile/README_de.md")

    for repo in ["ChatAndChess", "rpx", "KlangpultLight", ".github"]:
        assert repo in en_content
        assert repo in de_content

    assert "2026-09-20" in en_content
    assert "2026-09-20" in de_content
    assert "2026-09-19" in en_content
    assert "2026-09-19" in de_content
    assert "2026-07-27" in en_content
    assert "2026-07-27" in de_content


def test_ecosystem_cross_linking():
    """Verify sister organization references are complete across profile docs."""
    target_files = ["profile/README.md", "profile/README_de.md", "llms.txt"]
    for rel_path in target_files:
        content = get_file_content(rel_path)
        for org in SISTER_ORGS:
            assert org in content, f'Sister org "{org}" missing from {rel_path}'


def test_mermaid_diagram_syntax():
    """Verify Mermaid flowchart blocks exist and have matching subgraph boundaries."""
    for rel_path in ["profile/README.md", "profile/README_de.md"]:
        content = get_file_content(rel_path)
        assert "```mermaid" in content
        assert "graph TD" in content or "flowchart TD" in content
        subgraph_opens = len(re.findall(r"\bsubgraph\b", content))
        subgraph_ends = len(re.findall(r"\bend\b", content))
        assert subgraph_opens > 0
        assert subgraph_opens == subgraph_ends, f"Mismatched subgraph blocks in {rel_path}"


def test_utf8_encoding_and_umlauts():
    """Verify clean UTF-8 encoding and genuine German umlauts."""
    de_content = get_file_content("profile/README_de.md")
    assert "\ufffd" not in de_content, "Unicode replacement character (mojibake) in profile/README_de.md"
    assert "Öffentliche" in de_content
    assert "Spiele" in de_content
    assert "Dachorganisation" in de_content


def test_security_policy_parity():
    """Verify 48h Response SLA and official contacts in SECURITY.md."""
    security_content = get_file_content("SECURITY.md")
    assert "48 hours" in security_content or "48h" in security_content
    assert "security@open-bricks.org" in security_content
    assert "security@ellmos.ai" in security_content
    assert "Zero-Egress" in security_content
