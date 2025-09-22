# 🗓️ NYC Schools Data Analysis and Cleaning Project

## Goal: This repository is collected of projects focused on analyzing and cleaning datasets from the New York City public school system. 

It integrates work on:

1.SAT REsults Cleaning and Outlier Removal

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

-requirements:python dependencies


### 📊 Datasets & Data Cleaning Day 
Source: NYPC public High Schools SAT Scores Dataset

## 🧰 1 Cleaning Steps: 
Renamed columns to make consistant

Numeric values of columns

Remove the duplicate rows

Remove outliers (usingf IQR methods , SAT between 200-800) 

Converted the % (graduate and attentation rates) to numeric

Remove unrelated column and duplicate typo column 


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

### Insight
Bronx showed higer incident rates compared to its number of schools.Some school reported zero incidients-possible underreporting. Certain years had spikes in specific incidient types.
---

###  4 General NYC Schools Demographics and Performance Analysis
Integration & Schema Design
 
General NYC schools Analysis (PostgreSQL+ Python) Focus: Demographic and performance queries

> 🧰 Skills: Data modeling, ETL scripting, foreign key relationships, INSERTs via Python
> 
> ### Key Analysis
> Count schools by borough
> Joined datasets on dbn to merge demographics with performance

---
### How to run
Clone the repository git clone[
(https://github.com/yourusername/nyc-schools-analysis.git)] cd nyc-schools-analysis

Setup the environment based on requirements
