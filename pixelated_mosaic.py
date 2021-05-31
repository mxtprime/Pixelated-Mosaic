from PIL import Image
import math

''' Hello and welcome to my Final project for code in place ,
###########################################
WATCH THIS
https://www.youtube.com/watch?v=f1fXCRtSUWU
###########################################
This project is the automated python version of that using PIL library . 
In the video 2 passes were done , this code works well with 10 passes(depending on image size )
above 10 passes , the image becomes unrecoginzable 
even number of passes gives the best results i.e 2,4,6,8,10...

crop_width will also dictate the resolution , smaller is better
'''

def main():
    im = Image.open(r"C:\Users\")  # Add file path for your image 
    # crop width will dictate the "resolution" of the mosaic , smaller is better
    crop_width = 1
    number_of_passes = int(input("How many passes would like to perform on the image?: "))
    n = 0
    while n < number_of_passes: 
        a = image_mosaic(im, crop_width)
        b = a.rotate(90, expand = True)
        im = b
        n += 1
    
    im.rotate(-90*n, expand =True).show()

if __name__ == '__main__':
    main()


def round_down(n):
    ''' this function will return the same number n except replacing the
    last digit by zero , making the number divisible by 10'''
    a = str(n)
    b = a[:-1] + str(0)
    return int(b)

def resize(image):
    ''' this function resizes the image width 
    and height by rounding down the second digit 
    so if image width is 745 it will resize to 740'''
    w = round_down(image.width)
    h = round_down(image.height)
    resize = image.resize((w,h))
    return resize


def make_list(image, k):
    '''returns list of co-ordinates to be used to crop image strips'''
    width = image.width
    height = image.height
    m_list =[]
    n = width//k
    # intializing list 
    x = 0
    y = 0
    w = k
    z = height
    for i in range(n+1):
        m_list.append((x, y, w, z))
        x = x + k
        y = 0
        w = w + k
    return m_list


def image_crop(image,crop_width):
    '''returns the cropped images based on co-ordinates from make_list function , f(resize) is 
    also used to convert last digit of image height and width to zero
    crop width is a value to indicate the width of the crop larges crop will translate to lower
    resolution and vice versa'''

    image = resize(image)
    crop_list = make_list(image, crop_width)
    images_even = []
    images_odd = []
    counter = 0
    for i in crop_list:
        c = image.crop(i)
        if counter == 0 or counter%2 == 0:
            images_even.append(c)
            counter += 1
        else:
            images_odd.append(c)
            counter += 1
    return [images_even , images_odd]

def image_mosaic(image, crop_width):
    '''returns combined image which is the the cropped images of even put togather and the 
    cropped images of odd put togather side by side'''
    image_list = image_crop(image, crop_width)
    combined = []
    for image in image_list:
        x,y = 0,0
        image_len = len(image)-1
        size = (image_len * crop_width, image[0].height)
        stiched_image = Image.new('RGB', size, (255,255,255))
        for strip in image:
            stiched_image.paste(strip, (x,y))
            x = x + crop_width
        combined.append(stiched_image)
    
    c_size = ((combined[0].width + combined[1].width), combined[0].height)
    combined_image = Image.new('RGB', c_size, (255,255,255))
    n,m = 0,0
    for i in combined:
        combined_image.paste(i, (n,m))
        n = n + i.width
    return combined_image






 
