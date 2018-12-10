import torch
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import Dataset
import os
from skimage import io, transform
import numpy as np
import random

class YohoDataset(Dataset):

	def __init__(self):
		super(YohoDataset, self).__init__()
		self.directories = ["talkingpaulframes", "talkingleoframes", "silentpaulframes", "silentleoframes"]
		self.frames = [0, 0, 0, 0]
		self.file = open("list.txt", "w")
		self.len = 0
		for directory in self.directories:
			self.len += len(os.listdir(os.fsencode(directory))) // 30
		self.len -= self.len % 15

	def __len__(self):			
		return self.len
	
	def __getitem__(self, idx):
		concatImage = None
		rand_i = random.randint(0, len(self.frames) - 1)
		if os.path.isfile(os.path.join(self.directories[rand_i], "frame" + str(self.frames[rand_i] + 14) + ".jpg")):
			for _ in range(self.frames[rand_i], self.frames[rand_i] + 15):
				self.file.write(os.path.join(self.directories[rand_i], "frame" + str(self.frames[rand_i]) + ".jpg") + "\n")
				# image = io.imread(os.path.join(self.directories[rand_i], "frame" + str(self.frames[rand_i]) + ".jpg"), as_gray=True)
				# image = transform.resize(image, (30, 68), anti_aliasing=True, mode='constant')
				# image = image.reshape(image.shape[0], image.shape[1], 1)
				# if concatImage is None:
				# 	concatImage = image
				# else:
				# 	concatImage = np.concatenate((concatImage, image), axis=-1)
				self.frames[rand_i] += 1
		else:
			del self.frames[rand_i]
			del self.directories[rand_i]
		tag = 0
		if rand_i < 2:
			tag = 1
		return {'image': concatImage, 'tag': tag}

face_dataset = YohoDataset()


print(face_dataset.len)

for i in range(len(face_dataset) + 100):
	a = face_dataset[i]

# for i in range(4):
#     sample = face_dataset[i]

#     print(i, sample['image'].shape, sample['tag'])

		# transform = transforms.Compose(
		#     [
		#     #  transforms.RandomOrder([
		# 	# 	transforms.RandomVerticalFlip(),
		# 	# 	transforms.RandomRotation(20)
		# 	# ]),
		#      transforms.ToTensor(),
		#      transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
		#      ])

		# transform_test = transforms.Compose([
		#     transforms.ToTensor(),
		#     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)), 
		# ])

		# trainset = torchvision.datasets.CIFAR10(root='./data', train=True,
		#                                         download=True, transform=transform)
		# self.trainloader = torch.utils.data.DataLoader(trainset, batch_size=args.batchSize,
		#                                           shuffle=True, num_workers=2)

		# testset = torchvision.datasets.CIFAR10(root='./data', train=False,
		#                                        download=True, transform=transform_test) 
		# self.testloader = torch.utils.data.DataLoader(testset, batch_size=args.batchSize,
		#                                          shuffle=False, num_workers=2)

		# self.classes = ('plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck')
		
