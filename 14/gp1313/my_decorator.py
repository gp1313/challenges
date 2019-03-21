import cv2
import numpy as np

from functools import wraps

def to_gray_scale(func):

    @wraps(func)
    def decorator(*args):
        print(args[0].shape)
        func(*args)

    return decorator

@to_gray_scale
def show_image(img_arr, window_name):

    cv2.namedWindow(window_name, 0)
    cv2.imshow(window_name, img_arr)
    cv2.waitKey(0)

def main():
    img_path = 'dog.jpg'
    img_arr = cv2.imread(img_path, -1)
    assert img_arr is not None
    show_image(img_arr, 'Test')

if __name__ == '__main__':
    main()
