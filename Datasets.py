import os


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


## Dataset Folders
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
 

## DataSet Files
AnamolyFiles = [x for x in AnamolyDataFolder if x.endswith(".jpg")]

BlueMouseNormalFiles = [x for x in BlueMouseNormalFolder if x.endswith(".jpg")]
BlueMouseAbnormalFiles = [x for x in BlueMouseAbnormalFolder if x.endswith(".jpg")]

BlackMouseNormalFiles = [x for x in BlackMouseNormalFolder if x.endswith(".jpg")]
BlackMouseAbnormalFiles = [x for x in BlackMouseAbnormalFolder if x.endswith(".jpg")]

EmptyRoadFiles = [x for x in EmptyRoadFolder if x.endswith(".jpg")]
ExtrasFiles = [x for x in ExtrasFolder if x.endswith(".jpg")]
MergedTestFiles = [x for x in MergedTestFolder if x.endswith(".jpg")]

TestVideosFiles = [x for x in TestVideosFolder if x.endswith(".mp4")]
