import polars as pl
from scipy.spatial import KDTree
import pickle


if __name__ == "__main__":
    df = pl.read_csv("input.csv")
    df = df.rename({df.columns[2]:"y"})

    tree = KDTree(df[["x", "y"]])

    df = df.select("weapon")
    df.write_parquet("weapons.parquet")

    with open("tree.pkl", "wb") as file:
        pickle.dump(tree, file)
