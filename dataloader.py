import torch
import torchvision
import torchvision.transforms as transforms
from yoho_dataset import YohoDataset
from general_dataset import GeneralDataset

class YohoLoader(object):

	def __init__(self, args):
		super(YohoLoader, self).__init__()
		transform = transforms.Compose(
		    [
            #  transforms.ToPILImage(),
		    # #  transforms.RandomOrder([
			# # 	transforms.RandomVerticalFlip(),
		    #  transforms.RandomRotation(10),
			# ]),
		     transforms.ToTensor(),
		     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
		     ])

		transform_test = transforms.Compose([
		    transforms.ToTensor(),
		    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)), 
		])

		trainset = YohoDataset(transform=transform)
		self.trainloader = torch.utils.data.DataLoader(trainset, batch_size=args.batchSize,
		                                          shuffle=True, num_workers=2)

		testset = YohoDataset(transform=transform_test, train=False) 
		self.testloader = torch.utils.data.DataLoader(testset, batch_size=args.batchSize,
		                                         shuffle=False, num_workers=2)

		self.classes = ('silent', 'talking')
		
class GeneralLoader(object):

	def __init__(self, directory, batch_size):
		super(GeneralLoader, self).__init__()
		transform = transforms.Compose([
		     transforms.ToTensor(),
		     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
		])

		dataset = GeneralDataset(directory, transform=transform)
		self.dataloader = torch.utils.data.DataLoader(dataset, batch_size=batch_size,
		                                          shuffle=False, num_workers=2)

		self.classes = ('silent', 'talking')