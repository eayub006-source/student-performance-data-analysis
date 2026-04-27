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
    print("Columns:", list(df.columns), end="\n\n")
    df.info()
    print()
    print("Average age:", df["age"].mean())
    print()
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

    avg_age_by_sex = df.groupby("sex")["age"].mean()
    fig2, ax2 = plt.subplots(figsize=(6, 4))
    avg_age_by_sex.plot(kind="bar", ax=ax2, color=["steelblue", "coral"], edgecolor="white")
    ax2.set_title("Average Age by Gender")
    ax2.set_xlabel("Gender")
    ax2.set_ylabel("Average Age")
    fig2.tight_layout()
    out_path2 = OUTPUT_DIR / "avg_age_by_sex.png"
    fig2.savefig(out_path2, dpi=120)
    plt.close(fig2)
    print(f"Saved {out_path2}")

    g3_by_sex = df.groupby("sex")["G3"].mean()
    print("\nAverage final grade by gender:")
    print(g3_by_sex.to_string(), end="\n\n")

    fig3, ax3 = plt.subplots(figsize=(6, 4))
    g3_by_sex.plot(kind="bar", ax=ax3, color=["steelblue", "coral"], edgecolor="white")
    ax3.set_title("Average final grade (G3) by gender")
    ax3.set_xlabel("Gender")
    ax3.set_ylabel("Mean G3")
    fig3.tight_layout()
    out_path3 = OUTPUT_DIR / "g3_by_sex.png"
    fig3.savefig(out_path3, dpi=120)
    plt.close(fig3)
    print(f"Saved {out_path3}")


if __name__ == "__main__":
    main()
