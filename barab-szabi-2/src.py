import polars as pl
import pickle

query_df = pl.read_csv("query.csv")
with open("tree.pkl","rb") as file:
    tree = pickle.load(file)
weapons = pl.read_parquet("weapons.parquet")
dist, ind = tree.query(query_df)    
pl.DataFrame({"dist":dist,
            "weapon":weapons[ind]}).write_csv("out.csv")
