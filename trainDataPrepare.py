import os
from PIL import Image
import shutil

pathFold1="C:/Users/Nunan/Documents/GitHub/CartoonDetection/Folds/Fold1"
pathFold2="C:/Users/Nunan/Documents/GitHub/CartoonDetection/Folds/Fold2"
pathFold3="C:/Users/Nunan/Documents/GitHub/CartoonDetection/Folds/Fold3"
pathFold4="C:/Users/Nunan/Documents/GitHub/CartoonDetection/Folds/Fold4"
pathFold5="C:/Users/Nunan/Documents/GitHub/CartoonDetection/Folds/Fold5"
listPathFold=[pathFold1,pathFold2,pathFold3,pathFold4,pathFold5]

pathFold1Val="C:/Users/Nunan/Documents/GitHub/CartoonDetection/Train_data/Fold1Val"
pathFold2Val="C:/Users/Nunan/Documents/GitHub/CartoonDetection/Train_data/Fold2Val"
pathFold3Val="C:/Users/Nunan/Documents/GitHub/CartoonDetection/Train_data/Fold3Val"
pathFold4Val="C:/Users/Nunan/Documents/GitHub/CartoonDetection/Train_data/Fold4Val"
pathFold5Val="C:/Users/Nunan/Documents/GitHub/CartoonDetection/Train_data/Fold5Val"
listTrainPath=[pathFold1Val,pathFold2Val,pathFold3Val,pathFold4Val,pathFold5Val]

testpath="C:/Users/Nunan/Documents/GitHub/CartoonDetection/Test_dataset"
# index for train path
for itrain in range(5):
    # copy test images to folder
    for filename in os.listdir(testpath+"/images"):
        rawName,type=filename.split(".")
        shutil.copyfile(testpath+"/images/"+filename,listTrainPath[itrain]+"/images/test/"+filename)
        shutil.copyfile(testpath+"/labels/"+rawName+".txt",listTrainPath[itrain]+"/labels/test/"+rawName+".txt")
    print("copy test data to Fold"+str(itrain+1)+"Val/test")
    # index for fold path
    for ifold in range(5):
        if ifold==itrain:
            for filename in os.listdir(listPathFold[ifold]+"/images"):
                rawName,type=filename.split(".")
                shutil.copyfile(listPathFold[ifold]+"/images/"+filename,listTrainPath[itrain]+"/images/val/"+filename)
                shutil.copyfile(listPathFold[ifold]+"/labels/"+rawName+".txt",listTrainPath[itrain]+"/labels/val/"+rawName+".txt")
            print("copy fold "+str(ifold+1)+" to Fold"+str(itrain+1)+"Val/val")
        else:
            for filename in os.listdir(listPathFold[ifold]+"/images"):
                rawName,type=filename.split(".")
                shutil.copyfile(listPathFold[ifold]+"/images/"+filename,listTrainPath[itrain]+"/images/train/"+filename)
                shutil.copyfile(listPathFold[ifold]+"/labels/"+rawName+".txt",listTrainPath[itrain]+"/labels/train/"+rawName+".txt")
            print("copy fold "+str(ifold+1)+" to Fold"+str(itrain+1)+"Val/train")