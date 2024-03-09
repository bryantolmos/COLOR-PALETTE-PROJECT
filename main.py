import numpy as np
import image_processing as ip

source_path = "./Images/cat.png"

data = ip.image_data_extraction(source_path)
data_2 = np.array(data.tolist(), dtype=object)

# visualizing data
ip.hsv_print(source_path)

ip.visualize_data(
    hue_channel=data_2[:, :, 2].astype(np.uint8), 
    saturation_channel=data_2[:, :, 3].astype(np.uint8), 
    value_channel=data_2[:, :, 4].astype(np.uint8))
