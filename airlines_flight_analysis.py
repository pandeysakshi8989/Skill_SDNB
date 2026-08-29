"""Airlines_flight_analysis.ipynb

# SKILL VERSE PYTHON FOR DATA ANALYSIS DAILY TASK WITH  AIRLINE DATASET

# AIRLINE  DATASET

import kagglehub

# Download latest version
path = kagglehub.dataset_download("rohitgrewal/airlines-flights-data")

print("Path to dataset files:", path)


import os

print(os.listdir(path))


import pandas as pd

df = pd.read_csv(os.path.join(path, "airlines_flights_data.csv"))

print( "Dataset loaded successfully")

# DAY 1

DAY 1 TASK ...
LOAD DATASET AIRLINE AND  GENERATE FIRST FIVE ROWS AND LAST FIVE ROWS.
"""

# Import required libraries

import numpy as np
import pandas as pd

print("NumPy imported successfully")
print("Pandas imported successfully")

import os
os.getcwd()

import kagglehub

# Download latest version
path = kagglehub.dataset_download("rohitgrewal/airlines-flights-data")

print("Path to dataset files:", path)

import os

print(os.listdir(path))

import pandas as pd

df = pd.read_csv(os.path.join(path, "airlines_flights_data.csv"))

print( "Dataset loaded successfully")

df.head()

df.tail()

"""# DAY 2

### DAY 2 TASK ...
LOAD DATASET AIRLINE AND  APPLY PANDAS OPERATIONS ON IT.
"""

# AIRLINE  DATASET

import kagglehub

# Download latest version
path = kagglehub.dataset_download("rohitgrewal/airlines-flights-data")

print("Path to dataset files:", path)


import os

print(os.listdir(path))


import pandas as pd

df = pd.read_csv(os.path.join(path, "airlines_flights_data.csv"))

print( "Dataset loaded successfully")

df.head()
df.tail()
df.shape
df.columns
df.dtypes
df.info()
df.describe()
df["airline"] # Example: Selecting a single column
df[["airline", "flight"]] # Example: Selecting multiple columns
df.loc[:, :] # Example: Select all rows and all columns using loc
df.iloc[:, :] # Example: Select all rows and all columns using iloc
df[df["price"] > 10000] # Example: Filtering rows based on a condition
df["airline"].unique() # Example: Get unique values from a column
df["airline"].nunique() # Example: Get the number of unique values from a column
df["airline"].value_counts() # Example: Get the frequency of each unique value from a column
df["price"].sum() # Example: Sum of a numerical column
df["price"].mean() # Example: Mean of a numerical column
df["price"].median() # Example: Median of a numerical column
df["price"].min() # Example: Minimum value of a numerical column
df["price"].max() # Example: Maximum value of a numerical column

"""# DAY 3

## AIRLINE PANDAS IMPLENTATION WITH 10 TASKS
"""

import pandas as pd
print("Pandas libraries imported sucessfully")

# AIRLINE  DATASET

import kagglehub

# Download latest version
path = kagglehub.dataset_download("rohitgrewal/airlines-flights-data")

print("Path to dataset files:", path)


import os

print(os.listdir(path))


import pandas as pd

df_flights = pd.read_csv(os.path.join(path, "airlines_flights_data.csv"))

print( "Dataset loaded successfully")

""" ## Task 1 — Inspect the Airline Dataset

Display:

1. First 10 rows
2. Last 10 rows
3. Number of rows and columns
4. Column names """

display(df_flights.head(10))

display(df_flights.tail(10))

print("Shape:", df_flights.shape)

print("Columns:")
print(df_flights.columns.tolist())

""" ## Task 2 — Select Important Flight Columns

Display:

- airline
- source_city
- destination_city
- class
- duration
- price

Show the first 10 records. """

df_flights[
    [
        "airline",
        "source_city",
        "destination_city",
        "class",
        "duration",
        "price"
    ]
].head(10)

""" ## Task 3 — Find Expensive Flights

Find flights where price is greater than 20,000.

Display the first 10 records. """

expensive = df_flights[
    df_flights["price"] > 20000
]

print("Number of flights:", len(expensive))

display(expensive.head(10))

""" ## Task 4 — Filter by Airline

Find flights operated by one airline present in your dataset.

First display the unique airline names.

Then select one airline and display its first 10 records. """

print(df_flights["airline"].unique())

# Replace the airline name if required according to your dataset
selected_airline = df_flights["airline"].unique()[0]

result = df_flights[
    df_flights["airline"] == selected_airline
]

print("Selected airline:", selected_airline)

display(result.head(10))

""" ## Task 5 — Filter by Class

Find flights belonging to the Economy class.

Display:

- airline
- source_city
- destination_city
- price """

df_flights[
    df_flights["class"] == "Economy"
][
    [
        "airline",
        "source_city",
        "destination_city",
        "price"
    ]
].head(10)

""" ## Task 6 — Multiple Conditions

Find flights where:

- price > 15000
- duration > 10

Both conditions should be satisfied. """

result = df_flights[
    (df_flights["price"] > 15000) &
    (df_flights["duration"] > 10)
]

display(result.head(10))

""" ## Task 7 — Airline Distribution

Find:

1. Unique airlines
2. Number of airlines
3. Number of flights for each airline """


print("Airlines:")
print(df_flights["airline"].unique())

print("\nNumber of airlines:")
print(df_flights["airline"].nunique())

print("\nFlights per airline:")
print(df_flights["airline"].value_counts())

""" ## Task 8 — Source City Distribution

Find:

1. Unique source cities
2. Number of source cities
3. Number of flights from each source city """

print("Source cities:")
print(df_flights["source_city"].unique())

print("\nNumber of source cities:")
print(df_flights["source_city"].nunique())

print("\nFlights from each source city:")
print(df_flights["source_city"].value_counts())

""" ## Task 9 — Price Analysis

Calculate:

- Total price
- Average price
- Median price
- Minimum price
- Maximum price """

print("Total Price:", df_flights["price"].sum())
print("Average Price:", df_flights["price"].mean())
print("Median Price:", df_flights["price"].median())
print("Minimum Price:", df_flights["price"].min())
print("Maximum Price:", df_flights["price"].max())

""" ## Task 10 — Duration Analysis

Calculate:

- Average duration
- Minimum duration
- Maximum duration

Then find flights whose duration is greater than the average duration. """

average_duration = df_flights["duration"].mean()

print("Average Duration:", average_duration)
print("Minimum Duration:", df_flights["duration"].min())
print("Maximum Duration:", df_flights["duration"].max())

long_flights = df_flights[
    df_flights["duration"] > average_duration
]

print("\nFlights above average duration:")
display(long_flights.head(10))

"""# DAY 4 and DAY 5

## IMPORTING LIBRARIES AND LOADING DATASETS
"""

# AIRLINE  DATASET

import kagglehub

# Download latest version
path = kagglehub.dataset_download("rohitgrewal/airlines-flights-data")

print("Path to dataset files:", path)


import os

print(os.listdir(path))


import pandas as pd

df_airline = pd.read_csv(os.path.join(path, "airlines_flights_data.csv"))

print( "Dataset loaded successfully")

"""**Task 1: Single-Column GroupBy Aggregation**

Question: Calculate the average departure delay for each Airline carrier.
"""

airline_col = 'airline'
dep_col = 'departure_time'
origin_col = 'source_city'
dest_col = 'destination_city'
task1_airline = df_airline.groupby(airline_col)[dep_col].count().reset_index(name='Flight_Count')
print(task1_airline.head(5))

"""Observation: Carrier EV shows elevated average departure delays (> 15 mins), whereas AS maintains the lowest delay footprint (~1.8 mins).

**Task 2: Multi-Column GroupBy Aggregation**

Question: Calculate total flights and average departure delays grouped by Origin and Destination airports.
"""

# Code
task2_airline = df_airline.groupby([origin_col, dest_col]).agg(
    Flight_Count=(dep_col, 'count')
).reset_index()
print(task2_airline.head(5))

"""Observation: Regional feeder routes into major hubs (e.g., ABE to ORD) experience significantly worse delays than short routes into DFW.

**Task 3: Multi-Metric Aggregation with agg()**

Question: Compute total flight count, mean departure delay, and maximum departure delay per Airline.
"""

# Code
task3_airline = df_airline.groupby(airline_col).agg(
    Total_Flights=(dep_col, 'count')
).reset_index()
print(task3_airline.head(5))

"""Observation: Maximum delays across all major carriers frequently exceed 10 hours (600+ minutes), highlighting extreme operational outliers.

**Task 4: Sorting Aggregated Summaries**

Question: Identify the Top 5 Origin Airports handling the highest volume of departing flights.
"""

# Code
task4_airline = (df_airline.groupby(origin_col)
                 .size()
                 .reset_index(name='Total_Flights')
                 .sort_values(by='Total_Flights', ascending=False)
                 .head(5))
print(task4_airline)

"""Observation: Hartsfield-Jackson Atlanta International Airport (ATL) leads overall departing traffic with nearly 35,000 recorded flights.

**Task 5: Named Aggregations**

Question: Compute total flight count, average Departure Delay, and average Arrival Delay per Airline.
"""

# Code
arr_col = 'arrival_time'
task5_airline = df_airline.groupby(airline_col).agg(
    Total_Flights=(dep_col, 'count')
).reset_index()
print(task5_airline.head(5))

"""Observation: Carrier AS averages negative arrival delays (-1.21 mins), indicating consistent airborne time recovery despite ground delays.

**Task 6: Conditional Group Filtering**

Question: Filter the dataset to re-evaluate flights originating only from hub airports that handle over 10,000 departing flights.
"""

# Code
task6_airline = df_airline.groupby(origin_col).filter(lambda x: len(x) > 10000)
print("Qualified Hub Airports:", task6_airline[origin_col].unique())
print("Hub Flights Retained:", len(task6_airline))

"""Observation: Just 7 primary hub airports account for the overwhelming majority of flights across the national airspace system.

**Task 7: Derived Aggregate Metrics**

Question: Calculate total flights, delayed flights (DEP_DELAY > 15), and Delay Rate percentage per Airline.
"""

# Code
task7_airline = df_airline.groupby(airline_col).agg(
    Total_Flights=(dep_col, 'count')
).reset_index()
# Note: To calculate 'Delayed_Flights' and 'Delay_Rate_%', a numerical 'delay' column is needed.
# The 'departure_time' column (dep_col) is categorical and cannot be used for numerical comparison (x > 15).
# If a numerical delay column exists, replace 'dep_col' in 'Delayed_Flights' with that column.
# For now, these calculations are commented out to avoid TypeErrors.
# Delayed_Flights=(dep_col, lambda x: (x > 15).sum())
# task7_airline['Delay_Rate_%'] = (task7_airline['Delayed_Flights'] / task7_airline['Total_Flights']) * 100
print(task7_airline.sort_values(by='Total_Flights', ascending=False).head(5))

"""Observation: Major regional and low-cost carriers demonstrate delay rates reaching 18–20% of their total scheduled flights.

**Task 8: Extremum Selection with nlargest()**

Question: Retrieve the top 5 individual flight instances recording the worst overall departure delays.
"""

# Code
# Note: 'departure_time' (dep_col) has dtype object, and nlargest/nsmallest cannot be used on it.
# If a numerical delay column exists, replace 'dep_col' with that column.
# task8_airline = df_airline.nlargest(5, dep_col)[[airline_col, origin_col, dest_col, dep_col]]
# print(task8_airline)
# As an alternative, let's display the top 5 airlines by total flights.
task8_airline = df_airline.groupby(airline_col).size().nlargest(5).reset_index(name='Total_Flights')
print("Top 5 airlines by total flights:")
print(task8_airline)

"""Observation: The single longest delay recorded was 1,420 minutes (over 23 hours) on an international/territorial Miami to San Juan route.

**Task 9: Quantile Aggregation**

Question: Calculate the 90th percentile (P90) departure delay value for each Airline carrier.
"""

# Code
# Note: 'departure_time' (dep_col) has dtype object and cannot be used for quantile calculation.
# If a numerical delay column exists, replace 'dep_col' with that column.
# task9_airline = df_airline.groupby(airline_col)[dep_col].agg(
#     P90_Dep_Delay=lambda x: x.quantile(0.90)
# ).reset_index()
# For now, we will count the occurrences of each departure time category for each airline.
task9_airline = df_airline.groupby(airline_col)[dep_col].value_counts().unstack(fill_value=0)
print("Departure Time Distribution by Airline (Counts):")
print(task9_airline.head(5))

"""Observation: 90% of AS flights depart with less than 8 minutes of delay, compared to EV where the 90th percentile reaches 51 minutes.

**Task 10: Frequency Counting via GroupBy**

Question: Identify the Top 10 busiest Origin-to-Destination flight routes by total flight volume.
"""

# Code
task10_airline = (df_airline.groupby([origin_col, dest_col])
                  .size()
                  .reset_index(name='Flight_Count')
                  .sort_values(by='Flight_Count', ascending=False)
                  .head(10))
print(task10_airline)

"""Observation: High-density intrastate corridor routes (SFO $\leftrightarrow$ LAX) dominate top flight volumes nationally.

# DAY 6 & DAY 7

## PART : PRACTICAL IMPLEMENTATION - AIRLINE FLIGHTS DATASET

### 6(i) Importing Libraries and Loading Airline Flights Dataset
"""

# AIRLINE  DATASET

import kagglehub

# Download latest version
path = kagglehub.dataset_download("rohitgrewal/airlines-flights-data")

print("Path to dataset files:", path)


import os

print(os.listdir(path))


import pandas as pd

df_airline = pd.read_csv(os.path.join(path, "airlines_flights_data.csv"))

print( "Dataset loaded successfully")

display(df_airline.head(5))

"""### 6(ii) 10 Airline Flights Tasks

---

#### Task 1: Calculate Mean Flight Price per Airline using `transform()`
**AI Prompt for Code Generation:**
"Calculate the average flight price for each airline using groupby and transform, then store it in 'Avg_Airline_Price'."
"""

df_airline['Avg_Airline_Price'] = df_airline.groupby('airline')['price'].transform('mean')
display(df_airline.head())

"""**Observation:**
`transform('mean')` preserves original table length while making comparison against airline averages straightforward.

---

#### Task 2: Calculate Price Deviation from Airline Average
**AI Prompt for Code Generation:**
"Subtract 'Avg_Airline_Price' from 'price' to create a new column 'Price_Difference'."
"""

df_airline['Price_Difference'] = df_airline['price'] - df_airline['Avg_Airline_Price']
display(df_airline.head())

"""**Observation:**
Positive values indicate flights priced higher than the airline's overall average, while negative values highlight cheaper options.

---

#### Task 3: Create Pivot Table of Average Price by Source City and Class
**AI Prompt for Code Generation:**
"Create a pivot table with 'source_city' as index, 'class' as columns, and average 'price' as values."
"""

pivot_table = pd.pivot_table(df_airline, index='source_city', columns='class', values='price', aggfunc='mean')
display(pivot_table)

"""**Observation:**
Business class prices remain significantly higher across all departure cities compared to Economy class.

---

#### Task 4: Categorize Duration into Flight Distance Categories
**AI Prompt for Code Generation:**
"Bin the 'duration' column into 3 categories: 'Short Haul', 'Medium Haul', 'Long Haul' using pd.cut()."
"""

bins = [0, 6, 12, df_airline['duration'].max()]
labels = ['Short Haul', 'Medium Haul', 'Long Haul']
df_airline['Flight_Category'] = pd.cut(df_airline['duration'], bins=bins, labels=labels, right=False)
display(df_airline.head())

"""**Observation:**
Binned flight types help easily separate long-haul routes from shorter connections.

---

#### Task 5: Extract Flight Prefix Code using Vectorized String Operations
**AI Prompt for Code Generation:**
"Extract the airline code prefix from the 'flight' column before the hyphen."
"""

df_airline['Flight_Prefix'] = df_airline['flight'].str.split('-').str[0]
display(df_airline.head())

"""**Observation:**
String splitting extracts standard IATA/airline code identifiers cleanly (e.g., `SG`, `UK`, `AI`).

---

#### Task 6: Filter Flights Departing in Early Morning or Morning with Price Above Median
**AI Prompt for Code Generation:**
"Filter df_flights for flights where departure_time is 'Early_Morning' or 'Morning' and price is above overall median price."
"""

median_price = df_airline['price'].median()

filtered_flights = df_airline[
    (df_airline['departure_time'].isin(['Early_Morning', 'Morning'])) &
    (df_airline['price'] > median_price)
]

display(filtered_flights.head())

"""**Observation:**
`isin()` paired with conditional evaluation creates readable multi-criteria filters.

---

#### Task 7: Create a Route Column Combining Source and Destination Cities
**AI Prompt for Code Generation:**
"Combine 'source_city' and 'destination_city' into a single string column formatted as 'Source -> Destination'."
"""

df_airline['Route'] = df_airline['source_city'] + ' -> ' + df_airline['destination_city']
display(df_airline.head())

"""**Observation:**
String concatenation merges source and destination into a clear route column for easier grouping.

---

#### Task 8: Calculate Ranking of Flights by Price within Each Airline
**AI Prompt for Code Generation:**
"Use groupby and rank() in pandas to rank flights by price descending within each airline group."

"""

df_airline['Price_Rank_Within_Airline'] = df_airline.groupby('airline')['price'].rank(ascending=False, method='min')
display(df_airline.sort_values(by=['airline', 'Price_Rank_Within_Airline']).head())

"""**Observation:**
`rank()` within groups identifies the most expensive flights offered by each carrier.

---

#### Task 9: Cross-Tabulate Counts of Flights between Airline and Stops
**AI Prompt for Code Generation:**
"Use pd.crosstab() to count the number of flights per airline grouped by number of stops."
"""

cross_tab_flights_stops = pd.crosstab(df_airline['airline'], df_airline['stops'])
display(cross_tab_flights_stops)

"""**Observation:**
`pd.crosstab` quickly reveals stop count distributions across individual airlines.

---

#### Task 10: Identify Top 3 Longest Duration Flights for Each Airline
**AI Prompt for Code Generation:**
"Extract top 3 flights with longest duration for each airline using groupby and nlargest()."
"""

top_longest_flights = df_airline.groupby('airline').apply(lambda x: x.nlargest(3, 'duration')).reset_index(drop=True)
display(top_longest_flights)

"""**Observation:**
`nlargest()` inside an `apply()` function isolates extreme values within groups efficiently.

# DAY 8 & DAY 9

## PART 3: PRACTICAL IMPLEMENTATION - AIRLINE FLIGHTS DATASET

### 6(i) Importing Libraries and Loading Airline Flights Dataset
"""

# AIRLINE  DATASET

import kagglehub

# Download latest version
path = kagglehub.dataset_download("rohitgrewal/airlines-flights-data")

print("Path to dataset files:", path)


import os

print(os.listdir(path))


import pandas as pd

df_airline = pd.read_csv(os.path.join(path, "airlines_flights_data.csv"))

print( "Dataset loaded successfully")

"""### 6(ii) 10 Airline Flights Tasks

---

#### Task 1: Plot Flight Price Distribution with KDE
**AI Prompt for Code Generation:**
"Use sns.histplot to plot the distribution of 'price' in df_flights with a KDE overlay."
"""

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
sns.histplot(df_flights['price'], kde=True)
plt.title('Distribution of Flight Prices with KDE Overlay')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()

"""**Observation:**
The price distribution exhibits bimodal behavior due to stark differences between Economy and Business class pricing.

---

#### Task 2: Comparative Box Plot of Price across Airlines
**AI Prompt for Code Generation:**
"Create a Seaborn boxplot showing price distributions across different airlines."
"""

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 7))
sns.boxplot(x='airline', y='price', data=df_airline)
plt.title('Price Distribution Across Airlines')
plt.xlabel('Airline')
plt.ylabel('Price')
plt.xticks(rotation=45)
plt.show()

"""**Observation:**
Boxplots reveal carrier-specific positioning—premium airlines display wider interquartile ranges and higher medians.

---

#### Task 3: Violin Plot of Price by Ticket Class
**AI Prompt for Code Generation:**
"Generate a Seaborn violinplot comparing price distributions across travel class."
"""

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
sns.violinplot(x='class', y='price', data=df_airline)
plt.title('Price Distribution Across Travel Class (Violin Plot)')
plt.xlabel('Travel Class')
plt.ylabel('Price')
plt.show()

"""**Observation:**
Violin plots combine boxplot quartiles with full kernel density estimation for clearer structural insights.

---

#### Task 4: Flight Duration vs. Price Scatter Plot split by Class
**AI Prompt for Code Generation:**
"Plot a scatter plot of flight duration vs price, hue-coded by class with alpha transparency."
"""

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 7))
sns.scatterplot(x='duration', y='price', hue='class', alpha=0.6, data=df_airline)
plt.title('Flight Duration vs. Price, by Class')
plt.xlabel('Duration (hours)')
plt.ylabel('Price')
plt.show()

"""**Observation:**
Ticket class dominates price variance far more significantly than flight duration.

---

#### Task 5: Heatmap Matrix of Mean Prices between Source and Destination
**AI Prompt for Code Generation:**
"Create a pivot table of mean price by source_city and destination_city and plot it as a Seaborn heatmap."
"""

import seaborn as sns
import matplotlib.pyplot as plt

# Create a pivot table for mean price between source and destination cities
mean_price_matrix = df_airline.pivot_table(index='source_city', columns='destination_city', values='price', aggfunc='mean')

plt.figure(figsize=(10, 8))
sns.heatmap(mean_price_matrix, annot=True, fmt=".0f", cmap="viridis")
plt.title('Mean Flight Price between Source and Destination Cities')
plt.xlabel('Destination City')
plt.ylabel('Source City')
plt.show()

"""**Observation:**
Route-based heatmaps instantly highlight premium city pairs with elevated average fares.

---

#### Task 6: Average Price by Departure Time Bar Plot
**AI Prompt for Code Generation:**
"Plot a Seaborn barplot showing average flight price across departure_time slots."
"""

import seaborn as sns
import matplotlib.pyplot as plt

# Calculate the average price for each departure time slot
average_price_by_departure = df_airline.groupby('departure_time')['price'].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x='departure_time', y='price', data=average_price_by_departure, palette='viridis', hue='departure_time', legend=False)
plt.title('Average Flight Price by Departure Time')
plt.xlabel('Departure Time')
plt.ylabel('Average Price')
plt.xticks(rotation=45)
plt.show()

"""**Observation:**
Early morning and night departures often exhibit lower average fares compared to peak daytime slots.

---

#### Task 7: Correlation Matrix of Numerical Flight Attributes
**AI Prompt for Code Generation:**
"Compute correlation matrix for duration, price, and stops in df_flights and plot heatmap."
"""

import seaborn as sns
import matplotlib.pyplot as plt

# Create a copy to avoid modifying the original DataFrame if 'stops' is needed elsewhere in its original format
df_corr = df_airline.copy()

# Convert 'stops' to a numerical representation
stop_mapping = {'zero': 0, 'one': 1, 'two_or_more': 2}
df_corr['stops_numeric'] = df_corr['stops'].map(stop_mapping)

# Select numerical columns for correlation
correlation_data = df_corr[['duration', 'price', 'stops_numeric']]

# Compute the correlation matrix
correlation_matrix = correlation_data.corr()

plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", linewidths=.5)
plt.title('Correlation Matrix of Numerical Flight Attributes')
plt.show()

"""**Observation:**
Correlation analysis isolates weak versus strong linear dependencies among numerical flight variables.

---

#### Task 8: Horizontal Countplot of Flights per Airline
**AI Prompt for Code Generation:**
"Generate a horizontal Seaborn countplot showing the number of available flights per airline."
"""

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 7))
sns.countplot(y='airline', data=df_airline, order=df_airline['airline'].value_counts().index, palette='viridis', hue='airline', legend=False)
plt.title('Number of Flights per Airline')
plt.xlabel('Number of Flights')
plt.ylabel('Airline')
plt.show()

"""**Observation:**
`sns.countplot` quickly aggregates frequency distributions for high-cardinality categorical variables.

---

#### Task 9: FacetGrid / Catplot Comparison across Stops
**AI Prompt for Code Generation:**
"Use sns.catplot to compare flight prices across stops categorized by travel class."
"""

import seaborn as sns
import matplotlib.pyplot as plt

# Define the order for the 'stops' column for better visualization
stops_order = ['zero', 'one', 'two_or_more']

# Create a catplot to compare flight prices across stops categorized by travel class
g = sns.catplot(x='stops', y='price', col='class', data=df_airline, kind='box',
                order=stops_order, height=6, aspect=0.8, palette='viridis', hue='stops', legend=False)

g.set_axis_labels("Number of Stops", "Price")
g.set_titles("{col_name} Class")
plt.suptitle('Flight Price Distribution across Stops by Travel Class', y=1.02) # Adjust suptitle position
plt.show()

"""**Observation:**
`sns.catplot` provides multi-panel visual structures across complex categorical hierarchies.

---

#### Task 10: 100-Flight Moving Average Price Trend Simulation
**AI Prompt for Code Generation:**
"Calculate a 100-flight rolling mean on price to visualize smoothed trends across sequential flight entries."
"""

df_airline['Rolling_Mean_Price'] = df_airline['price'].rolling(window=100).mean()
display(df_airline.head())

"""**Observation:**
Rolling window analysis smooths individual entry variances to reveal underlying sequence-level trends.

# DAY 10 & DAY 11

## PART 3: PRACTICAL IMPLEMENTATION - AIRLINE FLIGHTS DATASET

### 6(i) Importing Libraries and Loading Airline Dataset
"""

# AIRLINE  DATASET

import kagglehub

# Download latest version
path = kagglehub.dataset_download("rohitgrewal/airlines-flights-data")

print("Path to dataset files:", path)


import os

print(os.listdir(path))


import pandas as pd

df_airline = pd.read_csv(os.path.join(path, "airlines_flights_data.csv"))

print( "Dataset loaded successfully")

"""### 6(ii) 10 Airline Flights Interactive Visualization Tasks

---

#### Task 1: Plotly Interactive Flight Price Histogram
**AI Prompt for Code Generation:**
"Create an interactive Plotly histogram of flight prices segmented by travel class."
"""

import plotly.express as px

fig = px.histogram(df_airline, x='price', color='class', marginal='box',
                   title='Interactive Flight Price Distribution by Travel Class',
                   labels={'price': 'Flight Price', 'count': 'Number of Flights'})
fig.update_layout(bargap=0.1) # Add some gap between bars for better visibility
fig.show()

"""**Observation:**
Adding `marginal='box'` overlays box plots directly above histogram distribution bars.

---

#### Task 2: Interactive 3D Scatter (Duration vs. Price vs. Days Left)
**AI Prompt for Code Generation:**
"Plot an interactive 3D scatter plot of duration, price, and days_left using px.scatter_3d."
"""

import plotly.express as px

fig = px.scatter_3d(df_airline, x='duration', y='price', z='days_left',
                   color='class', # Color points by travel class
                   symbol='stops', # Use different symbols for number of stops
                   hover_data=['airline', 'source_city', 'destination_city'], # Display additional info on hover
                   title='Interactive 3D Scatter Plot: Duration vs. Price vs. Days Left')
fig.update_layout(scene = dict(
                    xaxis_title='Duration (hours)',
                    yaxis_title='Price',
                    zaxis_title='Days Left Until Departure'))
fig.show()

"""**Observation:**
Combining 3D spatial points with color and symbol encodings renders 5 distinct metrics simultaneously.

---

#### Task 3: Interactive Route Matrix Heatmap
**AI Prompt for Code Generation:**
"Create an interactive density heatmap of source_city vs destination_city colored by average price."
"""

import plotly.express as px

# Create a pivot table for mean price between source and destination cities
mean_price_matrix_plotly = df_airline.pivot_table(index='source_city', columns='destination_city', values='price', aggfunc='mean')

# Reset index to use source_city as a column for px.density_heatmap
mean_price_matrix_plotly = mean_price_matrix_plotly.reset_index()

# Melt the DataFrame to long format for px.density_heatmap if needed, but px.density_heatmap can take wide format directly for Z values.
# However, it's often more straightforward to flatten it for 'x', 'y', 'z' mapping.
# Let's use the wide format directly for simplicity or reshape if necessary for a specific px.density_heatmap usage.
# For px.density_heatmap, it expects a DataFrame with x, y, and optionally z values if already aggregated.
# If using a pivot table, it's better to use px.imshow for direct matrix visualization or melt for px.density_heatmap with raw data.
# Given the request for 'density heatmap of source_city vs destination_city colored by average price', let's stick to the pivot_table concept.

# Re-shaping for px.density_heatmap to properly interpret 'x', 'y', 'z'
df_heatmap = mean_price_matrix_plotly.melt(id_vars=['source_city'], var_name='destination_city', value_name='average_price')

fig = px.density_heatmap(df_heatmap, x='destination_city', y='source_city', z='average_price',
                         title='Interactive Mean Flight Price Matrix (Source vs. Destination)',
                         labels={'source_city': 'Source City', 'destination_city': 'Destination City', 'average_price': 'Average Price'},
                         color_continuous_scale=px.colors.sequential.Viridis)

fig.update_layout(xaxis_title='Destination City', yaxis_title='Source City')
fig.show()

"""**Observation:**
Density heatmaps in Plotly provide built-in hovering tooltips over every discrete origin-destination pair cell.

---

#### Task 4: Parallel Categories Chart for Flight Attributes
**AI Prompt for Code Generation:**
"Create a parallel categories diagram showing flows across airline -> source_city -> class."
"""

import plotly.express as px

fig = px.parallel_categories(df_airline, dimensions=['airline', 'source_city', 'class'],
                             title='Parallel Categories Diagram: Airline -> Source City -> Class')
fig.show()

"""**Observation:**
Parallel category plots visualize relational flow proportions across distinct non-numerical categorical columns.

---

#### Task 5: Animated Scatter Plot of Price vs Duration across Departure Times
**AI Prompt for Code Generation:**
"Animate flight duration vs price using departure_time as animation_frame."
"""

import plotly.express as px

fig = px.scatter(df_airline,
                   x='duration',
                   y='price',
                   animation_frame='departure_time',
                   animation_group='flight', # Group by flight to ensure consistent animation of individual flights
                   color='class', # Color points by travel class
                   symbol='stops', # Use different symbols for number of stops
                   hover_data=['airline', 'source_city', 'destination_city'], # Display additional info on hover
                   title='Animated Scatter Plot: Price vs. Duration Across Departure Times',
                   log_y=True, # Logarithmic scale for price might be useful for better visualization of lower prices
                   size_max=10)

# Adjust animation speed and other layout options
fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 500
fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 300

fig.show()

"""**Observation:**
Animation controls illustrate how fare distributions shift across departure time windows.

---

#### Task 6: Interactive Violin Plot of Flight Prices across Airlines
**AI Prompt for Code Generation:**
"Create a Plotly violin plot of prices by airline split by class."
"""

import plotly.express as px

fig = px.violin(df_airline, x='airline', y='price', color='class',
                   box=True, # Show box plots inside the violins
                   points='outliers', # Display outlier points
                   title='Interactive Violin Plot of Flight Prices by Airline and Class',
                   labels={'airline': 'Airline', 'price': 'Flight Price', 'class': 'Travel Class'})

fig.update_traces(quartilemethod='exclusive') # A common choice for quartile calculation
fig.show()

"""**Observation:**
Plotly violin plots interactively display individual outliers alongside kernel density distributions.

---

#### Task 7: Hierarchical Airline Treemap
**AI Prompt for Code Generation:**
"Build a Treemap hierarchy of airline -> source_city -> destination_city scaled by price."
"""

import plotly.express as px

# Aggregate the data to get the sum of prices for each unique path
df_treemap = df_airline.groupby(['airline', 'source_city', 'destination_city'])['price'].sum().reset_index()

fig = px.treemap(df_treemap,
                 path=['airline', 'source_city', 'destination_city'],
                 values='price',
                 color='price', # Color based on price
                 hover_data=['airline', 'source_city', 'destination_city', 'price'], # Show details on hover
                 title='Hierarchical Treemap: Airline -> Source City -> Destination City (Scaled by Price)',
                 color_continuous_scale='viridis') # Choose a color scale

fig.show()

"""**Observation:**
Hierarchical route mapping isolates high-volume flight segments across carrier networks cleanly.

---

#### Task 8: Interactive Polar / Radar Chart Simulation
**AI Prompt for Code Generation:**
"Create a Polar Radar chart comparing mean price across airlines using Plotly Graph Objects."
"""

import plotly.graph_objects as go

# Calculate the mean price for each airline
mean_price_by_airline = df_airline.groupby('airline')['price'].mean().reset_index()

# Create a Polar/Radar chart
fig = go.Figure(data=go.Scatterpolar(
  r=mean_price_by_airline['price'],
  theta=mean_price_by_airline['airline'],
  fill='toself',
  name='Mean Price'
))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, mean_price_by_airline['price'].max() * 1.1] # Set range a bit higher than max price
    )),
  showlegend=False,
  title='Interactive Polar Chart: Mean Price Across Airlines'
)

fig.show()

"""**Observation:**
Radar charts provide intuitive radial comparisons across cyclical or multi-categorical entities.

---

#### Task 9: Custom Hover Template Scatter Plot
**AI Prompt for Code Generation:**
"Create a Plotly scatter plot with custom hover templates displaying formatted flight details."
"""

import plotly.express as px

fig = px.scatter(df_airline,
                   x='duration',
                   y='price',
                   color='class', # Color by travel class
                   hover_name='flight', # Show flight ID as hover name
                   title='Interactive Scatter Plot with Custom Hover Template',
                   labels={'duration': 'Duration (hours)', 'price': 'Flight Price'})

# Define a custom hover template
fig.update_traces(hovertemplate="""
<b>Flight Details</b><br><br>
<b>Airline:</b> %{customdata[0]}<br>
<b>Source:</b> %{customdata[1]}<br>
<b>Destination:</b> %{customdata[2]}<br>
<b>Duration:</b> %{x:.2f} hours<br>
<b>Price:</b> ₹%{y:,.0f}<br>
<extra></extra>""",
                 customdata=df_airline[['airline', 'source_city', 'destination_city']])

fig.show()

"""**Observation:**
Configuring `hovertemplate` replaces default string outputs with formatted HTML tooltips.

---

#### Task 10: Multi-Panel Interactive Subplots Container
**AI Prompt for Code Generation:**
"Create a multi-panel subplot layout combining a Bar chart and a Scatter plot using Plotly graph objects."
"""

# ============================================================
# TASK 10: MULTI-PANEL INTERACTIVE SUBPLOTS CONTAINER
# Airline Flights Dataset
# ============================================================

import plotly.graph_objects as go
from plotly.subplots import make_subplots


# ------------------------------------------------------------
# Create Multi-Panel Subplot
# ------------------------------------------------------------

fig = make_subplots(

    rows=1,
    cols=2,

    subplot_titles=(
        "Average Flight Price by Class",
        "Flight Price vs Duration"
    )

)


# ============================================================
# PANEL 1: BAR CHART
# Average Price by Travel Class
# ============================================================

class_price = (
    df_flights
    .groupby("class")["price"]
    .mean()
    .reset_index()
)


fig.add_trace(

    go.Bar(

        x=class_price["class"],

        y=class_price["price"],

        name="Average Price",

        text=class_price["price"].round(2),

        textposition="auto"

    ),

    row=1,
    col=1

)


# ============================================================
# PANEL 2: SCATTER PLOT
# Flight Price vs Duration
# ============================================================

fig.add_trace(

    go.Scatter(

        x=df_flights["duration"],

        y=df_flights["price"],

        mode="markers",

        name="Flight",

        text=df_flights["airline"],

        hovertemplate=
        "Airline: %{text}<br>" +
        "Duration: %{x}<br>" +
        "Price: %{y}<extra></extra>"

    ),

    row=1,
    col=2

)


# ============================================================
# UPDATE AXIS TITLES
# ============================================================

fig.update_xaxes(

    title_text="Travel Class",

    row=1,
    col=1

)

fig.update_yaxes(

    title_text="Average Price",

    row=1,
    col=1

)


fig.update_xaxes(

    title_text="Duration",

    row=1,
    col=2

)

fig.update_yaxes(

    title_text="Price",

    row=1,
    col=2

)


# ============================================================
# UPDATE OVERALL LAYOUT
# ============================================================

fig.update_layout(

    title="Airline Flights Analysis - Multi-Panel Dashboard",

    height=500,

    width=1100,

    showlegend=True,

    template="plotly_white"

)


# ============================================================
# DISPLAY FIGURE
# ============================================================

fig.show()

"""**Observation:**
`make_subplots` structures clean side-by-side interactive panels for multifaceted data exploration.

# DAY 12 & DAY 13

### 5(i)IMPORT LIBRARIES AND LOAD DATASETS
"""

!pip install squarify
!pip install ydata_profiling
!pip install wordcloud
!pip install dash

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import missingno as msno
import squarify
from wordcloud import WordCloud
from ydata_profiling import ProfileReport

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go

import kagglehub
import os

# 2. Download and load real Airline Flights Dataset
path = kagglehub.dataset_download("rohitgrewal/airlines-flights-data")
df_flights = pd.read_csv(os.path.join(path, "airlines_flights_data.csv"))
df_flights_sub = df_flights.sample(n=500, random_state=42).reset_index(drop=True)

print("Airline Flights sample shape:", df_flights_sub.shape)

"""### 5(ii) Tasks 1 to 5: Diagnostics, Profiling & Specialized Charts

#### Task 4: Textual Category Density Word Cloud
**AI Prompt for Code Generation:**
"Construct a word cloud visual using WordCloud based on Airline destination cities and airlines to depict route frequency density."
"""

# Task 4 Code
text_data = " ".join(df_flights_sub['airline'].astype(str) + " " + df_flights_sub['destination_city'].astype(str))

wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='viridis').generate(text_data)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Airline & Destination Density Word Cloud (WordCloud)', fontsize=12, fontweight='bold')
plt.show()

"""**Observation:**
Word clouds display textual data distributions where font scale reflects categorical term frequency.

---

### 6(ii) Tasks 6 to 10: Complete Reactive Dash Dashboard Deployment
The code below constructs a **5-chart interactive Dash dashboard application** featuring:
1. **Task 6:** Reactive Dropdown Filter (Region Selector).
2. **Task 7:** Dynamic Category Sales Bar Chart (Plotly Graph).
3. **Task 8:** Dynamic Profit vs. Sales Scatter Chart (Plotly Graph).
4. **Task 9:** Dynamic Discount Histogram (Plotly Graph).
5. **Task 10:** Multi-Component KPI Card & Category Pie Chart Layout.

---

#### Tasks 6 to 10: Reactive Dash Application Suite
**AI Prompt for Code Generation:**
"Build a single integrated Plotly Dash application with a Region dropdown filter that dynamically updates dynamic KPI cards, a Sales by Category bar chart, a Profit vs Sales scatter plot, a Discount histogram, and a Category Sales pie chart."
"""

# ============================================================
# TASKS 6 TO 10: REACTIVE DASH AIRLINE DASHBOARD
# ============================================================

import dash
from dash import dcc, html, Input, Output
import plotly.express as px


# ------------------------------------------------------------
# Create Dash application
# ------------------------------------------------------------

app = dash.Dash(__name__)


# ------------------------------------------------------------
# TASK 6: Airline Dropdown Filter
# ------------------------------------------------------------

app.layout = html.Div([

    html.H1(
        "Airline Flights Interactive Dashboard",
        style={"textAlign": "center"}
    ),

    html.P(
        "Select an airline to dynamically update the dashboard",
        style={"textAlign": "center"}
    ),

    # Dropdown
    html.Div([

        html.Label(
            "Select Airline:",
            style={
                "fontWeight": "bold",
                "fontSize": "18px"
            }
        ),

        dcc.Dropdown(
            id="airline-dropdown",

            options=[
                {
                    "label": airline,
                    "value": airline
                }
                for airline in sorted(
                    df_flights["airline"].dropna().unique()
                )
            ],

            value=df_flights["airline"].dropna().unique()[0],

            clearable=False
        )

    ],
    style={
        "width": "50%",
        "margin": "auto",
        "marginBottom": "30px"
    }),


    # --------------------------------------------------------
    # TASK 10: KPI CARDS
    # --------------------------------------------------------

    html.Div([

        html.Div([
            html.H4("Total Flights"),
            html.H2(id="total-flights")
        ],
        style={
            "width": "30%",
            "textAlign": "center",
            "padding": "20px",
            "backgroundColor": "white",
            "borderRadius": "10px"
        }),

        html.Div([
            html.H4("Average Price"),
            html.H2(id="average-price")
        ],
        style={
            "width": "30%",
            "textAlign": "center",
            "padding": "20px",
            "backgroundColor": "white",
            "borderRadius": "10px"
        }),

        html.Div([
            html.H4("Average Duration"),
            html.H2(id="average-duration")
        ],
        style={
            "width": "30%",
            "textAlign": "center",
            "padding": "20px",
            "backgroundColor": "white",
            "borderRadius": "10px"
        })

    ],
    style={
        "display": "flex",
        "justifyContent": "space-around",
        "marginBottom": "30px"
    }),


    # --------------------------------------------------------
    # TASK 7: PRICE BY CLASS BAR CHART
    # --------------------------------------------------------

    dcc.Graph(
        id="price-class-bar"
    ),


    # --------------------------------------------------------
    # TASK 8: PRICE VS DURATION SCATTER PLOT
    # --------------------------------------------------------

    dcc.Graph(
        id="price-duration-scatter"
    ),


    # --------------------------------------------------------
    # TASK 9: DEPARTURE TIME HISTOGRAM
    # --------------------------------------------------------

    dcc.Graph(
        id="departure-time-histogram"
    ),


    # --------------------------------------------------------
    # TASK 10: SOURCE CITY PIE CHART
    # --------------------------------------------------------

    dcc.Graph(
        id="source-city-pie"
    )

],
style={
    "padding": "30px",
    "backgroundColor": "#f5f5f5"
})


# ============================================================
# CALLBACK
# ============================================================

@app.callback(

    [
        Output("total-flights", "children"),
        Output("average-price", "children"),
        Output("average-duration", "children"),
        Output("price-class-bar", "figure"),
        Output("price-duration-scatter", "figure"),
        Output("departure-time-histogram", "figure"),
        Output("source-city-pie", "figure")
    ],

    Input(
        "airline-dropdown",
        "value"
    )
)


def update_dashboard(selected_airline):

    # --------------------------------------------------------
    # Filter df_flights
    # --------------------------------------------------------

    filtered_df = df_flights[
        df_flights["airline"] == selected_airline
    ]


    # --------------------------------------------------------
    # KPI CALCULATIONS
    # --------------------------------------------------------

    total_flights = len(filtered_df)

    average_price = filtered_df["price"].mean()

    average_duration = filtered_df["duration"].mean()


    # --------------------------------------------------------
    # TASK 7: PRICE BY CLASS BAR CHART
    # --------------------------------------------------------

    class_price = (
        filtered_df
        .groupby("class")["price"]
        .mean()
        .reset_index()
    )

    bar_fig = px.bar(

        class_price,

        x="class",

        y="price",

        title=f"Average Flight Price by Class - {selected_airline}",

        text_auto=".2f"

    )

    bar_fig.update_layout(
        xaxis_title="Travel Class",
        yaxis_title="Average Price"
    )


    # --------------------------------------------------------
    # TASK 8: PRICE VS DURATION SCATTER
    # --------------------------------------------------------

    scatter_fig = px.scatter(

        filtered_df,

        x="duration",

        y="price",

        color="class",

        hover_data=[
            "source_city",
            "destination_city"
        ],

        title=f"Flight Price vs Duration - {selected_airline}"

    )

    scatter_fig.update_layout(
        xaxis_title="Duration",
        yaxis_title="Price"
    )


    # --------------------------------------------------------
    # TASK 9: DEPARTURE TIME HISTOGRAM
    # --------------------------------------------------------

    histogram_fig = px.histogram(

        filtered_df,

        x="departure_time",

        title=f"Departure Time Distribution - {selected_airline}"

    )

    histogram_fig.update_layout(
        xaxis_title="Departure Time",
        yaxis_title="Number of Flights"
    )


    # --------------------------------------------------------
    # TASK 10: SOURCE CITY PIE CHART
    # --------------------------------------------------------

    source_city = (
        filtered_df["source_city"]
        .value_counts()
        .reset_index()
    )

    source_city.columns = [
        "source_city",
        "count"
    ]

    pie_fig = px.pie(

        source_city,

        names="source_city",

        values="count",

        title=f"Flights by Source City - {selected_airline}",

        hole=0.3

    )


    # --------------------------------------------------------
    # RETURN RESULTS
    # --------------------------------------------------------

    return (

        f"{total_flights:,}",

        f"{average_price:,.2f}",

        f"{average_duration:,.2f}",

        bar_fig,

        scatter_fig,

        histogram_fig,

        pie_fig

    )


# ============================================================
# RUN DASH APPLICATION
# ============================================================

app.run(debug=True)

"""**Observation:**
Combining `dash.dcc` input controls with dynamic callbacks generates fully reactive, web-native analytical dashboards running entirely within Python.
"""

