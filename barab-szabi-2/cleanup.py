import os
filelist = [ f for f in os.listdir() if f.endswith(".parquet") or 
            f.endswith(".pkl")]
for f in filelist:
    os.remove(f)