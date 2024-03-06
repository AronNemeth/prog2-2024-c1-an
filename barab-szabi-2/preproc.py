import polars as pl
from scipy import spatial
import pickle

df = pl.read_csv("input.csv")
df = df.rename({df.columns[2]:"y"})
tree = spatial.KDTree(df[["x","y"]],leafsize=10000)
with open("tree.pkl","wb") as file:
    pickle.dump(tree, file)
df.select("weapon").write_parquet("weapons.parquet")
