import torch
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import Dataset
import os
from skimage import io, transform
import numpy as np
import random

class YohoDataset(Dataset):

	def __init__(self, transform=None, train=True):
		super(YohoDataset, self).__init__()
		self.list = open("list.txt", "r").read().split("\n")
		self.transform = transform
		splice_index = int(0.3 * len(self.list))
		splice_index -= splice_index % 15
		if train:
			self.list = self.list[splice_index:len(self.list)]
		else:
			self.list = self.list[0:splice_index]

	def __len__(self):
		return len(self.list) // 15
	
	def __getitem__(self, idx):
		concatImage = None
		for i in range(idx * 15, idx * 15 + 15):
			image = io.imread(self.list[i], as_gray=True)
			image = transform.resize(image, (30, 68), anti_aliasing=True, mode='constant')
			image = image.reshape(image.shape[0], image.shape[1], 1)
			concatImage = image if concatImage is None else np.concatenate((concatImage, image), axis=-1)
		tag = 0
		if "talking" in self.list[idx * 15]:
			tag = 1
		if self.transform:
			concatImage = self.transform(concatImage)
		return {'image': concatImage, 'tag': tag}

# face_dataset = YohoDataset()


# print(len(face_dataset))


# for i in range(1):
#     sample = face_dataset[i]
#     print(i, sample['image'].shape, sample['tag'])
#     print(sample['image'])

# sample = face_dataset[100]
# print(sample['image'].shape, sample['tag'])
# sample = face_dataset[100]
# print(sample['image'].shape, sample['tag'])
