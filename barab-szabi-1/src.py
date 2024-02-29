import polars as pl
from scipy import spatial


query_df = pl.read_csv("query.csv")
df = pl.read_parquet("input.parquet")
tree = spatial.KDTree(df[["x","y"]])
out = []
for row in query_df.iter_rows():
    out.append({"dist": tree.query(row)[0], 
                "weapon": df[int(tree.query(row)[1])]["weapon"].item()})
pl.DataFrame(out).write_csv("out.csv")
