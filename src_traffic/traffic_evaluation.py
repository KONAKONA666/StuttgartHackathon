import pandas as pd
import numpy as np
import glob


files = glob.glob("../data/traffic/*.xls")

all_data = pd.DataFrame()

for f in files:
    df = pd.read_excel(f)
    all_data = all_data.append(df, ignore_index=True)
    ## Problem is that it makes one big data frame but maybe it's to big so it makes nan as

print(all_data)