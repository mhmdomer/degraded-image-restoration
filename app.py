from random import random
import cv2
import glob
import random
from noise import noisy
import os

masks = list(glob.iglob('masks/*.*', recursive=True))
images = list(glob.iglob('VOC2007/JPEGImages/*.*', recursive=True))
path = '/mnt/FCD48261D4821DD0/Vampire/University/10th Sem/Graduation Project/VOC2007/distortedJPEGImages'

def main():
    for image in images:
        img = cv2.resize(cv2.imread(image),(1000,750))
        mask = cv2.resize(cv2.imread(random.choice(masks)),(1000,750))
        if random.randint(0, 1) == 0:
            newImage = cv2.add(img,mask)
        else:
            newImage = cv2.subtract(img,mask)
        newImage = noisy('s&p', newImage)
        cv2.imwrite(os.path.join(path, os.path.basename(os.path.normpath(image))), newImage)

main()

