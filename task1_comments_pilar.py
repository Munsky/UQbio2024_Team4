# 1- I want to open tiff files that are in a specific folder and extract the metadata, for each tiff file i want to make this analysis
# the images have several frames and i want to analyze each frame separately

## for this i will use the package tifffile and the function imread to open the tiff files
## I will use the function metadata to extract the metadata of the tiff file
import tifffile
from tifffile import imread

open_tiff = imread('path/to/tiff/file')
metadata = tifffile.TiffFile('path/to/tiff/file').pages[0].tags

# 2- The images have 3 channels, I want to extract specific data from each channel so i want to separate the channels
# channel 0: red (1)
# channel 1: green (2)
# channel 2: blue (3)

## for this i will use the function split to separate the channels
import numpy as np
split_channels = np.split(open_tiff, 3, axis=0)

## I will use the function imshow to visualize the images and the channels separately 
import matplotlib.pyplot as plt
plt.imshow(split_channels[0])
plt.imshow(split_channels[1])
plt.imshow(split_channels[2])

# 3- I want to save the metadata in a csv file
## for this i will use the package pandas and the function to_csv to save the metadata in a csv file
import pandas as pd
metadata_df = pd.DataFrame(metadata)
metadata_df.to_csv('path/to/csv/file')

# 4- The metadata should have this information for each image:

# title: title of the image 

# column1: image name (frame number) or cell number
## for this i will use the function split to separate the image name from the path
image_name = 'path/to/tiff/file'.split('/')[-1]


# column2: number of viable cells in channel 0 for each frame
## for this i will use the function threshold to separate the cells from the background or i can use mask to separate the cells from the background 


# column3: cell size in channel 1 for each cell in each frame
##for this i can use mask to separate the cells from the background and then extract the cell size

# column4: nucleus size in channel 1 for each cell in each frame
## for this i can use mask to separate the cells from the background and then extract the nucleus size


# column5: protein concentration in channel 1 for each cell in each frame
## for this i can use mask to separate the cells from the background and then extract the protein concentration

# column6: number of mRNA in nucleus in channel 2 for each cell in each frame
## i can use mask and threshold to separate the nucleus from the background and then extract the number of mRNA in the nucleus

# column 7: number of mRNA in cytoplasmn in channel 2 for each cell in each frame
## i can use mask and threshold to separate the cytoplasm from the background and then extract the number of mRNA in the cytoplasm

# column7: number of transcription sites in channel 2 for each cell in each frame

# column8: intensity of transcription sites in channel 2 for each cell in each frame
