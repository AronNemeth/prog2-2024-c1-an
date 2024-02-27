import pandas as pd

df = pd.read_feather("out.feather")
df.to_csv("out.csv", index=False)
