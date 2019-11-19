import os
import shutil
import pandas as pd

#disease_names = ['pneumothorax', 'pneumonia', 'pleuralthickening', 'nofinding', 'nodule', 'mass', 'infiltration', 'fibrosis', 'emphysema', 'effusion', 'edema', 'consolidation', 'cardiomegaly', 'atelectasis']
disease_names = ['atelectasis']
dataset_divisions = ['train', 'test', 'val']
images_dir="/storage/images/"
data_dir="/storage/x-ray-data/data/"
df_dir="./Diseases_traintestval/"

if __name__ == "__main__":
	for disease_name in disease_names:
		for set_type in dataset_divisions:
			os.makedirs(data_dir + set_type + "/" + disease_name, exist_ok=True)
			dataframe_name = df_dir + disease_name + "_" + set_type +".csv"
			df = pd.read_csv(dataframe_name)
			print("disease: ", disease_name)
			print("dataset type: ", set_type)
			#print(df)
			for idx, row in df.iterrows():
				img_name = row["Image Index"]
				source = images_dir+img_name
				destination = data_dir + set_type + "/" + disease_name + "/" + img_name
				shutil.copy(source, destination) 
