import polars as pl

if __name__ == "__main__":
    # Read input data from Parquet file
    df = pl.read_parquet("input.parquet")

    # Read query data from CSV file
    query_df = pl.read_csv("query.csv")

    # Read tree model from Parquet file
    tree = pl.read_parquet("tree.parquet")

    # Perform query using the tree model
    distances, indices = tree.query(query_df, k=1)

    # Convert indices to Polars DataFrame
    indices_df = pl.DataFrame({"indices": indices})

    # Join indices with the original DataFrame to get corresponding "weapon" values
    result_df = df.join(indices_df, on_left="index", on_right="indices", how="inner")[["dist", "weapon"]]

    # Write the result DataFrame to a CSV file
    result_df.write_csv("out.csv")
