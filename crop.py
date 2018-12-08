import cv2
import os
import argparse

def crop(directory):
    directory = os.fsencode(directory)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".jpg"):
            textfile = open(os.fsdecode(directory) + "/" + filename.replace(".jpg", ".txt"))
            for line in textfile:
                line = line.strip()
                line = line.split()
                x = int(line[0])
                y = int(line[1])
                w = int(line[2])
                h = int(line[3])
            img = cv2.imread(os.fsdecode(directory) + "/" + filename)
            dim = img.shape
            width = dim[1]
            s = width / 500
            crop_img = img[int(y * s):int((y + h) * s), int(x * s):int((x + w) * s)]
            cv2.imwrite(os.fsdecode(directory) + "/" + filename, crop_img)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-d", "--directory", required=True,
        help="path to crop images in")
    args = vars(ap.parse_args())
    crop(args['directory'])