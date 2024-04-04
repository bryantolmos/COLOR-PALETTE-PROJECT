import numpy as np
import image_processing as ip

source_path = "./Images/cat.png"

ip.hsv_print(source_path)

data = ip.image_data_extraction(source_path)

data_processed = ip.chunk_analysis(data,source_path)

ip.visualize_data(
    hue_channel=data[:, :, 2].astype(np.uint8), 
    saturation_channel=data[:, :, 3].astype(np.uint8), 
    value_channel=data[:, :, 4].astype(np.uint8))

ip.visualize_data(
    hue_channel=data_processed[:, :, 2].astype(np.uint8), 
    saturation_channel=data_processed[:, :, 3].astype(np.uint8), 
    value_channel=data_processed[:, :, 4].astype(np.uint8))
