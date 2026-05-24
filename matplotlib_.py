import matplotlib.pyplot as plt
from matplotlib.axes import Axes
import numpy as np
import pandas as pd
import os

os.system("clear")

# x = [1, 2, 3, 4]
# y1 = [64, 43, 9, 16]
# y2 = [23, 2, 32, 16]

# plt.plot(x, y1, color="blue", label="y1") bieu do duong
# plt.plot(x, y2, color="red", label="y2")

# x = [1, 2, 3, 4, 5, 6]
# y = [45, 55, 68, 70, 85, 92]

# plt.figure(figsize=(10, 10))

# alpha = numpy.linspace(0, 2*numpy.pi, 100)


# x=10*numpy.cos(alpha)
# y=10*numpy.sin(alpha)
# # y1=numpy.cos(x)

# plt.plot(x, y, color="red")
# plt.plot(x, -y, color="blue")

column_names = """Hours_Studied,Attendance,Parental_Involvement,Access_to_Resources,Extracurricular_Activities,Sleep_Hours,Previous_Scores,Motivation_Level,Internet_Access,Tutoring_Sessions,Family_Income,Teacher_Quality,School_Type,Peer_Influence,Physical_Activity,Learning_Disabilities,Parental_Education_Level,Distance_from_Home,Gender,Exam_Score""".split(
    ","
)
column_used = [
    "Hours_Studied",
    "Attendance",
    "Sleep_Hours",
    "Previous_Scores",
    "Access_to_Resources",
    "Exam_Score",
]


df = pd.read_csv(
    "/home/woong/study/AI_linux/student.csv",
    names=column_names,
    usecols=column_used,
    skiprows=1,
)

# print(df_small)

# score=df.sort_values(by='Exam_Score',ascending=False)
# df["Hours_Studied"] = pandas.to_numeric(df["Hours_Studied"], errors="coerce")

df_small = df.sample(100)

# print(df_small[["Hours_Studied", "Exam_Score"]])

hours = df_small["Hours_Studied"]
score = df_small["Exam_Score"]

hours = pd.to_numeric(hours, errors="coerce")
score = pd.to_numeric(score, errors="coerce")

df_small = df_small.sort_values(by="Hours_Studied")


fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(10, 6))


ax1.scatter(hours, score)
ax2.scatter(hours, score)
ax3.scatter(hours, score)


# ax.scatter(hours, score, color='royalblue', alpha=0.7, edgecolors='white', label="Dữ liệu mẫu")
# ax.hexbin(df_small["Hours_Studied"], df_small["Exam_Score"], gridsize=30, cmap='Blues') chia đồ thị thành các ô tổ ong

# Tùy chỉnh bằng phương thức 'set_'
ax1.set_ylabel("Score")
ax1.set_xlabel("Hours")
ax1.set_title("oh shit")

ax1.legend()
ax1.grid(True, linestyle="--", alpha=0.5)

plt.show()
