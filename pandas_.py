import pandas
import numpy as np
import matplotlib.pyplot as plt
import os

os.system("clear")
# df = pandas.read_csv("data.csv", names=["stt", "name", "old", "point"])

# print(df)
# print(df.head(1)) xem n dong dau
# print(df.tail(2)) xem n dong cuoi
# print(df.info()) xem kieu du lieu cua tung cot
# print(df.describe())
# print(df.loc[2]) xem dong 2
# print(df.loc[:2])  xem tu dong 0 -> 2
# x = df.iloc[0:5,1] xem collum


# df['new_collum']=df['old']+10         them cot
# df['sex']='NaN'                      them cot


# x = df.groupby("name")["old"].sum()
# x=x.sort_values(ascending=False)
# print(x)

pandas.set_option("display.max_columns", None)  # Không giới hạn số lượng cột hiển thị
pandas.set_option("display.max_rows", None)
pandas.set_option("display.width", 1000)


# column_names = """Hours_Studied,Attendance,Parental_Involvement,Access_to_Resources,Extracurricular_Activities,Sleep_Hours,Previous_Scores,Motivation_Level,Internet_Access,Tutoring_Sessions,Family_Income,Teacher_Quality,School_Type,Peer_Influence,Physical_Activity,Learning_Disabilities,Parental_Education_Level,Distance_from_Home,Gender,Exam_Score""".split(
#     ","
# )
column_used = [
    "Hours_Studied",
    "Sleep_Hours",
    "Exam_Score",
]


df = pandas.read_csv(
    "/home/woong/study/AI_linux/student.csv",
    usecols=column_used,
)


df["Exam_Score"] = pandas.to_numeric(df["Exam_Score"], errors="coerce")
df["Hours_Studied"] = pandas.to_numeric(df["Hours_Studied"], errors="coerce")
df["Sleep_Hours"] = pandas.to_numeric(df["Sleep_Hours"], errors="coerce")

df_small = df.sample(100, random_state=28)
df_sorted = df_small.sort_values(by="Exam_Score", ascending=False)


x = df_sorted["Sleep_Hours"]
x1 = df_sorted["Hours_Studied"]

y = df_sorted["Exam_Score"]

m, b = np.polyfit(x, y, 1)
m1, b1 = np.polyfit(x1, y, 1)

# print(df_sorted.info())
# print(df_sorted.describe())

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))

ax1.scatter(df_sorted["Sleep_Hours"], df_sorted["Exam_Score"])
ax1.plot(x, m * x + b, color="red", linewidth=2)
ax1.grid(True, linestyle="--", alpha=0.6    )


ax2.scatter(df_sorted["Hours_Studied"], df_sorted["Exam_Score"])
ax2.plot(x1, m1 * x1 + b1, color="red", linewidth=2)
ax2.grid(True, linestyle="--", alpha=0.6)


plt.show()

# score=df.sort_values(by='Exam_Score',ascending=False)

# print(score)

# study_hard = df[df["Hours_Studied"] > 30]
# study_less = df[df["Hours_Studied"] < 30]
# print(study_hard["Exam_Score"].mean())
# print(study_less["Exam_Score"].mean())


# high_exam = df[df["Exam_Score"] > 90]
# print(high_exam["Hours_Studied"].mean())
# low_exam = df[(df["Exam_Score"] < 70) & (df["Exam_Score"] > 60)]
# print(low_exam["Hours_Studied"].mean())
