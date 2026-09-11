#!/usr/bin/env python3
"""Validate the recommended processed dataset."""
from pathlib import Path
import csv
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "data" / "processed" / "food_triples.csv"
ALLOWED = {"名称", "外形", "口感", "味道"}

with PATH.open("r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    assert reader.fieldnames == ["subject", "relation", "object"], reader.fieldnames
    rows = list(reader)

assert rows, "Dataset is empty"
assert all(r["subject"] and r["relation"] and r["object"] for r in rows), "Blank field found"
assert all(r["relation"] in ALLOWED for r in rows), "Unexpected relation found"
triples = [(r["subject"], r["relation"], r["object"]) for r in rows]
assert len(triples) == len(set(triples)), "Exact duplicate triple found in recommended file"

counts = Counter(r["relation"] for r in rows)
print(f"OK: {len(rows)} unique complete triples")
print("Relations:", dict(counts))
