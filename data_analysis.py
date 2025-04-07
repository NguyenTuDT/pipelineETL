import matplotlib.pyplot as plt
from dataframe import df_final  

# --- Vẽ biểu đồ cột ---
plt.figure(figsize=(10, 6))
bars = plt.bar(df_final['TenSP'], df_final['TotalSold'], color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'])

# --- Tuỳ chỉnh giao diện ---
plt.title('TOP 5 SẢN PHẨM BÁN CHẠY', fontsize=14, fontweight='bold', pad=20)
plt.xlabel('Tên sản phẩm', fontsize=12)
plt.ylabel('Tổng số lượng bán', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.3)

# --- Hiển thị giá trị trên cột ---
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{int(height)}', ha='center', va='bottom')

plt.tight_layout()
plt.show()