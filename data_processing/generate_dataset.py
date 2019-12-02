import os
import shutil

with open('./train_val_list.txt', 'r') as f_train:
	#read each line
	image_names = f_train.read().splitlines()
	#move the corresponding image to the train directory
	for image_name in image_names:
		img_path = "./images/"+image_name
		destination="./train/"+image_name
		#move the file by renaming the path
		os.rename(img_path, destination)
		#move file from the directory


with open('./test_list.txt', 'r') as f_test:
	#read each line
	image_names = f_test.read().splitlines()
	#move the corresponding image to the train directory
	for image_name in image_names:
		img_path = "./images/"+image_name
		destination="./test/"+image_name
		#move the file by renaming the path
		os.rename(img_path, destination)
		#move file from the directory
