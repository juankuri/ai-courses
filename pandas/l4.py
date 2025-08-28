#1===========
# Your code here
reviews_written = reviews.groupby('taster_twitter_handle').taster_twitter_handle.count()
print(reviews_written)

# Check your answer
q1.check()

#2===========
s = reviews.groupby("price")["points"].max()
print(s)


best_rating_per_price = s.sort_index()
print(best_rating_per_price)
# Check your answer
q2.check()

#3===========
min_price = reviews.groupby("variety")["price"].min()
max_price = reviews.groupby("variety")["price"].max()
# print(max_price)
# values = [[min_price, max_price]]
# index = ['min', "max"]

# print(values)
price_extremes = pd.DataFrame({
    "min": min_price,
    "max": max_price
})

print(price_extremes)
# Check your answer
q3.check()

#4===========
sorted_varieties = price_extremes.sort_values(by=["min", "max"], ascending = False)

# Check your answer
q4.check()

#5===========
reviewer_mean_ratings = reviews.groupby("taster_name").points.mean()

# Check your answer
q5.check()

#6===========
count = reviews.groupby(["country", "variety"]).size()
country_variety_counts = count.sort_values(ascending = False)

# Check your answer
q6.check()