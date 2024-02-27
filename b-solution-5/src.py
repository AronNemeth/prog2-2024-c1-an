import pandas as pd
from scipy.spatial import KDTree
import json

if __name__ == "__main__":
    # Read DataFrame from JSON file
    df = pd.read_json("input.json")

    # Read query DataFrame from CSV file
    query_df = pd.read_csv("query.csv")

    # Extract coordinates from DataFrames
    input_coords = df[["x", "y"]].values
    query_coords = query_df[["x", "y"]].values

    # Load KDTree from JSON file
    with open("tree.json", "r") as file:
        tree_data = json.load(file)
        tree = KDTree(tree_data["data"])
        tree.idx_array = tree_data["idx_array"]
        tree.maxes = tree_data["maxes"]
        tree.mins = tree_data["mins"]
        tree.leafsize = tree_data["leafsize"]

    # Query KDTree
    distances, indices = tree.query(query_coords, k=1)

    # Extract weapon values
    weapon_values = df.iloc[indices.flatten()]["weapon"].values

    # Create output DataFrame
    out_df = pd.DataFrame({"dist": distances.flatten(), "weapon": weapon_values})

    # Save output DataFrame to feather format
    out_df.to_feather("out.feather")
