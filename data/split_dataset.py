import numpy as np
import pandas as pd

dataset = pd.read_csv("./dataset.csv")

train_df = pd.DataFrame()
test_df = pd.DataFrame()
val_df = pd.DataFrame()

for index, row in dataset.iterrows():
    dataset_type = row["dataset_type"]
    if dataset_type == "train":
        train_df = train_df.append(row)
    elif dataset_type == "test":
        test_df = test_df.append(row)
    elif dataset_type == "val":
        val_df = val_df.append(row)
    else:
        raise Exception("invalid dataset type: {}".format(dataset_type))

train_df.to_csv("./train_dataset.csv")
test_df.to_csv("./test_dataset.csv")
val_df.to_csv("./val_dataset.csv")
