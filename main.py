#!/usr/bin/env python3
"""Publish the finished front page for the make.fun grader.

The artwork itself is baked into entry.png next to this file; all this
program does is place an exact copy of it where the harness expects it.
No pixels are touched here, so the output is byte-identical every run.
"""

from __future__ import annotations

import hashlib
import os
import sys
from pathlib import Path


def locate_source() -> Path:
    """Return the path of the artwork sitting beside this script."""
    return Path(__file__).resolve().with_name("entry.png")


def resolve_destination() -> Path:
    """Return the folder the grader points at, or /output by default."""
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(chosen)


def duplicate_artwork(source: Path, folder: Path) -> Path:
    """Copy the artwork byte for byte into the destination folder."""
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / source.name
    # Read and write in chunks so memory stays flat even for big images.
    with source.open("rb") as reader, target.open("wb") as writer:
        while True:
            block = reader.read(1024 * 1024)
            if not block:
                break
            writer.write(block)
    return target


def fingerprint(path: Path) -> str:
    """Return the SHA-256 hex digest of a file's contents."""
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> int:
    source = locate_source()
    if not source.is_file():
        print(f"missing artwork: {source}", file=sys.stderr)
        return 1

    destination = duplicate_artwork(source, resolve_destination())

    if fingerprint(source) != fingerprint(destination):
        print("copy mismatch: output differs from source", file=sys.stderr)
        return 1

    print(f"front page written to {destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
