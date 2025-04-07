import pymysql as _mysql_connector 
import pandas as pd  

def extract_data_from_csv(file_path):
    return pd.read_csv(file_path)  

def transform_data(df):
    df['TongTien'] = df['TongTien'].astype(float)  
    return df

def load_data(df, table_name):
    try:
        conn = _mysql_connector.connect(
            host='localhost',
            user='ntu_admin',
            password='Nguyenvantu2005@',
            database='retail_company'
        )
        cursor = conn.cursor()

        cursor.execute("SET SESSION FOREIGN_KEY_CHECKS=0")  # Dùng SESSION scope
        conn.commit()
        
        # Insert hóa đơn
        for _, row in df.iterrows():
            cursor.execute(f"INSERT INTO {table_name} (MaKH, NgayHD, TongTien ) VALUES (%s, %s, %s)",  (row['MaKH'], row['NgayHD'], row['TongTien']))
        
        cursor.execute("SET SESSION FOREIGN_KEY_CHECKS=0")  # Dùng SESSION scope
        conn.commit()
        
        conn.commit()
        print("Thành công!")
        
    except _mysql_connector.Error as err:
        print(f"Lỗi MySQL: {err}")
        conn.rollback()
    finally:
        if conn.open:
            conn.close()

if __name__ == "__main__":
    # Thực thi pipeline
    product_data = extract_data_from_csv('hoadon.csv')  
    clean_data = transform_data(product_data)  
    load_data(clean_data, 'hoadon') 
   
