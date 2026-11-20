# Backlog vault

This repository holds the work records of one or more projects, written by the basicly tracker.

- `log/WRITER/NNNNN.jsonl`: each writer's events, one JSON object per line, never rewritten.
- `reader.py`: prints every record from these files with plain Python, no other tool needed.
- `FORMAT.md`: the line format.

To stop using it, remove `.basicly-tracker.toml` from each code repository,
then delete this repository.
