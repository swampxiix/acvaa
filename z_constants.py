import os.path, cPickle, re

WWRTDIR = '/usr/local/wwrun'
BASEDIR = os.path.join(WWRTDIR, 'acva')
ACCTDIR = os.path.join(BASEDIR, 'accounts')
REGDIR = os.path.join(BASEDIR, 'reg')
EVENTDIR = os.path.join(BASEDIR, 'events')
REZDIR = os.path.join(BASEDIR, 'Residency', 'files')

EMAIL_REGISTER = os.path.join(REGDIR, 'email.dict')

DIPLSTR = 'T6yawy77cI11'
RESDSTR = 'c6z4d6G34AYx'
EMERSTR = 'W1P477cI4AZf'

STATES = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']
STATES_LOOKUP = {'AK': 'Alaska', 'AL': 'Alabama', 'AR': 'Arkansas', 'AZ': 'Arizona', 'CA': 'California', 'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware', 'FL': 'Florida', 'GA': 'Georgia', 'HI': 'Hawaii', 'IA': 'Iowa', 'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana', 'MA': 'Massachusetts', 'MD': 'Maryland', 'ME': 'Maine', 'MI': 'Michigan', 'MN': 'Minnesota', 'MO': 'Missouri', 'MS': 'Mississippi', 'MT': 'Montana', 'NC': 'North Carolina', 'ND': 'North Dakota', 'NE': 'Nebraska', 'NH': 'New Hampshire', 'NJ': 'New Jersey', 'NM': 'New Mexico', 'NV': 'Nevada', 'NY': 'New York', 'OH': 'Ohio', 'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania', 'RI': 'Rhode Island', 'SC': 'South Carolina', 'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah', 'VA': 'Virginia', 'VT': 'Vermont', 'WA': 'Washington', 'WI': 'Wisconsin', 'WV': 'West Virginia', 'WY': 'Wyoming', }
PROVS = ['AB', 'BC', 'MB', 'NB', 'NL', 'NS', 'NT', 'NU', 'ON', 'PE', 'QC', 'SK', 'YT',]
PROVS_LOOKUP = {'AB': 'Alberta', 'BC': 'British Columbia', 'MB': 'Manitoba', 'NB': 'New Brunswick', 'NL': 'Newfoundland and Labrador', 'NS': 'Nova Scotia', 'NT': 'Northwest Territories', 'NU': 'Nunavut', 'ON': 'Ontario', 'PE': 'Prince Edward Island', 'QC': 'Quebec', 'SK': 'Saskatchewan', 'YT': 'Yukon',}

HARV_DIPL = 'B9cL4zb9526l'
HARV_RESD = 'W1PBy65Q567i'

ALL_ROLES = ['admin', 'diplomate', 'resident', 'emeritus', 'honorary', 'memoriam', 'rtc']

DIPL_REGISTER = os.path.join(REGDIR, 'diplomates.list')
RESD_REGISTER = os.path.join(REGDIR, 'residents.list')
EMER_REGISTER = os.path.join(REGDIR, 'emeritus.list')
HONO_REGISTER = os.path.join(REGDIR, 'honorary.list')
MEMO_REGISTER = os.path.join(REGDIR, 'memoriam.list')
RTC_REGISTER = os.path.join(REGDIR, 'rtc.list')

EVENT_REGISTER = os.path.join(REGDIR, 'event_owners.dict')

JOB_CATS = ['Institution, Industry or Private Practice', 'Residency', 'Internship', 'Technician']
JOBDIR = os.path.join(BASEDIR, 'Jobs', 'job_files')
JOBCOUNT = os.path.join(JOBDIR, '.count')

######################################################
# MENU-RELATED CONSTANTS

MENUDIR = os.path.join(BASEDIR, 'menu_pieces')
menu_alltop = os.path.join(MENUDIR, 'all_top.html')
menu_admin = os.path.join(MENUDIR, 'admin_only.html')
menu_dips = os.path.join(MENUDIR, 'diplomates.html')
menu_cands = os.path.join(MENUDIR, 'candidates.html')
menu_allbottom = os.path.join(MENUDIR, 'all_bottom.html')
######################################################
# READ/WRITE FUNCTIONS

def rP(fullpath):
    try:
        file = open(fullpath, 'rb')
        p = cPickle.load(file)
        file.close()
    except IOError:
        p = {}
    return p

def wP(info, fullpath):
    file = open(fullpath, 'wb')
    cPickle.dump(info, file)
    file.close

def rText (fullpath):
    try:
        file = open(fullpath, 'r')
        txt = file.read()
        file.close()
    except IOError:
        txt = ''
    return txt

def wText (txt, fullpath):
    file = open(fullpath, 'w')
    file.write(txt)
    file.close()

######################################################
# SORT-RELATED FUNCTIONS

DIGITS = re.compile(r'[0-9]+')

def compnum(x, y):
    nx = ny = 0
    while True:
        a = DIGITS.search(x, nx)
        b = DIGITS.search(y, ny)
        if None in (a,b):
            return cmp(x[nx:], y[ny:])
        r = (cmp(x[nx:a.start()], y[ny:b.start()]) or
             cmp(int(x[a.start():a.end()]), int(y[b.start():b.end()])))
        if r:
            return r
        nx, ny = a.end(), b.end()


######################################################
MONTHS = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
FMONTHS = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}

######################################################

from z_countries import DEFAULT, CONTINENT_ORDER, COUNTRIES

def construct_pulldown():
    lines = []
    lines.append('<select id="countryselect" name="country" class="input">')
    for continent in CONTINENT_ORDER:
        lines.append('<optgroup label="%s">' % (continent))
        countries = COUNTRIES.get(continent)
        for country in countries:
            countrystring = '<option'
            if country == DEFAULT:
                countrystring += ' SELECTED'
            countrystring += '>%s</option>' % (country)
            lines.append(countrystring)
        lines.append('</optgroup>')
    lines.append('</select>')
    pulldown = '\r'.join(lines)
    return pulldown

COUNTRY_SELECT = construct_pulldown()
