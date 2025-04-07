import pandas as pd
import random
from datetime import datetime, timedelta

# --- Tạo dữ liệu sản phẩm ---
products = {
    'MaSP': ['SP001', 'SP002', 'SP003', 'SP004', 'SP005'],
    'TenSP': ['iPhone 15', 'Samsung Galaxy S23', 'MacBook Pro', 'AirPods Pro', 'Apple Watch'],
    'DonGia': [25.5, 18.2, 42.0, 7.5, 12.8]  # Đơn vị: triệu đồng
}
df_products = pd.DataFrame(products)

# --- Tạo dữ liệu hóa đơn chi tiết (CT_HOADON) ---
data = []
for _ in range(100):  # 100 bản ghi
    random_product = random.choice(df_products['MaSP'].values)
    data.append({
        'MaHD': 'HD' + str(random.randint(1000, 9999)),
        'MaSP': random_product,
        'SoLuong': random.randint(1, 5),
        'NgayHD': (datetime.now() - timedelta(days=random.randint(1, 30))).strftime('%Y-%m-%d')
    })

df_orders = pd.DataFrame(data)

# --- Tính tổng số lượng bán ---
df_sales = df_orders.groupby('MaSP')['SoLuong'].sum().reset_index()
df_sales.columns = ['MaSP', 'TotalSold']

# Kết hợp với tên sản phẩm
df_final = pd.merge(df_sales, df_products, on='MaSP')
print("Dữ liệu mẫu:")
print(df_final.head())