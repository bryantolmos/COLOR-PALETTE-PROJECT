import cv2
import numpy as np
import matplotlib.pyplot as plt



# image "manipulation" functions ------------------------------------


# where the imputs are a path to an image
def image_data_extraction(path: str):
    # reading images -> converting to HSV colorspace
    image = cv2.cvtColor(cv2.imread(path) ,cv2.COLOR_BGR2HSV_FULL)
        
   # vectorized extraction
    data = np.dstack((image[..., 0], image[..., 1], image[..., 2]))   

    return data.astype(np.uint8)

# identify recurring HSV values
def recurring_identify(data, data_channel):
    # count occurances of each value in data channel chosen
    channel_counts = np.bincount(data[:, :, data_channel].flatten())

    # This part of the code is commented out but can be useful
    # it returns a sorted dictionary in descending order where
    # the keys are the data_channel values and the values of 
    # the dictionary are the number of occurences
    #----------------------------------#
    # create a dictionary from the counts without zeros
    #non_zero_dict = {i: count for i, count in enumerate(channel_counts) if count > 0}

    # sort dictionary by descenting order
    #sorted_dict = dict(sorted(non_zero_dict.items(), key=lambda item: item[1], reverse=True))
    
    #return sorted_dict
    #----------------------------------#

    # get indices of non zero counts
    non_zero_indices = np.nonzero(channel_counts)[0]

    # sorte indices by count in descending order, most frequent first
    sorted_indices = non_zero_indices[channel_counts[non_zero_indices].argsort()[::-1]]

    # return list of sorted data channel values
    # made into list to facilitate working with dictionary_mapping()
    return list(sorted_indices)

def dictionary_mapping(source_arr, target_arr):
    # initialize mapped dict
    mapped_dict = {}
    
    # map source to target
    if (len(source_arr) >= len(target_arr)):
        for i in range(0,len(target_arr)):
            mapped_dict[target_arr[i]] = source_arr[i]
        return mapped_dict
    else:
        # mapping based on the length of source arr
        for i in range(0,len(source_arr)):
            mapped_dict[target_arr[i]] = source_arr[i]
        # finishing the rest of the mapping
        # from the remaining index from above to the end or the len of array
        remaining = len(target_arr) - (len(target_arr) - len(source_arr))
        for i in range(len(target_arr) - (len(target_arr) - len(source_arr)), len(target_arr)):
            if (i - remaining == len(target_arr) - (len(target_arr) - len(source_arr))):
                remaining = remaining + len(target_arr) - (len(target_arr) - len(source_arr))
            
            mapped_dict[target_arr[i]] = source_arr[i - remaining]

        return mapped_dict




def image_data_swap(data, source_dict, target_dict, data_channel):
    # get image dimensions
    height, width = data.shape[:2]

    # get frequent reoccuring values
    frequent_values = recurring_identify(data, data_channel)

    # create a mapping dictionary with source and target dictionaries
    mapping = {value: source_dict.get(value, target_dict.get(value, value)) for value in frequent_values}

    # copy of the data to avoid in place modification
    swapped_data = data.copy()

    # vectorized swapping
    swapped_data[:, :, data_channel] = np.vectorize(mapping.get)(swapped_data[:, :, data_channel])

    return swapped_data


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