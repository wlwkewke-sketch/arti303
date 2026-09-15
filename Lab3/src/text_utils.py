"""Utilities for cleaning and formatting text."""

def clean_name(raw):
    """Remove surrounding/duplicate whitespace and convert to title case."""
    return " ".join(raw.split()).title()
