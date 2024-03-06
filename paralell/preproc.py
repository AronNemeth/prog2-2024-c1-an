import pandas as pd
from scipy.spatial import KDTree
import pickle

if __name__ == "__main__":
    df = pd.read_csv("input.csv")
    df.to_pickle("input.pkl")

    # Build tree and save it as pickle
    tree = KDTree(df[["x", "y"]])

    with open("tree.pkl", "wb") as file:
        pickle.dump(tree, file)
