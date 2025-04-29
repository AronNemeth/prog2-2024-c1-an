import pandas as pd
import pickle
from multiprocessing import Process

def process_query(query_df, tree, output_queue):
    distances, indices = tree.query(query_df, k=1)
    weapon_values = df.iloc[indices]["weapon"].values
    output_queue.put((distances, weapon_values))

if __name__ == "__main__":
    df = pd.read_pickle("input.pkl")
    query_df = pd.read_csv("query.csv")

    with open("tree.pkl", "rb") as file:
        tree = pickle.load(file)

    # Split the query data into two halves
    query_df_split = np.array_split(query_df, 2)

    # Create a queue to collect results from processes
    output_queue = multiprocessing.Queue()

    # Create processes for parallel execution
    processes = []
    for query_df_part in query_df_split:
        process = Process(target=process_query, args=(query_df_part, tree, output_queue))
        process.start()
        processes.append(process)

    # Wait for all processes to finish
    for process in processes:
        process.join()

    # Collect results from the output queue
    distances_list = []
    weapon_values_list = []
    while not output_queue.empty():
        distances, weapon_values = output_queue.get()
        distances_list.append(distances)
        weapon_values_list.append(weapon_values)

    # Concatenate results from different processes
    distances = np.concatenate(distances_list)
    weapon_values = np.concatenate(weapon_values_list)

    # Save results to CSV
    pd.DataFrame({"dist": distances, "weapon": weapon_values}).to_csv("out.csv", index=False)

