# Importing the required dependencies
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import cv2
import PIL.Image
import requests
import urllib
import os
from keras.preprocessing.image import array_to_img,img_to_array,load_img
import matplotlib.pyplot as plt
class get_image:
	def __init__(self,loc_dict,path):
		self.loc=loc_dict
		self.path_to_write=path
		self.base_url="http://www.image-net.org/api/text/imagenet.synset.geturls?{}={}".format(self.loc.values(),self.loc.keys())
	# Path to write the images
	#path_to_write= "/content/train1/ships"
	def get_image(url):
  		img = requests.get(base_url)
  		soup = BeautifulSoup(img.content,"html.parser")
  		soup = str(soup)
  		soup= soup.split("\r\n")
  		i=1
  		for img_path in soup:
    			resp=requests.get(img_path).content
    			image = np.asarray(bytearray(resp), dtype="uint8")
    			image= cv2.imdecode(image,cv2.IMREAD_COLOR)
    			f_path=os.path.join(path_to_write,"ship"+str(i)+".jpg")
    			cv2.imwrite(f_path,image)

