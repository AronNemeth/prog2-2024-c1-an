import polars as pl
import pickle


if __name__ == "__main__":
    df = pl.read_parquet("weapons.parquet")
    query_df = pl.read_csv("query.csv")

    with open("tree.pkl", "rb") as file:
        tree = pickle.load(file)

    distances, indices = tree.query(query_df, k=1)

    weapon_values = df[indices]

    pl.DataFrame({"dist": distances, "weapon": weapon_values}).write_csv("out.csv")
