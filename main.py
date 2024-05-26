import image_processing as ip
import cv2

source = "./Images/mountains.jpg"
target = "./Images/sheep.jpg"
data_channel = 0

# data channel:
# 2 = Hue 
# 3 = Saturation
# 4 = Value

def main(source_path, target_path, data_channel):
    source_data = ip.image_data_extraction(source_path)
    target_data = ip.image_data_extraction(target_path)

    source_arr = ip.recurring_identify(source_data, data_channel)
    target_arr = ip.recurring_identify(target_data, data_channel)

    mapped_dictionary = ip.dictionary_mapping(source_arr, target_arr)

    new_image = ip.image_data_swap(target_data, mapped_dictionary, data_channel)

    cv2.imshow('new image', new_image)
    cv2.waitKey(0)

    return new_image

image = main(source, target, data_channel)
ip.hsv_bgr(image)
#ip.hsv_print(target)