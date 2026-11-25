"""The Worst App Idea Ever Pitched — entry generator (stdlib only).

Writes exactly one sentence (<=240 chars) pitching the worst, most
useless app imaginable to <output_dir>/entry.txt.
"""
import os

SENTENCE = (
    "PlantPitch is a $29/month app that translates your fern's silence "
    "into investor-ready pitch decks, so founders can raise a seed round "
    "on feedback from a plant that has never once had an opinion."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SENTENCE + "\n")
    print(f"Wrote {len(SENTENCE)} chars to {path}")


if __name__ == "__main__":
    main()
