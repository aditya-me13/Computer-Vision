import pdb
import glob
import cv2
import os

from functions.Helpers.Master import stitch_multiple_images

class PanaromaStitcher():
    def __init__(self):
        pass

    def make_panaroma_for_images_in(self,path):
        imf = path
        all_images = sorted(glob.glob(imf+os.sep+'*'))
        print('Found {} Images for stitching'.format(len(all_images)))

        ####  Your Implementation here
        #### you can use functions, class_methods, whatever!! Examples are illustrated below. Remove them and implement yours.
        #### Just make sure to return final stitched image and all Homography matrices from here
        
        return stitch_multiple_images(path)

    # def say_hi(self):
    #     print('Hii From John Doe..')
    
    # def do_something(self):
    #     return None
    
    # def do_something_more(self):
    #     return None