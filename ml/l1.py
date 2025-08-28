#=====1=====
import pandas as pd

# Path of the file to read
iowa_file_path = '../input/home-data-for-ml-course/train.csv'

# Fill in the line below to read the file into a variable home_data
home_data = pd.read_csv(iowa_file_path)

# Call line below with no argument to check that you've loaded the data correctly
step_1.check()

#=====2=====
# What is the average lot size (rounded to nearest integer)?
avg_lot_size = round(10516.828082)

# As of today, how old is the newest home (current year - the date in which it was built)
newest_home_age = 2025 - 2010

# Checks your answers
step_2.check()

