import time, calendar

def get_year():
    return time.localtime(time.time())[0]

def isToday(Y, M, D):
    if (Y, M, D) == getYMD():
        return True

def getYMD():
    return getNowT()[:3]

def getNowT():
    return time.localtime(time.time())

def get_int_from_YMD (Y, M, D):
    return calendar.timegm((int(Y), int(M), int(D), 0, 0, 0, 0, 1, -1))

def get_tuple_from_YMD (Y, M, D):
    return time.gmtime(get_int_from_YMD (Y, M, D))
