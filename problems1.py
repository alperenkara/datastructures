# converting minutes to hours

def convertToMinute(num):
    # find the hour
    # import math
    # hour = int(math.floor(num/60))
    hour = num//60
    # find the minutes
    minutes = num%60
    # merge them
    result  = "hour: {} minutes: {}".format(hour,minutes)
    return print(result)

convertToMinute(128)