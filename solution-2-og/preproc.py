import pandas as pd

if __name__ == "__main__":
    pd.read_csv("input.csv").to_pickle("input.pkl")
