# Data Transformation Documentation

This document describes the transformations, encoding, and rounding applied to the dataset to prepare it for machine learning. Each column's specific treatment is outlined below.

---

## 1. Encoding of Categorical Variables

To convert categorical columns into a format suitable for machine learning, we applied encoding as follows:

### Binary Columns (Encoded as 0 and 1)

These columns contain only two unique values, so they were label-encoded to represent them as binary values (0 and 1).

- **`gender`**
  - `0`: Female
  - `1`: Male

- **`fam_hist_o`** (Family History of Obesity)
  - `0`: No
  - `1`: Yes

- **`favc`** (Frequent Consumption of High Caloric Food)
  - `0`: No
  - `1`: Yes

- **`smoke`**
  - `0`: No
  - `1`: Yes

- **`scc`** (Caloric Consumption Monitoring)
  - `0`: No
  - `1`: Yes

### Multi-Category Columns (Encoded with Unique Integers for Each Category)

Each unique category in these columns was assigned a unique integer value. The integers are arbitrary and do not imply any ordering.

- **`mtrans`** (Mode of Transportation)
  - `0`: Walking
  - `1`: Bike
  - `2`: Motorbike
  - `3`: Public_Transportation
  - `4`: Automobile

- **`obesity_level`**
  - `0`: Insufficient_Weight
  - `1`: Normal_Weight
  - `2`: Overweight_Level_I
  - `3`: Overweight_Level_II
  - `4`: Obesity_Type_I
  - `5`: Obesity_Type_II
  - `6`: Obesity_Type_III

- **`caec`** (Consumption of Alcohol)
  - `0`: No
  - `1`: Sometimes
  - `2`: Frequently
  - `3`: Always

- **`calc`** (Consumption of Food Between Meals)
  - `0`: No
  - `1`: Sometimes
  - `2`: Frequently
  - `3`: Always

---

## 2. Rounding of Numeric Columns

The following rounding adjustments were made to numeric columns to standardize precision and make the dataset more readable.

### Integer Columns

These columns represent counts or whole numbers, so they were rounded to the nearest integer.

- **`age`**: Rounded to the nearest integer (no decimal places).
- **`fcvc`** (Frequency of Consumption of Vegetables)
  - Rounded to the nearest integer.
  - Represents the number of times vegetables are consumed per day.
- **`ncp`** (Number of Main Meals)
  - Rounded to the nearest integer.
  - Represents the typical number of main meals per day.
- **`faf`** (Physical Activity Frequency)
  - Rounded to the nearest integer.
  - Represents the frequency of physical activity per week.
- **`tue`** (Time Using Electronic Devices)
  - Rounded to the nearest integer.
  - Represents hours of electronic device use per day.

### Columns Rounded to 1 Decimal Place

This column likely represents a continuous variable that benefits from slight rounding for clarity.

- **`ch2o`** (Water Consumption in Liters)
  - Rounded to 1 decimal place.
  - Likely represents daily water intake in liters.

### Columns Rounded to 2 Decimal Places

These columns represent physical measurements and derived metrics, so they were rounded to two decimal places for consistency.

- **`height`** (in meters)
  - Rounded to 2 decimal places.
- **`weight`** (in kilograms)
  - Rounded to 2 decimal places.
- **`bmi`** (Body Mass Index)
  - Calculated as `weight / (height ** 2)` if `weight` and `height` are present.
  - Rounded to 2 decimal places for readability.

---

## Summary

- **Encoding**: Binary columns were label-encoded to 0/1, and multi-category columns were label-encoded with unique integers for each category.
- **Rounding**:
  - Integer rounding applied to `age`, `fcvc`, `ncp`, `faf`, and `tue`.
  - 1 decimal place for `ch2o`.
  - 2 decimal places for `height`, `weight`, and `bmi`.

This documentation should provide all necessary information to interpret the processed dataset correctly.
