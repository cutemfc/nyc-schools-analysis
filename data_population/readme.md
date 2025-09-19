# 🧮  Data Integration & Schema Design

Integrating a new dataset into an existing PostgreSQL database. Taking a deeper dive into understanding dataset structure, identifying relevant columns, cleaning messy data, and designing a script-based workflow to load it efficiently.

---

## 🧠 Task Summary

working with a real-world (and purposefully messy) SAT results dataset. Goal is to:

- Inspect and understand the structure of the dataset.
- Select meaningful and relational columns that link to existing tables.
- Identify issues in the data such as duplicates, outliers, or formatting inconsistencies.
- Clean and preprocess the data using Python.
- Prepare the data for database insertion.
- Write a Python script that connects to the database and appends the cleaned data.

By completing this task, you’ll practice translating raw CSV data into relational database entries while thinking critically about schema and data integrity.

---

## Key Finding
- the cleaned data is saveed as meifang_sat_results.csv
- when replace the missing value, it will be better with a reference, if no reference, just keep it.

