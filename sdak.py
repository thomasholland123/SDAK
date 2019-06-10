import shelve

mainMenuPrint: str = "Main Menu: \n[1] New Data \n[2] Open Data \n[3] Save Data \n[4] View Data \n[5] Edit Data \n[6]" \
                     " Show Save File Path \n[7] Check Concordant Results \n[8] Average Data\n[9] Plot Graph \n[10] Help"
firstStart: bool = True
anyData: bool = False
dataSaved: bool = False
yesNo = ''
seeData = ''
DataFile: str = ''

def firstTime():
    global firstStart
    while firstStart == True:
        print('Welcome to SciLabs, this is an interface to help with data analysis for sciences \nPlease remmeber to enter the value shown in the [], but without the surrounding []')
        firstStart = False


def openData():



def errorOut(state):
    print('There has been an error:')
    if state == 1:
        print('Input not recognised, please try again\n')
    elif state == 2:
        print('No data present, please create data\n')
    elif state == 3:
        print('Help for this topic not here, please go to https://github.com/thomasholland123/SDAK/wiki')
    else:
        print('Big problem: Error not known!\n')

def help(topic):
    print('Welcome to the Help')
    if topic == main:
        print('Please go to https://github.com/thomasholland123/SDAK/wiki for all the help topics.')
    else:
        errorOut(3)
  

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
    elif menuInput == 10:
        help(main)
    else:
        errorOut(1)


while True:
    mainMenu()
