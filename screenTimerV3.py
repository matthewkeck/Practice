## Matthew R Keck 6/3/2022

from win32gui import GetWindowText, GetForegroundWindow
from datetime import datetime
import subprocess
import calendar
import time
import pickle

screenTimeDic = {}
prevactivity = ''
my_date = datetime.today()
print(my_date)
print(type(my_date))
dayName = calendar.day_name[my_date.weekday()]

screenTimeFile = open("screenData","rb")
screenTimeDic = pickle.load(screenTimeFile)
screenTimeFile.close()

def screen_timer(prevactivity):
    
    startTime = time.time()
    while True:
        time.sleep(1)
        activity = GetWindowText(GetForegroundWindow())
        
        if activity != prevactivity:

            endTime = time.time()
            currentTime = endTime - startTime

            if "https://www" not in prevactivity and prevactivity != '' and prevactivity != 'Windows Default Lock Screen':

                prevactivity = prevactivity + ' - ' + dayName
                
                if prevactivity in  screenTimeDic:
                
                    screenTimeDic[prevactivity][0] += currentTime

                if prevactivity not in screenTimeDic:
                    tempList = [currentTime,my_date]
                    screenTimeDic[prevactivity] = tempList

                Time = seconds_to_time(currentTime)

                print(screenTimeDic[prevactivity])
                ##print(prevactivity, " : ",Time)

            screenTimeFile = open("screenData","wb")
            pickle.dump(screenTimeDic, screenTimeFile)
            screenTimeFile.close()
            
            prevactivity = activity
            
            return(screen_timer(prevactivity))

        else:
            endTime = time.time()
            currentTime = endTime - startTime
            

def seconds_to_time(seconds):

    minutes = seconds / 60
    seconds = (minutes - int(minutes))*60
    hours = minutes / 60
    minutes = (hours - int(hours))*60

    hours = int(hours)
    minutes = int(minutes)
    seconds = int(seconds)

    Time = str(hours) + ':' + str(minutes) + ':' + str(seconds)

    return(Time)


screen_timer(prevactivity)
