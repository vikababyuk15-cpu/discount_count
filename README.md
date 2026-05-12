# 📊 Game Matching Script

## 📌 Overview
This script compares data from two Excel files:
* **source.xlsx** — main data source
* **needed.xlsx** — list of games to search for

## ⚙️ How it works
1. **Data Cleaning**
   All text is normalized: lowercase, special characters removed, extra spaces cleaned.
2. **Matching Logic**
   Search by partial game name. If multiple matches → filter by provider.
3. **Output**
   Generates `result.xlsx`.

## 📂 Project Structure
* 📥 **Input Files:** `source.xlsx`, `needed.xlsx`
* 📤 **Output:** Matched rows, no duplicates, clean structure.

## 🚀 Quick Start
Run: `pip install pandas openpyxl`  
Then: `python script.py`
