import os.path, random
from acva.z_constants import BASEDIR, rP, wP

TRAINDIR = os.path.join(BASEDIR, "Training")
RTC_MAP_FILE = os.path.join(TRAINDIR, 'category.name.map')
RTC_CAT_FILE = os.path.join(TRAINDIR, 'categories.dict')

def get_rtc_categories ():
    return rP(RTC_CAT_FILE)

def get_rtc_name_map ():
    return rP(RTC_MAP_FILE)

def add_category (catname):
    GUID = str(random.random())
    catdict = get_rtc_categories()
    mapdict = get_rtc_name_map()
    catnames = mapdict.values()
    if catname not in catnames:
        mapdict[GUID] = catname
        catdict[GUID] = []
        wP(mapdict, RTC_MAP_FILE)
        wP(catdict, RTC_CAT_FILE)
    else:
        return True # indicates error

def delete_category (catname):
    """
    Category_Delete.py already checks to make sure there are
    no resources tied to this category.
    """
    catdict = get_rtc_categories()
    mapdict = get_rtc_name_map()
    CATGUID = False
    for guid in mapdict.keys():
        catstring = mapdict[guid]
        if catstring == catname:
            CATGUID = guid
    if CATGUID:
        del mapdict[CATGUID]
        del catdict[CATGUID]
        wP(mapdict, RTC_MAP_FILE)
        wP(catdict, RTC_CAT_FILE)
    else:
        return True # indicates error


