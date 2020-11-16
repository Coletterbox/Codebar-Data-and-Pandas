csv_file = 'taxi-01-2020-sample.csv.xz'

from os import path
path.getsize(csv_file) / (1024*1024)

import pandas as pd

df = pd.read_csv(csv_file)

df.columns

df.head(5)

time_cols = ['tpep_pickup_datetime', 'tpep_dropoff_datetime']
df = pd.read_csv(csv_file, parse_dates=time_cols)

df.dtypes

df.sample(5)

type(df), type(df['VendorID'])
