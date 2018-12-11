import torch
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import Dataset
import os
from skimage import io, transform
import numpy as np
import random

class GeneralDataset(Dataset):

    def __init__(self, directory, transform=None):
        super(GeneralDataset, self).__init__()
        self.directory = os.fsencode(directory)
        self.transform = transform
        self.framecounter = 0
        self.mouthcounter = 1
        self.file = open(os.path.join(directory, "out.txt"), 'w')
        numFrames = int(open(os.path.join(directory, "framecount.txt"), "r").read())
        while self.framecounter < numFrames:
            oldFrameCounter = self.framecounter
            if os.path.isfile(os.path.join(directory, "frame" + str(self.framecounter + 14) + "-" + str(self.mouthcounter) + ".jpg")):
                for _ in range(oldFrameCounter, oldFrameCounter + 15):
                    name = os.path.join(directory, "frame" + str(self.framecounter) + "-" + str(self.mouthcounter) + ".jpg")
                    if not os.path.isfile(name):
                        break
                    self.file.write(name + "\n")
                    self.framecounter += 1
            if os.path.isfile(os.path.join(os.fsdecode(self.directory), "frame" + str(oldFrameCounter + 14) + "-" + str(self.mouthcounter + 1) + ".jpg")):
                self.framecounter = oldFrameCounter
                self.mouthcounter += 1
            else:
                self.framecounter = oldFrameCounter + 15
                self.mouthcounter = 1
        self.file.close()
        self.list = open(os.path.join(directory, "out.txt"), "r").read().split("\n")

    def __len__(self):
        return len(self.list) // 15

    def __getitem__(self, idx):
        concatImage = None
        for i in range(idx * 15, idx * 15 + 15):
            image = io.imread(self.list[i], as_gray=True)
            image = transform.resize(image, (30, 68), anti_aliasing=True, mode='constant')
            image = image.reshape(image.shape[0], image.shape[1], 1)
            concatImage = image if concatImage is None else np.concatenate((concatImage, image), axis=-1)
        if self.transform:
            concatImage = self.transform(concatImage)
        return {'image': concatImage, 'framenum': self.list[idx * 15][self.list[idx * 15].rfind("frame")+5:self.list[idx * 15].rfind("-")],
                'mouthnum': self.list[idx * 15][self.list[idx * 15].rfind("-")+1:-4]}

# face_dataset = GeneralDataset("frames")


# print(len(face_dataset))


# for i in range(4):
#     sample = face_dataset[i]
#     print(i, sample['image'].shape, sample['tag'])

# sample = face_dataset[100]
# print(sample['image'].shape, sample['tag'])
# sample = face_dataset[100]
# print(sample['image'].shape, sample['tag'])
