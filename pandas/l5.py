#=====1=====
# Your code here
dtype = reviews.points.dtype

# Check your answer
q1.check()

#=====2=====
point_strings = reviews.points.astype('str')

# Check your answer
q2.check()

#=====3=====
n_missing_prices = pd.isnull(reviews["price"]).sum()


# Check your answer
q3.check()

#=====4=====
reviews_per_region = reviews.region_1.fillna("Unkwon").value_counts().sort_values(ascending=False)

# Check your answer
q4.check()
