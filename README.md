# Hospital Patient Data Analyzer

## Student Details

| Field | Details |
|-------|---------|
| Name | Jahnvi Sharma |
| ERP | RU-26-02208 |
| Section | B1 |
| University | Rungta International Skills University |
| School | School of Computer Science and Engineering |
| Programme | Bachelor of Technology - Computer Science and Engineering - Artificial Intelligence and Machine Learning in association with Microsoft |

## Project Allotted

| Field | Details |
|-------|---------|
| PS No. | 4 |
| Project Title | Hospital Patient Data Analyzer |
| Language | Python 3 |
| Concepts | Pandas, CSV, Data Cleaning, Grouping |

### Problem Statement

Analyse hospital patient data from a CSV file to clean the data and find insights such as department-wise patient load, average length of stay and age-group distribution.

**Note:** CSV columns: `Patient_ID, Age, Gender, Department, Admit_Date, Discharge_Date`. Use dummy data only.

### Bare Minimum Requirements

1. Write the solution in Python 3 (one `.py` file) and run it from the console.
2. Load the CSV file using Pandas.
3. Clean missing, duplicate and invalid values.
4. Use `groupby()` for department-wise and gender-wise analysis.
5. Calculate the length of stay and plot at least one Matplotlib chart.

### Instructions

1. Understand the problem statement and define the problem clearly.
2. Develop the solution using proper logic and programming concepts.
3. Implement all required features and pass the given test cases.
4. Test and debug the project to ensure correct output.
5. Prepare the documentation/report and upload the code and report to GitHub.
6. Complete and submit the project within the given deadline.

---

## About the Project

This is a console-based program that reads hospital patient records from a CSV file, cleans the data, and shows useful information through a simple menu. It uses only two libraries, `pandas` and `matplotlib`.

## Features

- Loads patient data from a CSV file using Pandas
- Removes duplicate patients
- Removes records with invalid dates, ages or discharge before admission
- Fills missing ages with the median age
- Department-wise patient count using `groupby()`
- Gender-wise patient count using `groupby()`
- Length of stay for each patient and the average stay
- Age-group distribution (0-40, 41-60, 61+)
- Bar charts using Matplotlib
- Menu-driven and easy to use

## Project Files

| File | Description |
|------|-------------|
| `hospital_analyzer.py` | Main Python program (single file) |
| `patients.csv` | Input data file (dummy data) |
| `README.md` | Project documentation |

## Requirements

- Python 3
- pandas
- matplotlib

Install the libraries if needed:

```
pip install pandas matplotlib
```

## How to Run

1. Place `hospital_analyzer.py` and `patients.csv` in the same folder.
2. Open a terminal in that folder.
3. Run:

```
python hospital_analyzer.py
```

4. Enter the CSV file name, or press Enter to use `patients.csv`.
5. Choose an option from the menu.

## Input File Format

The CSV file must have these columns:

```
Patient_ID,Age,Gender,Department,Admit_Date,Discharge_Date
P1,45,M,Cardiology,2026-08-01,2026-08-05
P2,30,F,Ortho,2026-08-02,2026-08-04
P3,60,M,Cardiology,2026-08-03,2026-08-08
```

Dates must be in `YYYY-MM-DD` format.

## Menu

```
===== Hospital Patient Data Analyzer =====
1. Department count
2. Length of stay
3. Stay and age groups
4. Gender count
5. Exit
```

| Option | What it does |
|--------|--------------|
| 1 | Shows the number of patients in each department and the total patients |
| 2 | Shows the stay of each patient, the average stay and a bar chart of average stay by department |
| 3 | Shows the average stay, the age-group counts and a bar chart of age groups |
| 4 | Shows the number of patients for each gender |
| 5 | Exits the program |

---

## Code Explanation

### Imports

```python
import pandas as pd
import matplotlib.pyplot as plt
```

- `pandas` is used to read the CSV file, clean the data and group it.
- `matplotlib.pyplot` is used to draw the bar charts.

### `load_data(file_name)`

Reads the CSV file into a Pandas DataFrame using `pd.read_csv()`. If the file does not exist, it prints "File not found" and returns `None` so the program stops safely instead of crashing.

### `clean_data(data)`

Cleans the raw data and adds the length of stay. It works on a copy so the original data is not changed. The steps are:

1. **Remove duplicates:** `drop_duplicates(subset="Patient_ID")` keeps the first record of each patient. It prints how many duplicates were removed.
2. **Fix the Age column:** `pd.to_numeric(..., errors="coerce")` converts ages to numbers. Wrong values become missing. Ages below 0 or above 120 are also treated as missing.
3. **Fix the date columns:** `pd.to_datetime(..., errors="coerce")` converts both dates. Records with an invalid date are dropped, and so are records where the discharge date is before the admit date.
4. **Fill missing text values:** a missing Department or Gender becomes `Unknown`.
5. **Fill missing ages:** missing ages are replaced with the median age. It prints the median used.
6. **Calculate length of stay:** a new column `Stay_Days` is created as `Discharge_Date - Admit_Date` in days. A same-day discharge gives 0 days.

It returns the cleaned DataFrame.

### `show_department_count(data)`

Uses `groupby("Department")` to count the patients in each department and prints them in one line, for example `Cardiology: 2 | Ortho: 1`. It then prints the total number of patients.

### `show_gender_count(data)`

Uses `groupby("Gender")` to count the patients of each gender and prints the result in one line.

### `plot_bar_chart(labels, values, title, x_label, y_label)`

A reusable helper that draws a bar chart with the given labels, values, title and axis names, then displays it with `plt.show()`. Both chart options use this function, so the plotting code is written only once.

### `show_length_of_stay(data)`

- Prints the stay of every patient in days.
- Prints the average stay with two decimal places.
- Uses `groupby("Department")` to find the average stay of each department and plots it as a bar chart.

### `get_age_groups(data)`

Puts each patient into an age group using `pd.cut()`: `0-40`, `41-60` and `61+`. It returns how many patients fall into each group.

### `show_stay_and_age_groups(data)`

- Prints the average stay in days.
- Prints the age-group counts, for example `Age groups: 0-40: 1 | 41-60: 2 | 61+: 0`.
- Plots the age groups as a bar chart and prints `Bar chart displayed`.

### `show_menu()`

Prints the menu options on the screen.

### `main()`

The starting point of the program:

1. Asks for the CSV file name (default `patients.csv`).
2. Loads the file and stops if it is missing.
3. Cleans the data and stops if no valid records remain.
4. Shows the menu in a loop and calls the matching function for the user's choice.
5. Prints "Invalid choice" for a wrong entry, and exits on option 5.

---

## Test Cases

### Test Case 1: Normal Input

**Input** (`patients.csv`):

```
Patient_ID,Age,Gender,Department,Admit_Date,Discharge_Date
P1,45,M,Cardiology,2026-08-01,2026-08-05
P2,30,F,Ortho,2026-08-02,2026-08-04
P3,60,M,Cardiology,2026-08-03,2026-08-08
```

Menu option 1 (Department count)

**Expected output:**

```
Cardiology: 2 | Ortho: 1
Total patients: 3
```

### Test Case 2: Boundary / Minimum Input

**Input** (`patients.csv`):

```
Patient_ID,Age,Gender,Department,Admit_Date,Discharge_Date
P4,25,F,ENT,2026-08-10,2026-08-10
```

(same-day discharge). Menu option 2 (Length of stay)

**Expected output:**

```
P4: 0 days
Average stay: 0.00 days
```

### Test Case 3: Invalid Input

**Input:** Test Case 1 rows plus a repeated P1 (duplicate) and P6 with a missing age:

```
Patient_ID,Age,Gender,Department,Admit_Date,Discharge_Date
P1,45,M,Cardiology,2026-08-01,2026-08-05
P2,30,F,Ortho,2026-08-02,2026-08-04
P3,60,M,Cardiology,2026-08-03,2026-08-08
P1,45,M,Cardiology,2026-08-01,2026-08-05
P6,,M,ENT,2026-08-06,2026-08-07
```

**Expected output:**

```
Duplicates removed: 1
Missing Age filled with median: 45
```

### Test Case 4: Different Valid Scenario

**Input:** Same CSV as Test Case 1. Menu option 3 (Stay and age groups)

**Expected output:**

```
Average stay: 3.67 days
Age groups: 0-40: 1 | 41-60: 2 | 61+: 0
Bar chart displayed
```

### Test Result Summary

| Test Case | Type | Result |
|-----------|------|--------|
| 1 | Normal Input | Pass |
| 2 | Boundary / Minimum Input | Pass |
| 3 | Invalid Input | Pass |
| 4 | Different Valid Scenario | Pass |

---

## Requirements Checklist

| Requirement | Status |
|-------------|--------|
| Solution in Python 3, one `.py` file, run from console | Done |
| Load the CSV file using Pandas | Done |
| Clean missing, duplicate and invalid values | Done |
| Use `groupby()` for department-wise and gender-wise analysis | Done |
| Calculate length of stay and plot a Matplotlib chart | Done |

## Conclusion

The Hospital Patient Data Analyzer loads patient records, cleans them, and gives department-wise, gender-wise, length-of-stay and age-group insights through a simple menu with Matplotlib bar charts. All four test cases give the expected output.

## Author

**Jahnvi Sharma**
ERP: RU-26-
Section: B1
Rungta International Skills University
