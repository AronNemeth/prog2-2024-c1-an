import pandas as pd
from scipy.spatial import KDTree
import json

if __name__ == "__main__":
    df = pd.read_csv("input.csv")

    tree = KDTree(df[["x", "y"]].values)

    # Convert KD tree to a JSON-compatible dictionary
    tree_dict = {
        "data": tree.data.tolist(),
        "idx_array": tree.idx_array.tolist(),
        "maxes": tree.maxes.tolist(),
        "mins": tree.mins.tolist(),
        "leafsize": tree.leafsize
    }

    # Save KD tree dictionary to a JSON file
    with open("tree.json", "w") as file:
        json.dump(tree_dict, file)

    # Save DataFrame to a JSON file
    df.to_json("input.json", orient="records")

