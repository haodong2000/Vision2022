# -*- coding: utf-8 -*-

import cv2
from IPython import display
from torchvision.datasets import MNIST, FashionMNIST
from torchvision import transforms
import time


def show_image(path):
    print(path)
    img = cv2.imread(path)
    cv2.imshow("kitty", img)
    key = cv2.waitKey(0)
    if key == 'q' or key == '27':
        # `27` is ESC
        cv2.destroyAllWindows()


def download_mnist():
    transform = transforms.Compose([transforms.ToTensor()])
    data_train = MNIST(root="../data/",
                       transform=transform,
                       train=True,
                       download=True)
    data_test = MNIST(root="../data/",
                      transform=transform,
                      train=False)
    data_fa_train = FashionMNIST(root="../data/",
                                 transform=transform,
                                 train=True,
                                 download=True)
    data_fa_test = FashionMNIST(root="../data/",
                                transform=transform,
                                train=False)


if __name__ == '__main__':
    download_mnist()
    show_image("./images/cat.jpg")
