import image_processing as ip
import numpy as np  # Importing NumPy for data type conversion


source = "./Images/palette.png"
target = "./Images/beach.png"

# data channel:
# 2 = Hue 
# 3 = Saturation
# 4 = Value

def debugg(path, data_channel):
    data = ip.image_data_extraction(path)
    data_dict = ip.recurring_identify(data, data_channel)

    print(data_dict)

    return data_dict

sd = debugg(source, 2)
td = debugg(target, 2)

print(ip.dictionary_mapping(sd,td))