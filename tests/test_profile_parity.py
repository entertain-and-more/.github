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
    name.strip()
    for name in os.environ.get("PROFILE_PRIVATE_REPO_DENYLIST", "").split(";")
    if name.strip()
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


def _assert_public_profile(content):
    public_names = {name.lower() for name in PUBLIC_REPOS}
    pattern = (
        r"https://(?:github\.com/|raw\.githubusercontent\.com/|api\.github\.com/repos/)"
        r"entertain-and-more/([A-Za-z0-9_.-]+)"
    )
    for name in re.findall(pattern, content, flags=re.IGNORECASE):
        if name.lower() not in public_names:
            raise AssertionError("Non-public repository reference")
    for private_name in PRIVATE_REPOS:
        pattern = rf"(?<![A-Za-z0-9_-]){re.escape(private_name)}(?![A-Za-z0-9_-])"
        if re.search(pattern, content, flags=re.IGNORECASE):
            raise AssertionError("Non-public repository reference")


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
        _assert_public_profile(content)


def test_check_timestamp_parity():
    """Verify verification date 2026-10-03 across profile files."""
    expected_iso = "2026-10-03"

    en_content = get_file_content("profile/README.md")
    assert expected_iso in en_content

    de_content = get_file_content("profile/README_de.md")
    assert expected_iso in de_content

    root_content = get_file_content("README.md")
    assert expected_iso in root_content

    llms_content = get_file_content("llms.txt")
    assert expected_iso in llms_content


@pytest.mark.parametrize("reference", [
    "synthetic-denied-repo",
    "https://github.com/entertain-and-more/synthetic-unlisted-repo",
    "https://raw.githubusercontent.com/entertain-and-more/synthetic-unlisted-repo/main/x",
    "https://api.github.com/repos/entertain-and-more/synthetic-unlisted-repo",
])
def test_private_guard_rejects_without_disclosing_identifier(monkeypatch, reference):
    monkeypatch.setitem(globals(), "PRIVATE_REPOS", ["synthetic-denied-repo"])
    monkeypatch.setitem(globals(), "get_file_content", lambda _path: reference)
    with pytest.raises(AssertionError) as failure:
        test_private_repo_leak_guard()
    assert str(failure.value) == "Non-public repository reference"


def test_activity_snapshot_integrity():
    """Verify recent push activity entries in profile READMEs."""
    en_content = get_file_content("profile/README.md")
    de_content = get_file_content("profile/README_de.md")

    for repo in ["ChatAndChess", "rpx", "KlangpultLight", ".github"]:
        assert repo in en_content
        assert repo in de_content

    for date in ["2026-10-03", "2026-10-02", "2026-09-22"]:
        assert date in en_content
        assert date in de_content


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


def test_verification_badges():
    """Verify date-stamped verification badges in profile READMEs."""
    en_content = get_file_content("profile/README.md")
    de_content = get_file_content("profile/README_de.md")
    assert "Verified-2026--10--03-blue" in en_content
    assert "Geprüft-2026--10--03-blue" in de_content


def test_ecosystem_zero_leak_hardening():
    """Verify private repos from other orgs are not mentioned in ecosystem tables."""
    target_files = [
        "profile/README.md",
        "profile/README_de.md",
        "README.md",
        "llms.txt",
    ]
    for rel_path in target_files:
        content = get_file_content(rel_path)
        _assert_public_profile(content)
