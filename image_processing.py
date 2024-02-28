import cv2
import numpy as np
import matplotlib.pyplot as plt

def visualize_data(hue, saturation, value):
    # access channels   
    hue_channel = hue
    saturation_channel = saturation
    value_channel = value

    # display using Matplotlib
    fig = plt.figure(figsize=(16, 4))

    fig = plt.subplot(1,3,1)
    fig = plt.imshow(hue_channel, cmap="hsv")
    fig = plt.title("Hue Channel")
    fig = plt.colorbar(label="Hue Value")

    fig = plt.subplot(1,3,2)
    fig = plt.imshow(saturation_channel, cmap="gray")
    fig = plt.title("Saturation Channel")

    fig = plt.subplot(1,3,3)
    fig = plt.imshow(value_channel, cmap="gray")
    fig = plt.title("Value Channel")

    fig = plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.4, hspace=0.4)

    return fig

# where the imputs are a path to an image
def image_data_extraction(source: str, target: str):
    # reading images -> converting to HSV colorspace
    def hsv_conversion(image_path):
        return cv2.cvtColor(cv2.imread(image_path) ,cv2.COLOR_BGR2HSV_FULL)

    def image_data(image):
        # get image height and width
        height, width = image.shape[:2]
        
        # 4d array for image data
        data = np.zeros((4, height, width), dtype=np.uint8)
    
        for y in range(height):
            for x in range(width):
                data[0, y, x] = image[y, x][0] # access hue data
                data[1, y, x] = image[y, x][1] # access saturation data
                data[2, y, x] = image[y, x][2] # access value data

                data[3, y, x] = y
                data[3, y, x] = x
    
        return data

    source_data = image_data(hsv_conversion(source))
    target_data = image_data(hsv_conversion(target))

    return source_data, target_data


            
