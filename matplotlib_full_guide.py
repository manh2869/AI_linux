import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ==========================================================
# 1. CHUẨN BỊ DỮ LIỆU (PREPARE DATA)
# ==========================================================
x = np.linspace(0, 10, 100)
y = np.sin(x)

# ==========================================================
# 2. CÁCH 1: PYPLOT API (DÀNH CHO NGƯỜI MỚI / VẼ NHANH)
# ==========================================================
print("--- Đang vẽ bằng Pyplot API ---")
plt.figure(figsize=(8, 4))
plt.plot(x, y, color="blue", linestyle="--", label="Sin(x)")
plt.title("Cách vẽ đơn giản với Pyplot API")
plt.xlabel("Trục X")
plt.ylabel("Trục Y")
plt.legend()
# plt.show() # Bỏ comment nếu muốn xem ngay

# ==========================================================
# 3. CÁCH 2: OBJECT-ORIENTED API (CÁCH CHUYÊN NGHIỆP - TRONG ẢNH CỦA BẠN)
# ==========================================================
print("--- Đang vẽ bằng Object-Oriented API ---")
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, np.cos(x), color="red", label="Cos(x)")

# Tùy chỉnh bằng phương thức .set()
ax.set(title="Cách vẽ chuyên nghiệp (OO API)",
       xlabel="Thời gian",
       ylabel="Giá trị",
       xlim=(0, 10),
       ylim=(-1.5, 1.5))
ax.legend()
ax.grid(True, linestyle=':', alpha=0.6)
# plt.show()

# ==========================================================
# 4. CÁC LOẠI BIỂU ĐỒ PHỔ BIẾN (COMMON PLOTS)
# ==========================================================
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))

# 4.1. Line Plot
ax1.plot(x, x**2, color="purple")
ax1.set_title("Line Plot (x^2)")

# 4.2. Scatter Plot
ax2.scatter(np.random.randn(50), np.random.randn(50), color="green", alpha=0.6)
ax2.set_title("Scatter Plot (Ngẫu nhiên)")

# 4.3. Bar Plot (Biểu đồ cột)
data = {"Apple": 10, "Banana": 15, "Orange": 8}
ax3.bar(data.keys(), data.values(), color="orange")
ax3.set_title("Bar Plot (Trái cây)")

# 4.4. Histogram (Biểu đồ tần suất)
random_data = np.random.normal(0, 1, 1000)
ax4.hist(random_data, bins=30, color="skyblue", edgecolor="black")
ax4.set_title("Histogram (Phân phối chuẩn)")

plt.tight_layout() # Tự động căn chỉnh để không bị đè chữ
# plt.show()

# ==========================================================
# 5. LƯU BIỂU ĐỒ (SAVING FIGURES)
# ==========================================================
fig.savefig("matplotlib_comprehensive_guide.png")
print("Đã lưu biểu đồ tổng hợp vào file: matplotlib_comprehensive_guide.png")

print("\n--- HOÀN THÀNH ---")
print("Lưu ý: Bạn có thể bỏ comment '#' trước các lệnh 'plt.show()' để xem biểu đồ hiện lên màn hình.")
