from scipy import ndimage, misc
import numpy as np
import os
import cv2
import matplotlib.pyplot as plt
import imageio

def main():
    outPath = "../silentpaulframes/unrotated"
    path = "../silentpaulframes/unrotated"

    # iterate through the names of contents of the folder
    for image_path in os.listdir(path):
        if (image_path.endswith(".jpg")):
            # create the full input path and read the file
            input_path = os.path.join(path, image_path)
            image_to_rotate = plt.imread(input_path)

            # rotate the image
            rotated = ndimage.rotate(image_to_rotate, 270)

            # create full output path, 'example.jpg' 
            # becomes 'rotate_example.jpg', save the file to disk
            fullpath = os.path.join(outPath, image_path)
            imageio.imsave(fullpath, rotated)

if __name__ == '__main__':
    main()