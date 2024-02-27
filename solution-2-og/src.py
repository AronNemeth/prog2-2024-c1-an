import pandas as pd
import numpy as np
from scipy.spatial import distance

if __name__ == "__main__":
    df = pd.read_pickle("input.pkl")
    query_df = pd.read_csv("query.csv")

    input_values = df[["x", "y"]].values
    query_values = query_df.values

    diffs = distance.cdist(input_values, query_values, metric="euclidean")

    min_indices = np.argmin(diffs, axis=0)  # Lehet nem az 0 kéne az axis-nál?
    min_distances = np.min(diffs, axis=0)

    weapon_values = df.iloc[min_indices]["weapon"].values

    out_df = pd.DataFrame({"dist": min_distances, "weapon": weapon_values})
    out_df.to_csv("out.csv", index=False)
