import argparse
from dataloader import GeneralLoader
import numpy as np
import torch
import os
import cv2

def transform_to_video(directory):
    os.system("ffmpeg -y -r 30 -i " + directory + "/frame%d.jpg -vcodec libx264 -crf 15 -pix_fmt yuv420p " + directory + "/video.mp4 > /dev/null 2>&1")

def run_net(net, general_loader, directory, framedir):
    loader = general_loader.dataloader
    with torch.no_grad():
        for data in loader:
            image = data['image'].float()
            framenum = data['framenum']
            mouthnum = data['mouthnum']
            outputs = net(image)
            _, predicted = torch.max(outputs.data, 1)
            predicted = predicted.tolist()
            for i in range(len(predicted)):
                for j in range(int(framenum[i]) * 2, int(framenum[i]) * 2 + 30):
                    mouthfilename = os.path.join(directory, "frame" + str(j // 2) + ".txt")
                    mouthfile = open(mouthfilename, "r")
                    mouthdata = mouthfile.read().split("\n")[int(mouthnum[i]) - 1]
                    colorframe = cv2.imread(os.path.join(framedir, "frame" + str(j) + ".jpg"))
                    color = (0, 255, 0) if predicted[i] == 1 else (0, 0, 255)
                    coords = mouthdata.split(" ")
                    _, w, _ = colorframe.shape
                    x1 = int(int(coords[0]) * (w / 500))
                    y1 = int(int(coords[1]) * (w / 500))
                    x2 = int((int(coords[0]) + int(coords[2])) * (w / 500))
                    y2 = int((int(coords[1]) + int(coords[3])) * (w / 500))
                    cv2.rectangle(colorframe, (x1, y1), (x2, y2), color, 2)
                    cv2.imwrite(os.path.join(framedir, "frame" + str(j) + ".jpg"), colorframe)
                    mouthfile.close()

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--framedir", required=True,
        help="path to color frames")
    ap.add_argument("-d", "--directory", required=True,
        help="path with mouths")
    ap.add_argument("-y", "--yoho", required=True,
        help="path to .yoho weights file")
    args = vars(ap.parse_args())
    loader = GeneralLoader(args["directory"], 4)
    net = torch.load(args["yoho"])
    net.eval()
    run_net(net, loader, args["directory"], args["framedir"])
    transform_to_video(args["framedir"])

