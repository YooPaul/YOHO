# adapted from: https://stackoverflow.com/questions/33311153/python-extracting-and-saving-video-frames

import cv2
import argparse
import os

def splitFrames(directory, nndir, filename):

    vidcap = cv2.VideoCapture(filename)
    success,image = vidcap.read()
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    count = 0

    if not os.path.exists(directory):
        os.makedirs(directory)

    if not os.path.exists(nndir):
        os.makedirs(nndir)

    while success:
        # image = cv2.transpose(image)
        # image = cv2.flip(image, 1)
        cv2.imwrite(directory + "/frame%d.jpg" % count, image)
        if count % 2 == 0:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            
            cv2.imwrite(nndir + "/frame%d.jpg" % (count / 2), image)     # save frame as JPEG file      
            # print('Read a new frame: ', success)
        success, image = vidcap.read()
        count += 1
        print(count)

    f = open(os.path.join(nndir, "framecount.txt"), "w")
    f.write(str((count + 1) // 2))
    f.close()

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--file", required=True,
        help="path to video file")
    ap.add_argument("-n", "--nndir", required=True,
        help="path to save frames in for neural network")
    ap.add_argument("-d", "--directory", required=True,
        help="path to save full frames in")
    args = vars(ap.parse_args())
    splitFrames(args['directory'], args['nndir'], args["file"])
