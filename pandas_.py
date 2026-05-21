import pandas
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


collum_names = """Hours_Studied,Attendance,Parental_Involvement,Access_to_Resources,Extracurricular_Activities,Sleep_Hours,Previous_Scores,Motivation_Level,Internet_Access,Tutoring_Sessions,Family_Income,Teacher_Quality,School_Type,Peer_Influence,Physical_Activity,Learning_Disabilities,Parental_Education_Level,Distance_from_Home,Gender,Exam_Score""".split(
    ","
)
collum_used = [
    "Hours_Studied",
    "Attendance",
    "Sleep_Hours",
    "Previous_Scores",
    "Access_to_Resources",
    "Exam_Score",
]


df = pandas.read_csv(
    "/home/woong/study/AI_linux/student.csv", names=collum_names, usecols=collum_used
)
df["Exam_Score"] = pandas.to_numeric(df["Exam_Score"], errors="coerce")
df["Hours_Studied"] = pandas.to_numeric(df["Hours_Studied"], errors="coerce")

# score=df.sort_values(by='Exam_Score',ascending=False)

# print(score)
# print(df.describe())

# study_hard = df[df["Hours_Studied"] > 30]
# study_less = df[df["Hours_Studied"] < 30]


# print(study_hard["Exam_Score"].mean())
# print(study_less["Exam_Score"].mean())


high_exam = df[df["Exam_Score"] > 90]
print(high_exam["Hours_Studied"].mean())
low_exam = df[(df["Exam_Score"] < 70) & (df["Exam_Score"] > 60)]
print(low_exam["Hours_Studied"].mean())
