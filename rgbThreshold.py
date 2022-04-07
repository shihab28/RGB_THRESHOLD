import os, sys, json
import cv2 as cv2
import numpy as np

rootDir = os.path.dirname(__file__).replace("\\", "/")
ImageDir = f"{rootDir}/resources/image"
ScriptDir = f"{rootDir}/resources/scripts"

redMin = np.array([50, 0, 0])
redMax = np.array([255, 125, 125])

grnMax = np.array([0, 20, 0])
grnMin = np.array([180, 255, 150])

bluMin = np.array([0, 0, 20])
bluMax = np.array([140, 200, 255])

imageExtList = ['png', 'jpg', "jepg", "ico", "gif", "bmp"]


def getExtension(tempName=None):
    
    try:
        nameList = tempName.split(".")
        if len(nameList) > 1:
            return nameList[-1]
    except Exception as e:
        print(e)      
    return None

def getNameOnly(tempName=None): 
    try:
        nameList = tempName.split(".")
        if len(nameList) > 1:
            return '.'.join(nameList[ : -1])
    except Exception as e:
        print(e)      
    return None

def loadImage(tempDir=ImageDir):
    imageDict = {}

    imageDirList = os.listdir(tempDir)

    for imName in imageDirList:
        imPath = f"{tempDir}/{imName}"
        print(imPath)
        if os.path.isfile(imPath) and getExtension(imName).lower() in imageExtList:
            imageDict[getNameOnly(imName)] = {}
            mainImage = cv2.imread(imPath, cv2.IMREAD_UNCHANGED)
            mainImage = cv2.resize(mainImage, (256, 256), interpolation=cv2.INTER_NEAREST)
            imageDict[getNameOnly(imName)]['image'] = mainImage
            mainImage = cv2.cvtColor(mainImage, cv2.COLOR_BGR2HSV)
            
            redMask = cv2.inRange(mainImage, redMin, redMax)
            redImage = cv2.bitwise_and(mainImage, mainImage, mask=redMask)
            imageDict[getNameOnly(imName)]['red'] = redImage

            grnMask = cv2.inRange(mainImage, grnMin, grnMax)
            grnImage = cv2.bitwise_and(mainImage, mainImage, mask=grnMask)
            imageDict[getNameOnly(imName)]['green'] = grnImage

            bluMask = cv2.inRange(mainImage, bluMin, bluMax)
            bluImage = cv2.bitwise_and(mainImage, mainImage, mask=bluMask)
            imageDict[getNameOnly(imName)]['blue'] = bluImage

    return imageDict

def printDict(tempCont):
    if type(tempCont) == list:
        for cont in tempCont:
            print(cont)

    elif type(tempCont) == dict:
        print(json.dumps(tempCont, indent=3))




if __name__ == "__main__":
    imageDictionary = loadImage()
    print(imageDictionary)

    for imName in imageDictionary:
        for imType in imageDictionary[imName]:
            pass
            cv2.imshow(f"{imType}", imageDictionary[imName][imType])
        # cv2.imshow(f"{imType}", imageDictionary[imName]['image'])

        wk = cv2.waitKey(0)









