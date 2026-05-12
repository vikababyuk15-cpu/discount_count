# 📊 Game Matching Script
📌 Overview

This script compares data from two Excel files:

source.xlsx — main data source
needed.xlsx — list of games to search for

It performs:

text normalization (cleaning)
partial matching by game name
provider-based disambiguation
generation of final output file result.xlsx
⚙️ How it works
1. Data Cleaning

All text is normalized to ensure consistent matching:

converted to lowercase
special characters are removed
extra spaces are cleaned
2. Matching Logic
First, it searches for partial matches by Game
If multiple matches are found → it refines by Provider
If still ambiguous → all matches are returned
3. Output

The final file:

result.xlsx

Contains:

matched records
cleaned structure
no duplicates
no helper columns
📂 Input Files
source.xlsx

Must contain:

Game
Provider
needed.xlsx

Must contain:

Game
Provider
📤 Output

result.xlsx includes:

matched rows from source
deduplicated results
cleaned dataset (no helper columns)
🚀 How to Run

Install dependencies:

pip install pandas openpyxl

Run the script:

python script.py
🧠 Key Features
partial string matching using str.contains()
robust text normalization
fallback logic for ambiguous matches
provider-level disambiguation
duplicate cleanup
🎯 Notes

This script is useful when:

game names are inconsistent or formatted differently
providers help resolve duplicates
datasets require fuzzy-like matching without external ML libraries
