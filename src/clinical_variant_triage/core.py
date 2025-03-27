"""Core workflow for Clinical Variant Triage by Red@."""

PROJECT_NAME = "Clinical Variant Triage"
DOMAIN_THEME = "bioinformatics"


def build_snapshot() -> dict[str, str]:
    return {"project": PROJECT_NAME, "author": "Red@", "theme": DOMAIN_THEME}
