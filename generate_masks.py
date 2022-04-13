from random import random
import cv2
import random
import glob

masks = list(glob.iglob('masks/*.*', recursive=True))

def generate_new_masks():
    for i in range(16,27):
        m1 = cv2.resize(cv2.imread(random.choice(masks)),(1000,750))
        m2 = cv2.resize(cv2.imread(random.choice(masks)),(1000,750))
        if random.randint(0, 1) == 0:
            newImage = cv2.add(m1,m2)
        else:
            newImage = cv2.subtract(m1,m2)
        cv2.imwrite('masks/'+str(i)+'.jpg', newImage)