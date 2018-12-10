import argparse
from dataloader import GeneralLoader
import numpy as np
import torch

def map_to_video(frames_dir, mouth_dir, yoho_dir):
    pass  # TODO

def run_net(net, dataset, idx):
    with torch.no_grad():
        outputs = net(dataset[idx])
        _, predicted = torch.max(outputs.data, 1)
    return predicted

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

