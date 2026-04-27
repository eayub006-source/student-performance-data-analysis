"""Student performance dataset: load, summarize, and plot final grades."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "student_data.csv"
OUTPUT_DIR = ROOT / "output"


def main() -> None:
    """Load CSV, print summary stats, and save a histogram of G3."""
    df = pd.read_csv(DATA_PATH)
    OUTPUT_DIR.mkdir(exist_ok=True)

    print(f"Loaded {len(df)} rows, {df.shape[1]} columns from {DATA_PATH.name}")
    print(df.head(), end="\n\n")
    print("G3 (final grade):")
    print(df["G3"].describe().to_string(), end="\n\n")

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.hist(df["G3"], bins=range(0, 22), edgecolor="white", color="steelblue", align="left")
    ax.set_xlabel("Final grade (G3)")
    ax.set_ylabel("Count")
    ax.set_title("Distribution of final grades")
    ax.set_xlim(-0.5, 20.5)
    fig.tight_layout()
    out_path = OUTPUT_DIR / "g3_distribution.png"
    fig.savefig(out_path, dpi=120)
    plt.close(fig)
    print(f"Saved {out_path}")


if __name__ == "__main__":
    main()
