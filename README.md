# pipelineETL
graph TD
    A[Tạo df_products] --> B[Tạo df_orders ngẫu nhiên]
    B --> C[Nhóm theo MaSP]
    C --> D[Ghép với df_products]
    D --> E[Vẽ biểu đồ]
