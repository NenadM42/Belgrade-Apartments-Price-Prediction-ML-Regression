import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn import preprocessing, model_selection ,svm
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge

from sklearn.ensemble import GradientBoostingRegressor
from sklearn import ensemble


source = 'RealEstateBelgrade.csv'
data = pd.read_csv(source)

y = data.Price
X = data.drop(['Price','ID','Address'],axis = 1)

X["No_of_rooms"] = X["No_of_rooms"].replace("5+","6")

#for i in range(0,len(y)):
#    y[i] = y[i].replace('.','')
    
#print(y)
"""
for i in range(0,len(X)):
    if(X.loc[i][1] == '6'):    
        print(X.loc[i])
    """
#print(y)
        
#print(X.loc[1][0])
    
#print(X.head())

#print(X.tail())

X_train,X_test,y_train,y_test = train_test_split(X,y,
                                                 test_size = 0.3,
                                                 random_state=314
                                                 )

#clf = LinearRegression()
clf = LinearRegression()

clf.fit(X_train,y_train)

accuracy = clf.score(X_test,y_test)

print(accuracy)


#X_train_scaled = preprocessing.scale(X_train)
#print(X_train_scaled)