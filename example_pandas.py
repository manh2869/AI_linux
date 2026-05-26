import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

os.system("clear")
# x = np.array([1, 2, 3, 4, 5, 6])
# y = np.array([2, 7, 1, -15, 4, 10])

# column_names = """Hours_Studied,Attendance,Parental_Involvement,Access_to_Resources,Extracurricular_Activities,Sleep_Hours,Previous_Scores,Motivation_Level,Internet_Access,Tutoring_Sessions,Family_Income,Teacher_Quality,School_Type,Peer_Influence,Physical_Activity,Learning_Disabilities,Parental_Education_Level,Distance_from_Home,Gender,Exam_Score""".split(
#     ","
# )

pd.set_option("display.max_rows", None)

name_used = [
    "Hours_Studied",
    "Sleep_Hours",
    "Previous_Scores",
    "Learning_Disabilities",
    "Internet_Access",
    "Distance_from_Home",
    "Exam_Score",
]

df = pd.read_csv("/home/woong/study/AI_linux/100_student.csv", usecols=name_used)

# df = df.sort_values(by="Exam_Score", ascending=False)

hours = df["Hours_Studied"]
sleep = df["Sleep_Hours"]
pre_score = df["Previous_Scores"]
score = df["Exam_Score"]

#               ***        clean data           ***

df_clean = df.dropna()  #   delete rows NaN   # print(df_clean.info())

# print(df.duplicated().sum())  sum duplicate
# df_clean = df.drop_duplicates() delete dupliocate

mean_score = df["Exam_Score"].mean()
# print(mean_score)     avegate
# df["Exam_Score"] = df["Exam_Score"].fillna(mean_score)  # fill NaN

# df = df.fillna(df.mean(numeric_only=True))  auto fill mean in colums numeric NaN

# loc str
distan_from_home = ["Near"]
df_loc = df[df["Distance_from_Home"].isin(distan_from_home)]
# print(df_loc)





print(df.isnull().sum())  # is  null  ?


# print(df)
# print(df.info())
# print(df.describe())

# a, b = np.polyfit(hours, score, 1)
# c, d = np.polyfit(sleep, score, 1)
# e, f = np.polyfit(pre_score, score, 1)   line


fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 8))

# ax1.plot(x, a * x + b, color="red", linewidth=2)
# ax1.set_ylim(0, 20)
# ax1.grid(True)

# ax2.plot(x, y, color="red", linewidth=2)
# ax2.grid(True)

# ax1.scatter(hours, score)
# ax1.plot(hours, a * hours + b, color="red", linewidth=2)
# ax1.grid(True)


# ax2.scatter(sleep, score)
# ax2.plot(sleep, c * sleep + d, color="red", linewidth=2)
# ax2.grid(True)


# ax3.scatter(pre_score, score)
# ax3.plot(pre_score, e * pre_score + f, color="red", linewidth=2)
# ax3.plot(np.sort(pre_score), e * np.sort(pre_score) + f, color="red", linewidth=2)
# ax3.grid(True)


# plt.show()
