from PIL import Image
import os
import pandas as pd
import matplotlib.pyplot as plt
import cv2

# path to all images folder
filepath="C:/Users/Nunan/Documents/GitHub/CartoonDetection/raw_dataset/images"
for filename in os.listdir(filepath):
  for fileImg in os.listdir(filepath+"/"+filename):
    name,typeimg=fileImg.split('.')
    if(typeimg!="jpg"):
        image = Image.open(filepath+"/"+filename+"/"+fileImg).convert("RGBA")
        try:
            os.remove(filepath+"/"+filename+"/"+fileImg)
        except:
            print("Error while deleting file : ", filepath+"/"+filename+"/"+fileImg)
        new_image = Image.new("RGBA", image.size, "WHITE") # Create a white rgba background
        new_image.paste(image, (0, 0), image)              # Paste the image on the background. Go to the links given below for details.
        new_image.convert('RGB').save(filepath+"/"+filename+"/"+name+'.jpg', "JPEG")  # Save as JPEG
        print("change "+fileImg+" to jpg")