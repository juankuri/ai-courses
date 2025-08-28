import pandas as pd

#1
median_points = reviews.points.median()
print(median_points)

# Check your answer
q1.check()

#2
countries = reviews.country.unique()

# Check your answer
q2.check()

#3
reviews_per_country = reviews.country.value_counts()

# Check your answer
q3.check()

#4
reviews_price_mean = reviews.price.mean()
centered_price  = reviews.price - reviews_price_mean

# Check your answer
q4.check()

#5
bargain_idx = (reviews.points / reviews.price).idxmax()
bargain_wine = reviews.loc[bargain_idx, 'title']

#6
# ???????????????????????????
# 
# def count_true_booleans_sum (bool_list):
#     return sum(bool_list)
    
# reviews_tropical = count_true_booleans_sum(reviews.description.map(lambda d: 'tropical' in d))

# reviews_fruity = count_true_booleans_sum(reviews.description.map(lambda d: 'fruity' in d))

# descriptor_counts = pd.Series([reviews_fruity, reviews_tropical], 
#                               index=['fruity', 'tropical'])
# print(descriptor_counts) 
# 
# ???????????????????????????
# Check your answer

n_trop = reviews.description.map(lambda desc: "tropical" in desc).sum()
n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
descriptor_counts = pd.Series([n_trop, n_fruity], index=['tropical', 'fruity'])

print(descriptor_counts)

q6.check()

#7
def star_points (row):
    if row.points >= 95:
        return 3
    elif row.points >=85:
        return 2
    else: 
        return 1


star_ratings = reviews.apply(star_points, axis = 'columns')

# Check your answer
q7.check()