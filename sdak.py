# Import statments
import shelve

# Definitions of global variables
mainMenuPrint: str = "Main Menu: \n[1] New Data \n[2] Open Data \n[3] Save Data \n[4] View Data \n[5] Edit Data \n[6]" \
                     " Show Save File Path \n[7] Check Concordant Results \n[8] Average Data\n[9] Plot Graph " \
                     "\n[10] Help"
firstStart: bool = True
anyData: bool = False
dataSaved: bool = False
yesNo = ''
seeData = ''
DataFile: str = ''


# Setting up definitions of functions
def firstTime():
    global firstStart
    while firstStart:
        print(
            'Welcome to SciLabs, this is an interface to help with data analysis for sciences \nPlease remmeber to '
            'enter the value shown in the [], but without the surrounding []')
        firstStart = False

def yesNo():
    yesNo = str(input('Enter [Y]es or [N]o:\n'))
    if yesNo == 'Y':
        return True
    elif yesNo == 'N':
        return False
    else:
        errorOut(1)


def fileLoc():
    print('Please enter the file location with .dat after it. This should either be relative to where the current '
          'program is being run or an absolute path. If unsure please type \'help\'')
    location = str(input('Enter file path or help:\n'))
    if location == 'help':
        help(filelocation)
    else:
        return location

def openData():
    print('This is only for when there is a file already present. If you want to create a file, from the main menu '
          'type \'1\' for \'New Data\'')
    global f
    f = shelve.open(fileLoc(), flag='w', writeback=True)
    print('Do you want to see the contence?')
    yesNo()
    if yesNo:
        viewData()
    else:
        pass


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
    if topic == 'main':
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
        help('main')
    else:
        errorOut(1)

# main program loop
while True:
    mainMenu()
