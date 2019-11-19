import os
import numpy as np
import pandas as pd

csv_dir = "./Diseases_traintestval/"
df = pd.DataFrame()

def generate_feature(row):
    feature_categories = ["F", "M", "0.0", "10.0", "20.0", "30.0", "40.0", "50.0", "60.0", "70.0", "80.0", "90.0"]
    features = []
    for feature in feature_categories:
        features.append(row[feature])
    return features

def disease_to_label(disease):
    disease_names = np.array(['pneumothorax', 'pneumonia', 'pleuralthickening', 'nofinding', 'nodule', 'mass', 'infiltration', 'fibrosis', 'emphysema', 'effusion', 'edema', 'consolidation', 'cardiomegaly', 'atelectasis'])
    label = np.argwhere(disease_names == disease)[0][0]
    return int(label)


for csv_file in os.listdir(csv_dir):
    filename, extension = os.path.splitext(csv_file)
    disease_name, dataset_type = filename.split("_")
    print("Filename: ", filename)
    print("disease_name: ", disease_name)
    print("dataset_type: ", dataset_type)
    sub_disease_df = pd.read_csv(csv_dir+csv_file)
    for idx, row in sub_disease_df.iterrows():
        entry = {"disease": disease_name, "img_name": row["Image Index"], "dataset_type":dataset_type, "feature": generate_feature(row),"label":disease_to_label(disease_name)}
        df = df.append(entry, ignore_index=True)
    print(df)

df.to_csv("./dataset.csv")
