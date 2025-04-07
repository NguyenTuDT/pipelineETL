import sys
print("Python path:", sys.executable)

try:
    import pandas as pd
    print("Pandas version:", pd.__version__)
except ImportError:
    print("Lỗi: Không tìm thấy pandas!")
