import cv2
import numpy as np
import matplotlib.pyplot as plt

def hsv_print(path):
    image = cv2.cvtColor(cv2.imread(path) ,cv2.COLOR_BGR2HSV_FULL)
    cv2.imshow('hsv image',image)
    cv2.waitKey(0)

def visualize_data(hue_channel, saturation_channel, value_channel):
    # create the figure and adjust layout
    fig, axes = plt.subplots(1, 3, figsize=(16, 4))
    fig.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.4, hspace=0.4)

    # display each channel on a separate subplot
    fig.colorbar(axes[0].imshow(hue_channel, cmap="hsv"), ax=axes[0], label="Hue Value")
    axes[0].set_title("Hue Channel")

    axes[1].imshow(saturation_channel, cmap="gray")
    axes[1].set_title("Saturation Channel")

    axes[2].imshow(value_channel, cmap="gray")
    axes[2].set_title("Value Channel")

    plt.show()

# where the imputs are a path to an image
def image_data_extraction(path: str):
    # reading images -> converting to HSV colorspace
    image = cv2.cvtColor(cv2.imread(path) ,cv2.COLOR_BGR2HSV_FULL)

    # get image height and width
    height, width = image.shape[:2]
        
    # empty numpy array to store pixel data (HSV)
    data = np.empty((height, width, 5), dtype=np.uint8)
    
    for y in range(height):
        for x in range(width):
            # accessing and storing hsv image data
            data[y, x, 0] = x  # Store x coordinate
            data[y, x, 1] = y  # Store y coordinate
            data[y, x, 2] = image[y, x][0]  # Store hue value 
            data[y, x, 3] = image[y, x][1]  # Store saturation value 
            data[y, x, 4] = image[y, x][2]  # Store value value     

    return data

# analyse image in chunks to do less operations
def chunk_analysis(image_data, image_path):
    image = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2HSV_FULL)

    x = image.shape[1] - (image.shape[1] % 3)
    y = image.shape[0] - (image.shape[0] % 3)
    
    data = np.empty((int(y/3), int(x/3), 5), dtype=np.uint8)
    
    # iterate through the center of every 3x3 chung available and store the val
    # of that center pixel into out data array
    index_y = 0
    index_x = 0
    for i in range(1, y, 3):
        for j in range(1, x, 3):
            data[index_y, index_x, 0] = i  # Store x coordinate
            data[index_y, index_x, 1] = j  # Store y coordinate
            data[index_y, index_x, 2] = image_data[i, j][0]  # Store hue value 
            data[index_y, index_x, 3] = image_data[i, j][1]  # Store saturation value 
            data[index_y, index_x, 4] = image_data[i, j][2]  # Store value value 
            index_x += 1
        index_x = 0
        index_y += 1

    return data