import pandas as pd
import os

def classify_dataset(data_dir):
    """
    data_dir (String): /path/to/images/directory/
    based on the data_entry sheet, moves images to diseased or non_diseased directory within data_dir
    """
    df = pd.read_csv("Data_Entry_2017.csv")
    for index, row in df.iterrows():
        img_name = row["Image Index"]
        img_path = data_dir + img_name
        #if the row's image is in the dataset
        if (os.path.exists(data_dir + img_name)):
            #then move it to the corresponding classification directory
            if row["Diseased?"] == 1:
                #move to diseased dir
                destination=data_dir+"diseased/" + img_name
            else:
                #move to non_diseased dir
                destination=data_dir+"non_diseased/" + img_name
            os.rename(img_path, destination)


if __name__ == "__main__":
    #run classify_dataset for a particular data_dir
    data_dir = "./test/"
    classify_dataset(data_dir)
