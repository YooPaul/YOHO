import cv2
import os
import argparse

def crop(directory):
    counter = 0
    directory = os.fsencode(directory)
    for file in os.listdir(directory):
        print(counter)
        filename = os.fsdecode(file)
        if filename.endswith(".jpg"):
            if not os.path.isfile(os.fsdecode(directory) + "/" + filename.replace(".jpg", ".txt")):
                os.remove(os.fsdecode(directory) + "/" + filename)
                continue
            textfile = open(os.fsdecode(directory) + "/" + filename.replace(".jpg", ".txt"))
            i = 1
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
                r = 2.281
                if w / h > r:
                    y -= (w / r - h) / 2
                    h = w / r
                else:
                    x -= (h * r - w) / 2
                    w = h * r
                x -= 0.05 * w
                y -= 0.05 * h
                w += 0.1 * w
                h += 0.1 * h
                crop_img = img[int(y * s):int((y + h) * s), int(x * s):int((x + w) * s)]
                cv2.imwrite(os.fsdecode(directory) + "/" + filename.replace(".jpg", "") + "-" + str(i) + ".jpg", crop_img)
                i += 1
        counter += 1

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-d", "--directory", required=True,
        help="path to crop images in")
    args = vars(ap.parse_args())
    crop(args['directory'])