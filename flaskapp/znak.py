import sys 
import os 
import numpy as np 
from PIL import Image
import matplotlib.pyplot as plt
import scipy.ndimage.interpolation as interp

height = 224
width = 224

def read_image_files(dir_name):
    image_box = Image.open(dir_name).convert("RGB") # / ?? 
    return image_box

def imageModule2(image_box):
    

    images_resized = np.array([np.array( image_box.resize( (height,width) ) )/255.0 ])
    #images_resized = np.array( image_box.resize( (height,width)) ) /255.0
    image_ = images_resized[0].copy()

    return image_

def znakView(image_copy):
     
    # с изменением исходного размера массива
    image_rot_r = interp.rotate(input=image_copy, angle=45, axes=(0,1), reshape = True)
    # меняем масштаб изображения
    image_interp = interp.zoom(image_rot_r,(0.3,0.3,1))


    for x in range(0,len(image_interp)):
        for y in range(0,len(image_interp[0])):
            r, g, b = image_copy[x, y, 0:3]
            r1 , g1, b1= image_interp[x, y, 0:3]
            image_copy[x, y, 0:3] = (0.5 * r + 0.5 * r1,  0.5 * g + 0.5 * g1, 0.5 * b + 0.5 * b1)
    return image_copy

def znak(filename):

    #filename = os.path.join('data', 'image.jpg')
    image_box = read_image_files(filename) 

    fig = plt.figure(figsize=(5,5)) # задаем размер фигуры
    width = height = int(1**0.5)
    print(image_box) 
    viewer = [[]]*1 # массив саб графиков
    
    image_copy = imageModule2(image_box)
    image_copy = znakView(image_copy)

    viewer = fig.add_subplot(width,height,1) 
    viewer.imshow(image_copy) # делаем график изображения 

    plt.show()

