# Student performance — simple analysis

Small Python script using **pandas** and **matplotlib** (good for beginners).

## How to run

1. Install Python 3 (if you do not have it).
2. Open a terminal in this project folder and run:

```bash
pip install -r requirements.txt
python main.py
```

3. The `output/` folder is created automatically. You should get:

   - `output/g3_distribution.png` — histogram of final grades  
   - `output/avg_age_by_sex.png` — average age by gender  

## What it prints

- First 5 rows of the data  
- Average age  
- Average final grade (`G3`) by gender (`F` / `M`)  

## Data

Uses `student_data.csv` (student performance dataset, e.g. from Kaggle).
