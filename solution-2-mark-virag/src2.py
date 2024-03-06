import polars as pl
from scipy import spatial


query_df = pl.read_csv("query.csv").to_pandas()  
df = pl.read_parquet("input.parquet").to_pandas()


tree = spatial.cKDTree(df.iloc[:, [1, 2]])


distances, indices = tree.query(query_df.iloc[:, [0, 1]], k=1)


out_df = pl.DataFrame({
    "dist": distances,
    "weapon": df.iloc[indices, df.columns.get_loc("weapon")].values
})

out_df.write_csv("out.csv")