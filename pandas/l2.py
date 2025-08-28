#1
# Your code here
desc = reviews.description

# Check your answer
q1.check()

#2
first_description = reviews.description[0]

# Check your answer
q2.check()
first_description

#3
first_row = reviews.iloc[0] #because its a DAtaFrame, we use iloc to get the first row

# Check your answer
q3.check()
first_row

#4
first_descriptions = reviews['description'][:10]

# Check your answer
q4.check()
first_descriptions
    #Solution:
    #first_descriptions = reviews.description.iloc[:10]
    #Note that many other options will return a valid result, such as desc.head(10) and reviews.loc[:9, "description"].

#5
