from utils import argParser
from dataloader import YohoLoader
import matplotlib.pyplot as plt
import numpy as np
import models
import torch
import pdb
import time
import datetime



def train(net, dataloader, optimizer, criterion, epoch):

    running_loss = 0.0
    total_loss = 0.0

    for i, data in enumerate(dataloader.trainloader, 0):
        # get the inputs
        image = data['image'].float()
        tag = data['tag']

        # zero the parameter gradients
        optimizer.zero_grad()

        # forward + backward + optimize
        outputs = net(image)
        # print(tag.shape)
        # print(outputs.shape)
        # print(tag)
        # temp = torch.tensor([0 for i in range(tag.shape[0])])
        # for i in range(tag.shape[0]):
        #     temp[i] = 0 if tag[i, 0] == 1 else 1
        # print(temp)
        loss = criterion(outputs, tag)  # using cross-entropy loss
        loss.backward()
        optimizer.step()

        # print statistics
        running_loss += loss.item()
        total_loss += loss.item()
        if (i + 1) % 10 == 0:    # print every 10 mini-batches
            print('[%d, %5d] loss: %.3f' %
                  (epoch + 1, i + 1, running_loss / 10))
            log('[%d, %5d] loss: %.3f' %
                  (epoch + 1, i + 1, running_loss / 10))
            running_loss = 0.0

    print('Final Summary:   loss: %.3f' %
          (total_loss / i))
    log('Final Summary:   loss: %.3f' %
          (total_loss / i))


def test(net, dataloader, run=''):
    correct = 0
    total = 0
    if run == 'Train':
        dataTestLoader = dataloader.trainloader
    else:
        dataTestLoader = dataloader.testloader
    with torch.no_grad():
        for data in dataTestLoader:
            image = data['image'].float()
            tag = data['tag']
            outputs = net(image)
            _, predicted = torch.max(outputs.data, 1)
            total += tag.size(0)
            correct += (predicted == tag).sum().item()

    print('%s Accuracy of the network: %d %%' % (run,
        100 * correct / total))
    log('%s Accuracy of the network: %d %%' % (run,
        100 * correct / total))

    class_correct = list(0. for i in range(2))
    class_total = list(0. for i in range(2))
    with torch.no_grad():
        for data in dataTestLoader:
            image = data['image'].float()
            tag = data['tag']
            outputs = net(image)
            _, predicted = torch.max(outputs, 1)
            c = (predicted == tag).squeeze()
            for i in range(len(tag)):
                label = tag[i]
                class_correct[label] += c[i].item()
                class_total[label] += 1


    for i in range(2):
        print('%s Accuracy of %5s : %2d %%' % (
            run, dataloader.classes[i], 100 * class_correct[i] / class_total[i]))
        log('%s Accuracy of %5s : %2d %%' % (
            run, dataloader.classes[i], 100 * class_correct[i] / class_total[i]))

def log(data):
    logFile.write(data + "\n")

def main():

    args = argParser()

    cifarLoader = YohoLoader(args)
    net = args.model()

    criterion = net.criterion()
    optimizer = net.optimizer()

    for epoch in range(args.epochs):  # loop over the dataset multiple times
        net.adjust_learning_rate(optimizer, epoch, args)
        train(net, cifarLoader, optimizer, criterion, epoch)
        if epoch % 4 == 0: # Comment out this part if you want a faster training
            test(net, cifarLoader, 'Train')
            test(net, cifarLoader, 'Test')
        torch.save(net, "weights/epoch" + str(epoch) + ".yoho")

    # print('The log is recorded in ')
    # print(net.logFile.name)

if __name__ == '__main__':
    ts = time.time()
    st = datetime.datetime.fromtimestamp(
        ts).strftime('%Y-%m-%d_%H:%M:%S_log.txt')
    logFile = open('logs/' + st, 'w')
    print('The log is recorded in ')
    print(logFile.name)
    main()
    print('The log is recorded in ')
    print(logFile.name)
    logFile.close()
    # args = argParser()
    # cifarLoader = YohoLoader(args)
    # net = torch.load("net.dat")
    # net.eval()
    # test(net, cifarLoader, 'Test')


