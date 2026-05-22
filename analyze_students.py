import pandas as pd
import matplotlib.pyplot as plt

# 1. Đọc dữ liệu
df = pd.read_csv("/home/woong/study/AI_linux/student.csv")

# --- Yêu cầu 1: Thống kê cơ bản ---
print("--- 1. Thống kê cơ bản các cột số ---")
stats = df.describe()
print(stats)
print("\n")

# --- Yêu cầu 2: Mối liên hệ giữa Hours_Studied và Exam_Score ---
correlation = df["Hours_Studied"].corr(df["Exam_Score"])
print(f"--- 2. Mối liên hệ ---")
print(f"Hệ số tương quan giữa số giờ học và điểm thi: {correlation:.4f}")
if correlation > 0.7:
    print("Nhận xét: Có mối tương quan thuận rất mạnh.")
elif correlation > 0.4:
    print("Nhận xét: Có mối tương quan thuận vừa phải.")
else:
    print("Nhận xét: Mối tương quan yếu.")
print("\n")

# --- Yêu cầu 3: Vẽ biểu đồ phân bố điểm thi ---
print("--- 3. Đang tạo biểu đồ phân bố điểm thi... ---")
plt.figure(figsize=(10, 6))
plt.hist(df["Exam_Score"], bins=30, color="skyblue", edgecolor="black", alpha=0.7)
plt.title("Phân bố điểm thi (Exam Score Distribution)")
plt.xlabel("Điểm thi")
plt.ylabel("Số lượng sinh viên")
plt.grid(axis="y", alpha=0.3)

# Lưu biểu đồ ra file
output_chart = "exam_score_dist.png"
plt.savefig(output_chart)
print(f"Biểu đồ đã được lưu tại: {output_chart}")
