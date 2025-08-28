reviews.head()
#=====1=====
# Your code here
renamed = reviews.rename(columns={'region_1' : 'region', 'region_2' : 'locale'})

# Check your answer
q1.check()

#=====2=====
reindexed = reviews.rename_axis("wines", axis="columns")

# Check your answer
q2.check()

#=====3=====
gaming_products = pd.read_csv("../input/things-on-reddit/top-things/top-things/reddits/g/gaming.csv")
gaming_products['subreddit'] = "r/gaming"
movie_products = pd.read_csv("../input/things-on-reddit/top-things/top-things/reddits/m/movies.csv")
movie_products['subreddit'] = "r/movies"

combined_products = pd.concat([gaming_products, movie_products])

# Check your answer
q3.check()

#=====4=====
left = powerlifting_meets.set_index(['MeetID'])
right = powerlifting_competitors.set_index(['MeetID'])


powerlifting_combined = left.join(right, lsuffix='_meets', rsuffix='_competitors')

# Check your answer
q4.check()