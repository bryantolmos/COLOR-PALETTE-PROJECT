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

# sort all data by value channel 
def merge_sort(original):
    arr = original
    if len(arr) > 1:
        # array from index 0 to len(arr) / 2
        leftarr = arr[:len(arr)//2]
        # from len(arr) to end of arr
        rightarr = arr[len(arr)//2:]

        # recursion
        merge_sort(leftarr)
        merge_sort(rightarr)

        # merging array
        i = 0 # index of left
        j = 0 # index of right
        k = 0 # index of merged

        while (i < len(leftarr) and j < len(rightarr)):
            if leftarr[i] < rightarr[j]:
                arr[k] = leftarr[i]
                i += 1
            else:
                arr[k] = rightarr[j]
                j += 1
            k += 1
        
        while (i < len(leftarr)):
            arr[k] = leftarr[i]
            i += 1 
            k += 1

        while (j< len(rightarr)):
            arr[k] = rightarr[j]
            j += 1
            k += 1

    return arr