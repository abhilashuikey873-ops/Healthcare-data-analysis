# Healthcare Data Analysis Using Python

## Project Overview
This project analyzes healthcare data using Python and Pandas to understand patient distribution, treatment costs, and hospital stays across different departments.

The goal is to summarize healthcare data and generate useful insights to support data-driven decision-making.

## Objectives
- Calculate the total number of patients.
- Analyze patient distribution by department.
- Calculate the average treatment cost for each department.
- Calculate the total treatment cost by department.
- Analyze the average hospital stay by department.

## Technologies Used
- Python
- Pandas
- Jupyter Notebook / VS Code

## Dataset
The project uses a CSV file named `healthcare.csv`.

The dataset includes the following columns:
- `Department` — Hospital department name.
- `Patients` — Number of patients.
- `Treatment_Cost` — Treatment cost.
- `Hospital_Stay` — Duration of hospital stay.

## Analysis Performed
1. **Total Patients:** Calculates the total number of patients in the dataset.
2. **Department-wise Patients:** Calculates the total patients in each department.
3. **Average Treatment Cost:** Finds the average treatment cost for each department.
4. **Total Treatment Cost:** Calculates the total treatment cost for each department.
5. **Average Hospital Stay:** Calculates the average hospital stay for each department.

## Python Libraries
Pandas is used to load, manipulate, group, and analyze the healthcare dataset.

## How to Run the Project

1. Clone or download this repository.
2. Install Python on your computer.
3. Install Pandas:

   ```bash
   pip install pandas
   ```

4. Place `healthcare.csv` in the same folder as `data analysis.py`.
5. Run the Python script:

   ```bash
   python "data analysis.py"
   ```

## Project Structure

```text
Healthcare-Data-Analysis/
│
├── healthcare.csv
├── data analysis.py
└── README.md
```

## Key Learnings
- Loading CSV files using Pandas.
- Working with DataFrames and columns.
- Using `sum()` and `mean()` for calculations.
- Grouping data with `groupby()`.
- Generating department-wise summaries.

## Future Improvements
- Visualize department-wise data using Matplotlib or Seaborn.
- Identify departments with the highest treatment costs.
- Check and handle missing values.
- Create an interactive healthcare dashboard using Power BI.

## Author
Abhilash
