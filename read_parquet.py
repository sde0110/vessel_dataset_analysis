import pandas as pd

# 파일 경로
file_path = "2011_NOAA_AIS_logs_11.parquet"

# Parquet 파일 읽기
df = pd.read_parquet(file_path)

# 데이터 확인
print(df.sample(5))
