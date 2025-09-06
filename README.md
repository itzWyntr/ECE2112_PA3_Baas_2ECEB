# PA3 - Pandas

PA3 consists of 2 problems

## Objectives

1. To identify the codes and functions incorporated in the Pandas Library
2. To be able to apply and use the different codes and functions in creating a Python program using a
Pandas Library

## Programming Assignment 3

PA3.1: https://github.com/itzWyntr/ECE2112_PA3_Baas_2ECEB/blob/main/PA3.1.ipynb

PA3.2: https://github.com/itzWyntr/ECE2112_PA3_Baas_2ECEB/blob/main/PA3.2.ipynb

.py Files: 

PA3.1: https://github.com/itzWyntr/ECE2112_PA3_Baas_2ECEB/blob/main/PA3.1.py

PA3.2: https://github.com/itzWyntr/ECE2112_PA3_Baas_2ECEB/blob/main/PA3.2.py

## Table of Contents

Objectives: https://github.com/itzWyntr/ECE2112_PA3_Baas_2ECEB/blob/main/README.md#objectives

Programming Assignment 3: https://github.com/itzWyntr/ECE2112_PA3_Baas_2ECEB/blob/main/README.md#programming-assignment-3

Problems: https://github.com/itzWyntr/ECE2112_PA3_Baas_2ECEB/blob/main/README.md#problems

  Problem 1: https://github.com/itzWyntr/ECE2112_PA3_Baas_2ECEB/blob/main/README.md#problem-1
  
  Problem 2: https://github.com/itzWyntr/ECE2112_PA3_Baas_2ECEB/blob/main/README.md#problem-2

## Problems

### Problem 1:

We are asked to load a .csv file and load the first and last 5 rows

1. Import pandas
```python
import pandas as pd
```

2. Load the .csv file
```python
cars = pd.read_csv('cars.csv')
cars
```

3. Locate the first and last 5 rows. Use concat to combine
```python
display = pd.concat([cars.iloc[0:5],cars.iloc[27:32]])
```

4. Display the result
```python
print("The first and last 5 cars are:")
display
```

### Problem 2: 
Problem 2 is divided into 5 different parts:

a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.

b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.

c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?

d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

Reminder: 

1. Initially, repeat the first 2 steps of problem 1

For a.

I used the code "car.iloc[]" to locate the first 5 odd-numbered columns. The code .iloc[] is used to locate the given integer for row and column index positions
```python
odd_num_rows = cars.iloc[:,::2]
odd_num_rows
```

For b. 
I used the code "cars.loc[]" to locate the model Mazda RX4. The code .loc[] is used to locate the column or row label
```python
cars.loc[cars['Model'] == 'Mazda RX4']
```

For c. 
I used a chained operation of .loc[] and .iloc[] to extract the value of cylinders in Camaro Z28.
```python
cam_cyl = cars.loc[cars['Model']== 'Camaro Z28','cyl'].iloc[0]

print("Cylinders of Camaro Z28: ",cam_cyl)
```
If only .loc[] is used, The result of the code might be 
```
5    8
Name: cyl, dtype: int64
```

For d.
1. I used loc to locate the model, car, cylinder and gear
```python
Mazda = cars.loc[cars["Model"]== 'Mazda RX4 Wag', ['Model','cyl', 'gear']] #For Mazda RX4 Wag
Ford = cars.loc[cars["Model"]== 'Ford Pantera L', ['Model','cyl', 'gear']] #For 'Ford Pantera L'
Honda = cars.loc[cars["Model"]== 'Honda Civic', ['Model','cyl', 'gear']] #For 'Honda Civic'
```
2. Concatantinate (.concat) is used to combine all the results
```python
print("The car's gears and cylinders are: ")
pd.concat([Mazda, Ford, Honda])
```








