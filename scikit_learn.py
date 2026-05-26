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

imputer = SimpleImputer(missing_values=np.nan, strategy="mean")  # set up strategy
imputer.fit(x[:, 0:1])  # calulator data
x[:, 0:1] = imputer.transform(x[:, 0:1])  #   find NaN and replace


le = LabelEncoder()
x[:, 4] = le.fit_transform(x[:, 4])
# print(gender.classes_)  check male = 0  ?   1

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

# fig, ax1 = plt.subplots(figsize=(10, 10))
# ax1.scatter(df.iloc[:, 0:1], df.iloc[:, -1])
# ax1.grid()
# plt.show()


print(x_train[0:5, :])
# print(y_train)
# print(x_test)
# print(y_test)

sc = StandardScaler()

x_train[:, 0:4] = sc.fit_transform(x_train[:, 0:4])

# x_test[:, 0:5] = sc.fit_transform(x_test[:, 0:5])


# y_train =sc.fit_transform(y_train)
print(x_train[0:5, :])

# print(x_test)
print("deviation   ", sc.scale_)  # [deviation,...,...,]
print("mean  ", sc.mean_)  # [mean.,...,...,...,]

# print(df.isnull().sum())
model = LinearRegression()
model.fit(x_train, y_train)

print(model)
# 4. Dự đoán và Đánh giá (Evaluation)
# y_pred = model.predict(x_test)

# mse = mean_squared_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)
# print(f"--- KẾT QUẢ MÔ HÌNH ---")
# print(f"Mean Squared Error: {mse:.2f}")
# print(f"R-squared (Độ chính xác): {r2:.2f}")
# plt.figure(figsize=(8, 6))
# plt.scatter(y_test, y_pred, color='blue', alpha=0.6)
# plt.plot([y_test.min(), y_test.max()], [y_test.min(),
#     y_test.max()], 'r--', lw=2)
# plt.xlabel("Điểm Thực Tế")
# plt.ylabel("Điểm Dự Đoán")
# plt.title("So Sánh: Thực Tế vs Dự Đoán (Scikit-learn)")
# plt.grid(True)
# plt.show()

# # 6. Thử dự đoán cho chính bạn!
# # Giả sử: Học 20h, Chuyên cần 90%, Ngủ 7h, Điểm kì trước 85, Giới
#     # tính 1 (Male)
# my_data = sc.transform([[20, 90, 7, 85, 1]])
# predicted_score = model.predict(my_data)
# print(f"\nNếu bạn học 20h và có các chỉ số trên, dự đoán điểm là:{predicted_score[0]:.2f}")
