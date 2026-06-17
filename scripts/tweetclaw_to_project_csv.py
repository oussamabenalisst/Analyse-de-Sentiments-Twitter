from __future__ import annotations

import argparse
import csv
import json
from collections.abc import Iterable
from pathlib import Path
from typing import Any


TEXT_FIELDS = ("tweet_text", "text", "full_text", "content", "body", "tweet")
RETWEET_FIELDS = ("retweet_count", "retweets", "repost_count")
REPLY_FIELDS = ("reply_count", "replies")
CONTAINER_FIELDS = ("tweets", "data", "results", "items")


def main() -> None:
    args = parse_args()
    rows = [normalize_record(record) for record in load_records(args.input)]
    rows = [row for row in rows if row["tweet_text"]]

    with args.output.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["tweet_text", "retweet_count", "reply_count"],
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} rows to {args.output}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert a TweetClaw export into project_twitter_data.csv format."
    )
    parser.add_argument("input", type=Path, help="TweetClaw CSV, JSON, or JSONL export.")
    parser.add_argument("output", type=Path, help="Destination CSV file.")
    return parser.parse_args()


def load_records(path: Path) -> list[dict[str, Any]]:
    suffix = path.suffix.lower()

    if suffix == ".csv":
        with path.open(newline="", encoding="utf-8") as file:
            return [dict(row) for row in csv.DictReader(file)]

    if suffix == ".jsonl":
        records = []
        with path.open(encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line:
                    records.append(json.loads(line))
        return records

    if suffix == ".json":
        with path.open(encoding="utf-8") as file:
            payload = json.load(file)
        return unwrap_json_records(payload)

    raise ValueError("Input must be a CSV, JSON, or JSONL file.")


def unwrap_json_records(payload: Any) -> list[dict[str, Any]]:
    if isinstance(payload, list):
        return [record for record in payload if isinstance(record, dict)]

    if isinstance(payload, dict):
        for field in CONTAINER_FIELDS:
            records = payload.get(field)
            if isinstance(records, list):
                return [record for record in records if isinstance(record, dict)]
        return [payload]

    return []


def normalize_record(record: dict[str, Any]) -> dict[str, int | str]:
    return {
        "tweet_text": first_text(record, TEXT_FIELDS),
        "retweet_count": first_int(record, RETWEET_FIELDS, nested_field="public_metrics"),
        "reply_count": first_int(record, REPLY_FIELDS, nested_field="public_metrics"),
    }


def first_text(record: dict[str, Any], fields: Iterable[str]) -> str:
    for field in fields:
        value = record.get(field)
        if value is not None:
            text = str(value).strip()
            if text:
                return text
    return ""


def first_int(
    record: dict[str, Any],
    fields: Iterable[str],
    *,
    nested_field: str,
) -> int:
    for field in fields:
        value = record.get(field)
        parsed = parse_int(value)
        if parsed is not None:
            return parsed

    nested = record.get(nested_field)
    if isinstance(nested, dict):
        for field in fields:
            parsed = parse_int(nested.get(field))
            if parsed is not None:
                return parsed

    return 0


def parse_int(value: Any) -> int | None:
    if value in (None, ""):
        return None

    try:
        return int(value)
    except (TypeError, ValueError):
        return None


if __name__ == "__main__":
    main()
