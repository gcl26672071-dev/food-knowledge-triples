#!/usr/bin/env python3
"""Rebuild processed dataset files from the preserved original CSV.
Uses only the Python standard library.
"""
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "data" / "raw" / "food_triples_original.csv"
OUT = ROOT / "data" / "processed"
REVIEW = ROOT / "data_review"
OUT.mkdir(parents=True, exist_ok=True)
REVIEW.mkdir(parents=True, exist_ok=True)

with SRC.open("r", encoding="utf-8-sig", newline="") as f:
    rows = list(csv.reader(f))[1:]

parsed = []
for row in rows:
    row = row + [""] * (4 - len(row))
    source_row, subject, relation, obj = [x.strip() for x in row[:4]]
    parsed.append((source_row, subject, relation, obj))

complete = [r for r in parsed if r[1] and r[2] and r[3]]
incomplete = [r for r in parsed if not (r[1] and r[2] and r[3])]

seen = set()
unique = []
for _, subject, relation, obj in complete:
    triple = (subject, relation, obj)
    if triple not in seen:
        seen.add(triple)
        unique.append(triple)

def write_csv(path, header, rows):
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(header)
        w.writerows(rows)

write_csv(OUT / "food_triples.csv", ["subject", "relation", "object"], unique)
write_csv(OUT / "food_triples_all_complete.csv", ["subject", "relation", "object"],
          [(s, r, o) for _, s, r, o in complete])
write_csv(REVIEW / "incomplete_rows.csv", ["source_row", "subject", "relation", "object"], incomplete)
write_csv(REVIEW / "unassigned_values.csv", ["source_row", "value"],
          [(i, o) for i, s, r, o in incomplete if not s and not r and o])
write_csv(REVIEW / "missing_object_rows.csv", ["source_row", "subject", "relation", "object"],
          [x for x in incomplete if x[1] and x[2] and not x[3]])
write_csv(REVIEW / "blank_rows.csv", ["source_row", "subject", "relation", "object"],
          [x for x in incomplete if not x[1] and not x[2] and not x[3]])

print(f"Complete rows: {len(complete)}")
print(f"Unique triples: {len(unique)}")
print(f"Incomplete rows: {len(incomplete)}")
