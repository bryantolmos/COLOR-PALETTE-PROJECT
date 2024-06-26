import cv2
import numpy as np
import matplotlib.pyplot as plt



# image "manipulation" functions ------------------------------------


# where the imputs are a path to an image
def image_data_extraction(path: str):
    # reading images -> converting to HSV colorspace
    image = cv2.cvtColor(cv2.imread(path) ,cv2.COLOR_BGR2HSV_FULL)

    # get image height and width
    height, width = image.shape[:2]
        
    # empty numpy array to store pixel data (HSV)
    data = np.empty((width, height, 5), dtype=np.uint8)
    
    for x in range(width):
        for y in range(height):
            # accessing and storing hsv image data
            data[x, y, 0] = x  # Store x coordinate
            data[x, y, 1] = y  # Store y coordinate
            data[x, y, 2] = image[x, y][0]  # Store hue value 
            data[x, y, 3] = image[x, y][1]  # Store saturation value 
            data[x, y, 4] = image[x, y][2]  # Store value value     

    return data

# identify recurring HSV values
def recurring_identify(data, data_channel):
# initializing dict
    dictionary = {}
    for i in range(0,256):
        dictionary[i] = 0

    for x in range(len(data[0])): # length
        for y in range(len(data[1])): # height
            dictionary[data[x,y][data_channel]] += 1

    # remove all zero values
    non_zero_dict = {key: value for key, value in dictionary.items() if value != 0}

    # overwrite data
    non_zero_dict = dict(sorted(non_zero_dict.items(), key=lambda item: item[1], reverse=True))

    return non_zero_dict

def image_data_swap(path: str, source_dict, target_dict, target_image_data, data_channel):
    # reading images -> converting to HSV colorspace
    target_image = cv2.cvtColor(cv2.imread(path) ,cv2.COLOR_BGR2HSV_FULL)

    # get image height and width
    height, width = target_image.shape[:2]


    # start color swap

    
    # convert dictionary keys to lists
    keys_list1 = list(source_dict)
    keys_list2 = list(target_dict)

    # extend keys_list1 with additional keys from keys_list2
    if (len(keys_list1) < len(keys_list2)):
        keys_list1.extend(keys_list2[len(source_dict):])

    # create a mapping dictionary
    mapping = {}
    for key, value in zip(target_dict.keys(), keys_list1):
        mapping[key] = value

    # print the resulting mapping
    # print(mapping)

    
    for x in range(width):
        for y in range(height):
            # accessing and storing hsv image data
            target_image_data[x, y, data_channel] = mapping[target_image_data[x, y, data_channel]]  # Store hue value 

    return target_image_data



# visualize functions ------------------------------------


def hsv_print(path):
    image = cv2.cvtColor(cv2.imread(path) ,cv2.COLOR_BGR2HSV_FULL)
    cv2.imshow('hsv image',image)
    cv2.waitKey(0)
    #cv2.imwrite('hsv_image.jpg', image)

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

def hsv_bgr(hsv_data):
    # extracting HSV channels cutting off x & y cords
    data = hsv_data[:, :, :3] 
    print(f"Number of channels in new_image: {data.shape[2]}")

    return cv2.cvtColor(data.astype(np.float32), cv2.COLOR_HSV2BGR_FULL)



# just storing functions ------------------------------------


# lowkey dont know why i need this, but still kinda cool 
# analyse image in chunks to do less operations
# also need to update x and y stuff but nawwwwww
def chunk_analysis(image_data, image_path):
    image = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2HSV_FULL)

    size = 3

    x = image.shape[1] - (image.shape[1] % size)
    y = image.shape[0] - (image.shape[0] % size)
    
    data = np.empty((int(y/size), int(x/size), 5), dtype=np.uint8)
    
    # iterate through the center of every 3x3 chung available and store the val
    # of that center pixel into out data array
    index_y = 0
    index_x = 0
    for i in range(1, y, size):
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