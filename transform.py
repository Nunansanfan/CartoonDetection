import cv2
import os
from PIL import Image
import shutil


def colorshift1(img):
  return cv2.cvtColor(img, cv2.COLOR_BGR2XYZ)

def colorshift2(img):
  return cv2.cvtColor(img, cv2.COLOR_RGB2XYZ) 

def findInd(imgName):
    return img_list.index(imgName)

path_to_img_files = r"C:\Users\Nunan\Documents\GitHub\CartoonDetection\raw_dataset\images"  # Insert your path to images folder here
path_to_txt_files = r"C:\Users\Nunan\Documents\GitHub\CartoonDetection\raw_dataset\labels"  # Insert your path to label folder here
label_list = []
img_list = []

for root, dir, files in os.walk(path_to_txt_files):
    for label in files:
        label_list.append(label)
for root, dir, files in os.walk(path_to_img_files):
    for image in files:
        img_list.append(image)
#------------ img_list & label_list can be map by index ------------
# for i in range(len(label_list)):
#     print("image : "+img_list[i]+", label : "+label_list[i])
# path="C:\Users\Nunan\Documents\GitHub\CartoonDetection\raw_dataset"

for imgFolderName in os.listdir(path_to_img_files):
   
    pathToImageFolder=path_to_img_files+"/"+imgFolderName
    pathToTextFolder = path_to_txt_files+"/"+imgFolderName

    for imgName in os.listdir(pathToImageFolder):
        fileRawName=str(imgName.split(".")[0])
        input_img = cv2.imread(pathToImageFolder+"/"+imgName)
        
        # color shift 1 : save new image and copy old label (new name = oldname_color1.jpg & oldname_color1.txt)
        shiftColorImg1=colorshift1(input_img)
        cv2.imwrite(pathToImageFolder+"/"+fileRawName+"_color1.jpg",shiftColorImg1)
        shutil.copyfile(pathToTextFolder+"/"+label_list[findInd(imgName)], pathToTextFolder+"/"+fileRawName+"_color1.txt")
        
        # color shift 2 : save new image and copy old label (new name = oldname_color2.jpg & oldname_color2.txt)
        shiftColorImg2=colorshift2(input_img)
        cv2.imwrite(pathToImageFolder+"/"+fileRawName+"_color2.jpg",shiftColorImg2)
        shutil.copyfile(pathToTextFolder+"/"+label_list[findInd(imgName)], pathToTextFolder+"/"+fileRawName+"_color2.txt")

        print("Done: save 2 color shift images of ->"+imgName+"<- and copied label")
