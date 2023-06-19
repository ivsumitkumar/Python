#step 1: import library
import pandas as pd

#step 2: import data
df = pd.read_csv(r"F:/Study/Programs/Dataset/Boston.csv")

# print(df.head())
# print(df.columns)

#steo 3: define y and x
y=df[ 'MEDV']
x=df[['CRIM', 'ZN', 'INDUS', 'CHAS', 'NX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX',
       'PTRATIO', 'B', 'LSTAT']]

# print(y.shape)
# print(x.shape)

#step 4: split data into train and test sample
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,train_size=0.7, random_state=2529)

#step 5: choose the model
from sklearn.linear_model import LinearRegression
model = LinearRegression()

#step 6: train model
model.fit(x_train,y_train)

#Intercecp
# print(model.intercept_)

#Slope
# print(model.coef_)

#step 7: Predict Model
y_pred = model.predict(x_test)

#step 8: Check accuracy of model
from sklearn.metrics import mean_absolute_error, r2_score
print(mean_absolute_error(y_test,y_pred))
accuracy = r2_score(y_test,y_pred)*100
print("Accuracy of the model is %.2f"%accuracy)