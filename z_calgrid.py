import calendar
calendar.setfirstweekday(calendar.SUNDAY)
from z_times import getYMD

def getGrid(Y=None, M=None):
    if not Y or not M: Y, M, D = getYMD()
    prevMo = getPrevMonth(Y, M)
    prevMoLWk = prevMo[-1]
    thisMo = getThisMonth(Y, M)
    nextMo = getNextMonth(Y, M)
    nextMoFWk = nextMo[0]
    DEX = 0
    for day in thisMo[0]: # first week of the month
        if not day:
            thisMo[0][DEX] = prevMoLWk[DEX]
        DEX += 1
    DEX = 0
    for day in thisMo[-1]: # last week of the month
        if not day:
            thisMo[-1][DEX] = nextMoFWk[DEX]
        DEX += 1
    return thisMo

def getPrevMonth(Y=None, M=None):
    if not Y or not M: Y, M, D = getYMD()
    lY, lM = Y, M - 1
    if M == 1: lY, lM = Y-1, 12
    return convertGrid(lY, lM, calendar.monthcalendar(lY, lM))

def convertGrid(Y, M, GRID):
    FINAL = []
    for week in GRID:
        NEWWEEK = []
        for day in week:
            if day:
                T = (Y, M, day)
                NEWWEEK.append(T)
            else:
                NEWWEEK.append(0)
        FINAL.append(NEWWEEK)
    return FINAL

def getThisMonth(Y=None, M=None):
    if not Y or not M: Y, M, D = getYMD()
    return convertGrid(Y, M, calendar.monthcalendar(Y,M))

def getNextMonth(Y=None, M=None):
    if not Y or not M: Y, M, D = getYMD()
    nY, nM = Y, M + 1
    if M == 12: nY, nM = Y + 1, 1
    return convertGrid(nY, nM, calendar.monthcalendar(nY, nM))

