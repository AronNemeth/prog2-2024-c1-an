import pandas as pd
import pyarrow.parquet as pq
from scipy.spatial import KDTree

if __name__ == "__main__":
    # Read input data from CSV file
    df = pd.read_csv("input.csv")

    # Convert DataFrame to Parquet and save it
    table = pq.Table.from_pandas(df)
    pq.write_table(table, "input.parquet")

    # Build tree
    tree = KDTree(df[["x", "y"]])

    # Save tree as Parquet
    tree_df = pd.DataFrame(tree.data)
    tree_table = pq.Table.from_pandas(tree_df)
    pq.write_table(tree_table, "tree.parquet")
