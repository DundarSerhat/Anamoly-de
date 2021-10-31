import os
import json


SeperatedDataName = 'Raw Data\Separeted Data\\'
Anamoly = SeperatedDataName + 'Anamoly\\'
BlueMouseNormal = SeperatedDataName + 'Blue Mouse - Normal\\'
BlueMouseAbnormal = SeperatedDataName + 'Blue Mouse - Abnormal\\'
BlackMouseNormal = SeperatedDataName + 'Black Mouse - Normal\\'
BlackMouseAbnormal = SeperatedDataName + 'Black Mouse - Abnormal\\'
EmptyRoad = SeperatedDataName + 'Empty Road\\'
Extras = SeperatedDataName + 'Extras\\'
MergedTest = SeperatedDataName + 'Merged Test\\'
TestVideos = 'Raw Data\Test Videos\\'


# Raw Data Folders
SeparatedDataFolder = os.listdir(SeperatedDataName)

AnamolyDataFolder = os.listdir(Anamoly)

BlueMouseNormalFolder = os.listdir(BlueMouseNormal)
BlueMouseAbnormalFolder = os.listdir(BlueMouseAbnormal)

BlackMouseNormalFolder = os.listdir(BlackMouseNormal)
BlackMouseAbnormalFolder = os.listdir(BlackMouseAbnormal)

EmptyRoadFolder = os.listdir(EmptyRoad)
ExtrasFolder = os.listdir(Extras)
MergedTestFolder = os.listdir(MergedTest)

TestVideosFolder = os.listdir(TestVideos)


# DataSet Files
AnamolyFiles = [(Anamoly + x) for x in AnamolyDataFolder if x.endswith(".jpg")]

BlueMouseNormalFiles = [(BlueMouseNormal + x)
                        for x in BlueMouseNormalFolder if x.endswith(".jpg")]
BlueMouseAbnormalFiles = [(BlueMouseAbnormal + x)
                          for x in BlueMouseAbnormalFolder if x.endswith(".jpg")]

BlackMouseNormalFiles = [(BlackMouseNormal + x)
                         for x in BlackMouseNormalFolder if x.endswith(".jpg")]
BlackMouseAbnormalFiles = [(BlackMouseAbnormal + x)
                           for x in BlackMouseAbnormalFolder if x.endswith(".jpg")]

EmptyRoadFiles = [(EmptyRoad + x)
                  for x in EmptyRoadFolder if x.endswith(".jpg")]
ExtrasFiles = [(Extras + x) for x in ExtrasFolder if x.endswith(".jpg")]
MergedTestFiles = [(MergedTest + x)
                   for x in MergedTestFolder if x.endswith(".jpg")]

TestVideosFiles = [(TestVideos + x)
                   for x in TestVideosFolder if x.endswith(".mp4")]


# Dataset Folders
DatasetFolder = 'Dataset\\'
BlueMouseDS = DatasetFolder + 'BlueMouse\\'
BlueMouseAbnormalDS = DatasetFolder + 'BlueMouseAbnormal\\'
BlackMouseDS = DatasetFolder + 'BlackMouse\\'
BlackMouseAbnormalDS = DatasetFolder + 'BlackMouseAbnormal\\'

BlueMouseDSList = os.listdir(BlueMouseDS)
BlueMouseDSFiles = [(BlueMouseDS + x)
                        for x in BlueMouseDSList if x.endswith(".jpg")]

BlueMouseAbDSList = os.listdir(BlueMouseAbnormalDS)
BlueMouseABDSFiles = [(BlueMouseAbnormalDS + x)
                        for x in BlueMouseAbDSList if x.endswith(".jpg")]


BlackMouseDSList = os.listdir(BlackMouseDS)
BlackMouseDSFiles = [(BlackMouseDS + x)
                        for x in BlackMouseDSList if x.endswith(".jpg")]

BlackMouseAbDSList = os.listdir(BlackMouseAbnormalDS)
BlackMouseABDSFiles = [(BlackMouseAbnormalDS + x)
                        for x in BlackMouseAbDSList if x.endswith(".jpg")]



Labels = ['BlueMouse', 'BlueMouseAbnormal', 'BlackMouse', 'BlackMouseAbnormal', 'Anamoly']

BlueDatasets = [ 
    {
        "Label": "BlueMouse",
        "RawFiles": BlueMouseNormalFiles,
        "DatasetPath": BlueMouseDS,
        "Datasets": BlueMouseDSFiles
    },
    {
        "Label": "BlueMouseAbnormal",
        "RawFiles": BlueMouseAbnormalFiles,
        "DatasetPath": BlueMouseAbnormalDS,
        "Datasets": BlueMouseABDSFiles
    }
]

BlackDatasets = [
    {
        "Label": "BlackMouse",
        "RawFiles": BlackMouseNormalFiles,
        "DatasetPath": BlackMouseDS,
        "Datasets": BlackMouseDSFiles
    },
    {
        "Label": "BlackMouseAbnormal",
        "RawFiles": BlackMouseAbnormalFiles,
        "DatasetPath": BlackMouseAbnormalDS,
        "Datasets": BlackMouseABDSFiles
    }
  
]

print(BlackDatasets[0]["Datasets"])