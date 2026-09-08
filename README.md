# Weekly_tasks
Tasks for Python for Data Science and AIML
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Task Python for Science
1.Out-of-Core CSV Parser & Aggregator with Constant Memory Bounds

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Task AI ML
1.Vectorized Multi-Dimensional A* Pathfinding on OpenStreetMap Graphs

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## SKIL VERSE - Python for Data Analytics with AI assistance ( 12 August 2026 - 7 September)
1. Superstore Sales Project
2. Airline Flights Data Project

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## EDA TASK FOR PYTHON

###  Week 1: Superstore Sales Data Understanding, Cleaning & Exploratory Analysis

### Dataset: Superstore Sales Dataset

### Problem Statement

Raw retail datasets often contain missing values, duplicate entries, inconsistent data types, and extreme outliers. Before generating business insights, the data must be rigorously inspected, cleaned, and standardized.

### Objectives

- Inspect dataset dimensions, column data types, and basic statistics using Pandas.
- Identify and handle missing values, duplicates, and improper data types.
- Detect outliers in continuous variables (Sales, Quantity, Profit, Discount) using IQR and Z-scores.

### Tasks & Deliverables

- Load data via Pandas and inspect with `.info()`, `.describe()`, and `.head()`.
- Convert Order Date and Ship Date into proper datetime objects.
- Clean text formatting across categorical attributes (Category, Sub-Category, Segment).
- Calculate initial summary statistics for numerical attributes.

### Necessary Implementation

- Load the dataset using Pandas.
- Inspect the dataset using `.head()`, `.info()`, `.describe()`, `.shape`, and column information.
- Remove null values.
- Clean text formatting across Category, Sub-Category, and Segment.
- Calculate initial summary statistics for numerical attributes.

### Week 2: Retail Sales Visualization, Relationship Analysis & Business Insights

###  Dataset: Superstore Sales Dataset (Preprocessed from Week 1)

### Problem Statement

Numerical summaries alone fail to explain why certain product lines lose money or how regional discounting strategies impact total revenue. Visual analysis is required to discover profit leaks and growth opportunities.

### Objectives

- Perform univariate, bivariate, and multivariate analysis on sales performance.
- Evaluate profit margins across categories, sub-categories, and geographic regions.
- Analyze the relationship between discounts, sales volume, and overall profitability.

### Tasks & Deliverables

- Construct bar plots and box plots using Seaborn to visualize profit and sales distribution.
- Plot discount levels against profit margins to identify discount thresholds that ruin profitability.
- Generate a correlation heatmap across all numerical attributes.
- Prepare the findings into a 1-page survey report.

### Necessary Implementation

- Construct Seaborn bar plots for sales/profit analysis.
- Construct Seaborn box plots for sales/profit distribution.
- Analyze Discount vs Profit.
- Analyze Discount vs Profit Margin.
- Generate a correlation heatmap for numerical attributes.
- Identify important business findings.
- Prepare a concise 1-page business findings report.
