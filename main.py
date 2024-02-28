import matplotlib.pyplot as plt
import image_processing as ip

source, target = ip.image_data_extraction("./Images/cat.png", "./Images/robin.png")

sourcefig = ip.visualize_data(source[0], source[1], source[2])
targetfig = ip.visualize_data(target[0], target[1], target[2])

sourcefig = plt.show()
targetfig = plt.show()
