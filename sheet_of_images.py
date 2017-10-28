import numpy as np
import os  # to get file listing
from tqdm import tqdm  # progress bar to track progress
from time import sleep  # help with progress bar
from PIL import Image, ImageOps
from time import sleep

# Path to your images. The path should only contain images that are saved as numpy array save files (".npy")
#  as the helper is not set-up to filter files

# Note: images all need to be the same size.
path_to_images = "C:/Users/ttobey.GSI/Desktop/nfl_data/test_images/"

# create list of image files in directory
file_list = os.listdir(path_to_images)
save_path = "C:/Users/ttobey.GSI/Desktop/nfl_data/thumbnails/"

# To create array of images need to know the number of images and their dimensions
# image_count = len(file_list)  # gets count of images
# r, c, d = np.shape(np.load(path_to_images + file_list[0]))  # gets size of images; note assumes all image are same size




total_images = len(file_list)

images_per_row = 5
size = 100, 100
border =4
def create_zero(r,c,d,border,total_images):
    r1= r+(border*2)
    c1 = c+(border*2)
    rows = int((total_images/images_per_row)*r1)
    columns = c1*images_per_row
    master_array = np.zeros((rows,columns,d))
    return master_array
images_displayed =0
#new_img = Image.new('RGB',(400,400))
for image_count, file in enumerate(file_list):
    if image_count == 0:
        start_array = np.load(path_to_images+file)
        r,c,d = start_array.shape
        master_array = create_zero(r,c,d,border,total_images)
        print(master_array.shape)

        row_start = border
        row_end = r+border
        col_start = border
        col_end = c+ border
        master_array[row_start:row_end,col_start:col_end,:d] = start_array


        images_displayed =1
    else:
        if images_displayed == images_per_row:
            row_start = row_end + border+border #move down
            row_end = row_start+r
            col_start = border # reset to zero
            col_end = c+ border # reset to zero
            images_displayed =0
        else:
            #Only moving right so ne need to change row
            col_start = col_end + border+border
            col_end = col_start+c
        add_array = np.load(path_to_images+file)
        master_array[row_start:row_end,col_start:col_end,:d] = add_array # loads array into empty file
        #add_array = np_zeros
        #start_array =  np.concatenate((start_array,add_array), axis =1)
        images_displayed =  images_displayed  + 1
    #if image_count > 2:

        #break



# print(start_array.shape)
# r1,c1,d1 = start_array.shape
# total_images = image_count+1
# print(image_count)
#
# rows = int(((total_images)/images_per_row)*r1)
# print(columns)
# start_array = start_array.reshape((rows,columns,d))
img= (master_array*255).astype(np.uint8)

img = Image.fromarray(img)


img.show()


    #img = img.thumbnail(size)

    #img.save(save_path+file + ".thumbnail", "JPEG")
# image = np.load(path_to_images+infile)
# image= (image*255).astype(np.uint8)
# img = Image.fromarray(image)
# img = img.resize(size)
# img= ImageOps.expand(img,border = 4, fill =0)

# if i == 0:
#     npy_image = np.load(path_to_images+file)
#     npy_image= (npy_image*255).astype(np.uint8)
#     start_image = Image.fromarray(npy_image)
#     start_image = start_image.thumbnail(size)
# else:
#     npy_image = np.load(path_to_images+file)
#     npy_image = (npy_image*255).astype(np.uint8)
#     next_image = Image.fromarray(npy_image)
#     next_image= next_image.thumbnail(size)
#     start_image.paste(next_image,box=None, mask=None)