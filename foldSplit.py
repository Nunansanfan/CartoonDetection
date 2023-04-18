import os,random
import shutil

def countFile(folderpath):
    return len(os.listdir(folderpath))
    
def findInd(imgName):
    return img_list.index(imgName)


path_to_img_files = r"C:\Users\Nunan\Documents\GitHub\CartoonDetection\raw_dataset\images"  # Insert your path to images folder here
path_to_txt_files = r"C:\Users\Nunan\Documents\GitHub\CartoonDetection\raw_dataset\labels"  # Insert your path to label folder here
label_list = []
img_list = []

#------------ img_list & label_list can be map by index ------------
for root, dir, files in os.walk(path_to_txt_files):
    for label in files:
        label_list.append(label)
for root, dir, files in os.walk(path_to_img_files):
    for image in files:
        img_list.append(image)

# iterate through each folder
for imgFolderName in os.listdir(path_to_img_files):
    pathToImageFolder=path_to_img_files+"/"+imgFolderName
    pathToTextFolder = path_to_txt_files+"/"+imgFolderName

    # this list contain only image name for each folder
    imgInFolList=[]
    for imgname in os.listdir(pathToImageFolder):
        imgInFolList.append(imgname)

    # 4 fold, calculate numbers of image per fold 
    numImage=len(imgInFolList)
    perFold=int(numImage/4)

    # prepare to random copy image to "Fold" folder
    remainIndexImg=[i for i in range(numImage)]
    pathFold="C:/Users/Nunan/Documents/GitHub/CartoonDetection/Folds/Fold"
    # first 3 fold equally
    for i in range(3):
        print("Fold "+str(i+1)+"---------------------------------")
        pathImageFold=pathFold+str(i+1)+"/images"
        pathLabelFold=pathFold+str(i+1)+"/labels"
        for j in range(perFold):
            random_num = random.choice(remainIndexImg)
            remainIndexImg.remove(random_num)
            shutil.copyfile(pathToImageFolder+"/"+imgInFolList[random_num], pathImageFold+"/"+imgInFolList[random_num])
            shutil.copyfile(pathToTextFolder+"/"+label_list[findInd(imgInFolList[random_num])], pathLabelFold+"/"+label_list[findInd(imgInFolList[random_num])])
            print("Random "+str(random_num)+": successfully copy image and label of ->"+imgInFolList[random_num]+"<- to Fold "+str(i+1))


    # what is remain from first 3 fold will be in 4th Fold
    pathImageFold=pathFold+str(4)+"/images"
    pathLabelFold=pathFold+str(4)+"/labels"
    for ind in remainIndexImg:
        shutil.copyfile(pathToImageFolder+"/"+imgInFolList[ind], pathImageFold+"/"+imgInFolList[ind])
        shutil.copyfile(pathToTextFolder+"/"+label_list[findInd(imgInFolList[ind])], pathLabelFold+"/"+label_list[findInd(imgInFolList[ind])])
        print("Random "+str(ind)+": successfully copy image and label of ->"+imgInFolList[ind]+"<- to Fold 4")

