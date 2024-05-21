import image_processing as ip
import cv2
import numpy as np  # Importing NumPy for data type conversion


source = "./Images/palette.png"
target = "./Images/beach.png"

# data channel:
# 2 = Hue 
# 3 = Saturation
# 4 = Value


def main(source_path, target_path, data_channel):
    def image(path, data_channel):
        # 1) print image in HSV color space
        #ip.hsv_print(path)
    
        # 2) extract data from image
        data = ip.image_data_extraction(path)

        # 3) visualize data
        #ip.visualize_data(
            #hue_channel=data[:, :, 2].astype(np.uint8), 
            #saturation_channel=data[:, :, 3].astype(np.uint8), 
            #value_channel=data[:, :, 4].astype(np.uint8))
    
        # 4) find the recurring data
        recurring_data = ip.recurring_identify(data, data_channel)

        # 6) return recurring data
        return recurring_data, data
    
    source_dict, source_data = image(source_path, data_channel)
    target_dict, target_data = image(target_path, data_channel)
    
    new_source_image = ip.image_data_swap(target_path, source_dict, target_dict, target_data, data_channel)

    return new_source_image

new_image = main(source,target,4)

img = ip.hsv_bgr(new_image).astype(np.uint8)

# Try both saving methods
try:
  cv2.imwrite("swapped_image_v1.jpg", img)  # Regular saving
  print("hello")
except:
  cv2.imwrite("swapped_image_v2.jpg", img, flags=cv2.IMWRITE_UNCHANGED)  # Alternative saving
  print("ou ou ou")