import json
import pathlib
import sys

root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")
records = {}
for path in sorted(root.glob("log/*/*.jsonl")):
    for line in path.read_text(encoding="utf-8").splitlines():
        event = json.loads(line)
        if event.get("record"):
            records.setdefault(event["record"], []).append(event["kind"])
for record, kinds in sorted(records.items()):
    print(record, " ".join(kinds))
