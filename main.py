import numpy as np
import image_processing as ip

source_path = "./Images/beach.png"

ip.hsv_print(source_path)

data = ip.image_data_extraction(source_path)

ip.visualize_data(
    hue_channel=data[:, :, 2].astype(np.uint8), 
    saturation_channel=data[:, :, 3].astype(np.uint8), 
    value_channel=data[:, :, 4].astype(np.uint8))

redata = ip.recurring_identify(data, 4)

print(redata)

