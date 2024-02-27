import pandas as pd
import numpy as np
from scipy.spatial import distance
import pyarrow.feather as feather


if __name__ == "__main__":
    df = pd.read_pickle("input.pkl")
    query_df = pd.read_csv("query.csv")

    input_values = df[["x", "y"]].values
    query_values = query_df.values

    diffs = distance.cdist(input_values, query_values, metric="sqeuclidean")

    min_indices = np.argmin(diffs, axis=0)
    min_distances = np.min(diffs, axis=0)

    weapon_values = df.iloc[min_indices]["weapon"].values

    out_df = pd.DataFrame({"dist": min_distances, "weapon": weapon_values})

    pd.DataFrame(out_df).to_feather("out.feather")
