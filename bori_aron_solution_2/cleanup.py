import os

directory = os.path.dirname(__file__)
extensions_to_delete = [".pkl", ".parquet"]

all_files = os.listdir(directory)
files_to_delete = [
    file
    for file in all_files
    if any(file.endswith(ext) for ext in extensions_to_delete)
]

for f_to_delete in files_to_delete:
    file_path = os.path.join(directory, f_to_delete)
    try:
        os.remove(file_path)
    except FileNotFoundError:
        print("f{f_to_delete} does not exist.")