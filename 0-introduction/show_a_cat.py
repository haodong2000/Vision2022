# -*- coding: utf-8 -*-

import cv2
from IPython import display
from torchvision.datasets import MNIST, FashionMNIST
from torchvision import transforms
import time
import torch
import tensorflow as tf

def gpu_information():
    print("torch.__version__ ->", torch.__version__)
    print("tensorflow.__version__ ->", tf.__version__)
    print(torch.cuda.is_available())
    # let's see the list of CUDA architectures, and the device name
    if torch.cuda.is_available():
        print(torch.cuda.get_device_name(device=None), torch.cuda.get_arch_list())
    print(tf.test.is_gpu_available())
    # tf.test.is_gpu_available() is deprecated and will be removed soon
    print(tf.config.list_physical_devices('GPU') )

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
    gpu_information()
