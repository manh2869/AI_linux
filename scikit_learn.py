import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

import os

os.system("clear")


df = pd.read_csv("/home/woong/study/AI_linux/selected_columns.csv", index_col=0)


mean_score = df["Exam_Score"].mean()
# mean_studied = df["Hours_Studied"].mean()


df["Exam_Score"] = df["Exam_Score"].fillna(mean_score)
# df["Hours_Studied"] = df["Hours_Studied"].fillna(mean_studied)

x = df.iloc[:, :-1].values
y = df.iloc[:, -1].values


# new_student = [22.0, 88, 10, 72, "Fmale"]
# new_df = pd.DataFrame(new_student)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)


imputer = SimpleImputer(missing_values=np.nan, strategy="mean")  # set up strategy
imputer.fit(x_train[:, 0:1])  # calulator data
x_train[:, 0:1] = imputer.transform(x_train[:, 0:1])  #   find NaN and replace
x_test[:, 0:1] = imputer.transform(x_test[:, 0:1])  #   find NaN and replace


le = LabelEncoder()
x_train[:, 4] = le.fit_transform(x_train[:, 4])
x_test[:, 4] = le.fit_transform(x_test[:, 4])


# print(gender.classes_)  check male = 0  ?   1


# print(x_train[0:5, :])
# # print(y_train)
# # print(x_test)
# # print(y_test)

sc = StandardScaler()  #   object  sc include mean,deviation...

#       use sc  for caculater   mean,deviation,variance
#       ex   print(sc.mean_)

# sc.fit(x_train)   and   x_train=sc.transform(x_train)   =  sc.fit_transform()


x_train[:, 0:4] = sc.fit_transform(x_train[:, 0:4])

x_test[:, 0:4] = sc.transform(x_test[:, 0:4])


model = LinearRegression()
model.fit(x_train, y_train)


y_predict = model.predict()


# print(model.coef_)  # he so cua line Regression
# print(model.intercept_)  # he so tu do  bias -  intercept

# print("x test", x_test[0:5, :])

print("y_predict    ", y_predict)


# mse = mean_squared_error(y_test, y_predict)
# r2 = r2_score(y_test, y_predict)
#   ???
# print(mse)
# print(r2)

# print("deviation   ", sc.scale_)  # [deviation,...,...,]
# print("mean  ", sc.mean_)  # [mean.,...,...,...,]
