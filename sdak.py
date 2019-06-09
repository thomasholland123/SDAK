from matplotlib import *
from numpy import *
from scipy import *
from pandas import *

mainMenuPrint: str = "Main Menu: \n[1] New Data \n[2] Open Data \n[3] Save Data \n[4] View Data \n[5] Edit Data \n[6]" \
                     " Show Save File Path \n[7] Check Concordant Results \n[8] Average Data\n[9] Plot Graph"
firstStart: bool = True
anyData: bool = False
dataSaved: bool = False
contin = False
yesNo = ''
seeData = ''
DataFile: str = ''

def firstTime():
    global firstStart
    while firstStart == True:
        print('Welcome to SciLabs, this is an interface to help with data analysis for sciences \nPlease remmeber to enter the value shown in the [], but without the surrounding []')
        firstStart = False

def viewData():
    global anyData
    global DataFile

        

def saveYesNo():
    global yesNo
    while yesNo not in ('Y', 'N'):
        yesNo = input('Do you want to save: \n[Y]es \n[N]o:\n')
        if yesNo == 'Y':
            saveData()
            break
        elif yesNo == 'N':
            pass
            break
        else:
            errorOut(1)

def openData():
    global seeData
    global dataSaved
    global path
    global DataFile
    if dataSaved == False:
            print('Current Data is not saved')
            saveYesNo()
    else:
        pass
    path = str(input('Enter file path \nShould be a .txt file in current directory where this program is running from:\n'))
    DataFile = open(path, 'r+')

    while seeData not in ('Y', 'N'):
        seeData = str(input('Do you want to see your data: \n[Y]es \n[N]o: \n'))
        if seeData == 'Y':
            viewData()
        elif seeData == 'N':
            pass
        else:
            errorOut(1)


def errorOut(state):
    print('There has been an error:')
    if state == 1:
        print('Input not recognised, please try again\n')
    elif state == 2:
        print('No data present, please create data\n')
    else:
        print('Big problem: Error not known!\n')


def mainMenu():
    firstTime()

    print(mainMenuPrint)
    menuInput: int = int(input('Enter option:'))

    if menuInput == 2:
        openData()
    elif menuInput == 3:
        saveData()
    elif menuInput == 4:
        viewData()
    elif menuInput == 5:
        editData()
    elif menuInput == 6:
        fileLoc()
    elif menuInput == 7:
        checkConcord()
    elif menuInput == 8:
        averageData()
    elif menuInput == 9:
        plotGraph()
    elif menuInput == 1:
        newData()
    else:
        errorOut(1)


while True:
    mainMenu()
