import pandas as pd
import os
import time

chunk_size = 1
batch_no = 1

for chunk in pd.read_csv('sp-old-2021-08.csv', chunksize=30000):
    chunk.to_csv('sp-old-2021-08_' + '00'+str(batch_no)+'.csv', index=False)
    batch_no += 1
    time.sleep(1)
