import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch
import os
import datetime
import pdb
import time
import torchvision.models as torchmodels


class BaseModel(nn.Module):
    def __init__(self):
        super(BaseModel, self).__init__()
        # if not os.path.exists('logs'):
        #     os.makedirs('logs')
        # ts = time.time()
        # st = datetime.datetime.fromtimestamp(
            # ts).strftime('%Y-%m-%d_%H:%M:%S_log.txt')
        # self.logFile = open('logs/' + st, 'w')

    # def log(self, str):
    #     print(str)
    #     self.logFile.write(str + '\n')

    def criterion(self):
        # return nn.MSELoss()
        return nn.CrossEntropyLoss()

    def optimizer(self):
        return optim.SGD(self.parameters(), lr=0.001)

    def adjust_learning_rate(self, optimizer, epoch, args):
        lr = args.lr * (0.9**(epoch // 50))# TODO: Implement decreasing learning rate's rules
        for param_group in optimizer.param_groups:
            param_group['lr'] = lr


class LazyNet(BaseModel):
    def __init__(self):
        super(LazyNet, self).__init__()
        self.fc = nn.Linear(30 * 68 * 15, 2)

    def forward(self, x):
        # TODO: Implement forward pass for LazyNet
        # print(list(x.size()))
        x = x.view(x.size(0), -1)
        # print(list(x.size()))
        x = self.fc(x)
        return x
        

class BoringNet(BaseModel):
    def __init__(self):
        super(BoringNet, self).__init__()
        self.fc1 = nn.Linear(32 * 32 * 3, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = x.view(x.size(0), -1)
        x = F.leaky_relu(self.fc1(x))
        x = F.leaky_relu(self.fc2(x))
        x = self.fc3(x)
        return x


# class CoolNet(BaseModel):
#     def __init__(self):
#         super(CoolNet, self).__init__()
#         self.conv1 = nn.Conv2d(3, 20, kernel_size=3, padding=1, stride=1)
#         self.pool1 = nn.MaxPool2d(kernel_size=2, stride=2, padding=0)
#         self.conv2 = nn.Conv2d(20, 24, kernel_size=3, stride=1, padding=1)
#         self.pool2 = nn.MaxPool2d(kernel_size=2, stride=2, padding=0)
#         self.fc1 = nn.Linear(24 * 8 * 8, 600)
#         self.fc2 = nn.Linear(600, 10)

#     def forward(self, x):
#         # x = F.relu(self.conv1(x))
#         # x = self.pool1(x)
#         # x = F.relu(self.conv1(x))
#         # x = self.pool2(x)
#         # x = x.view(x.size(0), -1)
#         # x = F.leaky_relu(self.fc1(x))
#         # x = F.leaky_relu(self.fc2(x))
#         # x = self.fc3(x)
#         x = F.relu(self.conv1(x))
#         x = self.pool1(x)
#         x = F.relu(self.conv2(x))
#         x = self.pool2(x)
#         x = x.view(x.size(0), -1)
#         x = F.leaky_relu(self.fc1(x))
#         x = self.fc2(x)
#         # x = self.fc3(x)
#         return x
