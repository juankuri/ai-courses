#=====1=====
y = home_data.SalePrice

# Check your answer
step_1.check()

#=====2=====
# Create the list of features below
feature_names = [
    'LotArea',
    'YearBuilt',
    '1stFlrSF',
    '2ndFlrSF',
    'FullBath',
    'BedroomAbvGr',
    'TotRmsAbvGrd'
]

# Select data corresponding to features in feature_names
X = home_data[feature_names]

# Check your answer
step_2.check()

#=====3=====
from sklearn.tree import DecisionTreeRegressor
#specify the model. 
#For model reproducibility, set a numeric value for random_state when specifying the model
iowa_model = DecisionTreeRegressor(random_state=11)

# Fit the model
iowa_model.fit(X, y)

# Check your answer
step_3.check()

#=====4=====
predictions = iowa_model.predict(X)
print(predictions)

# Check your answer
step_4.check()

#=====5=====
