# 🗓️ NYC Schools Data Analysis and Cleaning Project

## Goal: This repository is collected of projects focused on analyzing and cleaning datasets from the New York City public school system. 

It integrates work on:

1.SAT Results Cleaning and Outlier Removal

2.Brooklyn School Data Analysis

3.NYC School Incidients Analysis

4.General NYC Schools Demographics and Performance Analysis

The goal is to produce high-quality and cleaned datasets and insightful analytics to understand school performance, demographics, and safety across NYC boroughs.



---

## 📍 Projects Structure
-data

-notebook

-Python scripts

-Outputs

-requirements:
python dependencies


### 📊 Datasets & Data Cleaning Day 
Source: NYPC public High Schools SAT Scores Dataset

## 🧰 1 Cleaning Steps: 
Renamed columns to make consistant

Numeric values of columns

Remove the duplicate rows

Remove outliers (using IQR methods , SAT between 200-800) 

Converted the % (graduate and attentation rates) to numeric

Remove unrelated column and duplicate typo column 

## Result
<img width="1558" height="482" alt="Screenshot 2025-09-22 at 17 02 10" src="https://github.com/user-attachments/assets/fc7534ef-9cbf-46af-b6d4-5bcd06284669" />


> ## 🧰 2 Brooklyn School Data Analysis
### Objective: 
Analyze Brooklyn high schools for performance and enrollment trends

### Key Steps:
Filtered dataset for **Brooklyn school only**

Normalized column names

Counted Unique schools and **Grade 9 entry  offerings**

Summarized **average student count borough**

Created **bar chars** showing school distribution by borough

### Insight:
Brooklyn has the highest number schools

A large portion of Brooklyn schools offer 9 Grade entry

Enrollment varies significantly between boroughs

<img width="704" height="470" alt="image" src="https://github.com/user-attachments/assets/87cc69a5-5569-4715-b0a4-312ba68b2710" />



---

### 🗃️ 3 NYC School incidients Analysis
### Objects:
Understand incident patterns in NYC schools


### Data Cleaning:
Standardize column names(lowerase, underscores, no special characters)
Used Google Sheets quick cleaning

Analysis performed: 
Count total and unique schools.
Found the most freques incidient incident type
calculate the % of incidents in the Bronx
created pivot tables and charts for borough level distribution.

### Insight: 

Bronx showed higer incident rates compared to its number of schools.Some school reported zero incidients-possible underreporting. Certain years had spikes in specific incidient types.


### 🗃️ 4 General NYC Schools Demographics and Performance Analysis
Integration & Schema Design
 
General NYC schools Analysis (PostgreSQL+ Python) Focus: Demographic and performance queries

Skills: Data modeling, ETL scripting, foreign key relationships, INSERTs via Python
> 
> ### Key Analysis
> Count schools by borough
> Joined datasets on dbn to merge demographics with performance


## Data Engineering Pipeline (ETL)

This project implements a robust **ETL (Extract, Transform, Load)** pipeline using Python and Pandas to analyze New York City school data. 

### 1. Extract
* **Source Aggregation:** Automatically retrieves heterogeneous datasets from fragmented directory structures (`school_directory_exploration`, `incident_analysis`, and `data_population`).
* **Path Resolution:** Implements a dynamic file-mapping system to handle diverse naming conventions and directory depths.

### 2. Transform (Quality Control)
* **Data Cleaning:** Standardizes numeric types and implements automated imputation (mean substitution) for missing values.
* **Feature Engineering:** Calculates derivative metrics such as `total_SAT` scores to facilitate downstream analysis.
* **Standardization:** Normalizes primary keys (e.g., `DBN`) to ensure relational interoperability across tables.

### 3. Load
* **Analysis-Ready State:** Consolidates processed data into a unified Python dictionary structure, prepared for high-fidelity statistical modeling or database ingestion.---
### How to run
Clone the repository git clone[
(https://github.com/yourusername/nyc-schools-analysis.git)] cd nyc-schools-analysis

Setup the environment based on requirements
