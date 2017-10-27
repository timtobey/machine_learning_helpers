import numpy as np
import os  # to get file listing
from tqdm import tqdm  # progress bar to track progress
from time import sleep  # help with progress bar

######################################################
# As creating image arrays for machine learning can be memory intensive
# that prevent the use of simple concatenate functions.
# This function uses a numpy memmap array to reduce memory requirements.
# It will create an array of images from images saved as numpy arrays.
######################################################

# Set Your image source path, array path, array name  and then run.


# Path to your images. The path should only contain images that are saved as numpy array save files (".npy")
#  as the helper is not set-up to filter files

# Note: images all need to be the same size.
path_to_images = "C:/my_images/"

# path where to save array of images. Needs to be different from image folder or could create issues.
# Make sure you use a drive with a enough space as these arrays can be large
path_to_master_array = "C:/master_image_array/"

# name of array of images array
master_array_file_name = "master_test_array.npy"


# create list of image files in directory
file_list = os.listdir(path_to_images)

# To create array of images need to know the number of images and their dimensions
image_count = len(file_list)  # gets count of images
r, c, d = np.shape(np.load(path_to_images + file_list[0]))  # gets size of images; note assumes all image are same size


# A numpy memmap array is created. This is done because we don't want to load the entire array into memory.
# Note the 'w+' flag; any  existing memmap file will be overwritten so be careful


fm = np.memmap(path_to_master_array + master_array_file_name,
               dtype='float32', mode='w+', shape=(image_count, r, c, d))

# iterate through the images and change memmap array
for i, file in tqdm(enumerate(file_list)):
    fm[i, ...] = np.load(path_to_images + file)
    sleep(.005)
