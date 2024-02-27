import pandas as pd
from scipy.spatial import KDTree
import pickle

if __name__ == "__main__":
    df = pd.read_csv("input.csv")

    tree = KDTree(df[["x", "y"]].values)

    with open("tree.pickle", "wb") as file:
        pickle.dump(tree, file)

    df.to_pickle("input.pkl")
