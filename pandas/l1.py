import pandas as pd

#1
# Your code goes here. Create a dataframe matching the above diagram and assign it to the variable fruits.
fruits = pd.DataFrame({'Apples': [30], 'Bananas': [21]})

# Check your answer
q1.check()
fruits

#2
# Your code goes here. Create a dataframe matching the above diagram and assign it to the variable fruit_sales.
fruit_sales = pd.DataFrame({'Apples': [35, 41], 'Bananas': [21, 34]}, index=['2017 Sales', '2018 Sales'])

# Check your answer
q2.check()
fruit_sales

#3
ingredients = pd.Series(['4 cups', '1 cup', '2 large', '1 can'], index=['Flour', 'Milk', 'Eggs', 'Spam'], name='Dinner')

# Check your answer
q3.check()
ingredients

#4
reviews = pd.read_csv('../input/wine-reviews/winemag-data_first150k.csv', index_col=0)

# Check your answer
q4.check()
reviews

#5
sample_reviews = reviews.iloc[[0,1,2,4,7],0:]

# Check your answer
q5.check()
sample_reviews
# Solution:
# indices = [1, 2, 3, 5, 8]
# sample_reviews = reviews.loc[indices]

#6
df = reviews.loc[[0,1,10,100], ['country', 'province', 'region_1', 'region_2']]

# Check your answer
q6.check()
df

#7
df = reviews.loc[:99,['country', 'variety']]

# Check your answer
q7.check()
df

#8
italian_wines = reviews.loc[reviews.country.isin(['Italy'])]

# Check your answer
q8.check()

#9
top_oceania_wines = reviews.loc[((reviews.country == 'Australia') | (reviews.country == 'New Zealand')) & (reviews.points >=95)] 

# Check your answer
q9.check()
top_oceania_wines