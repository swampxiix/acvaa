import os.path, random
from acva.z_constants import BASEDIR, rP, wP
from acva.z_docs import sanitize_file_name
from acva.z_events import cleanse_url

TRAINDIR = os.path.join(BASEDIR, "Training")
REZDIR = os.path.join(TRAINDIR, "resources")
FILEDIR = os.path.join(TRAINDIR, "files")
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

def edit_category (oldname, newname):
    mapdict = get_rtc_name_map()
    CATGUID = False
    for guid in mapdict.keys():
        catstring = mapdict[guid]
        if catstring == oldname:
            CATGUID = guid
    if CATGUID:
        mapdict[CATGUID] = newname
        wP(mapdict, RTC_MAP_FILE)
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

def get_guid_by_name (name):
    mapdict = get_rtc_name_map()
    for guid in mapdict.keys():
        if mapdict[guid] == name:
            return guid

def add_resource (form):
    guid = get_guid_by_name(form.get('category'))
    form['category'] = guid
    if form.get('url'):
        form['url'] = cleanse_url(form.get('url'))
    if form.get('filename') and form.get('contents'):
        filename = sanitize_file_name(form.get('filename'))
        open(os.path.join(FILEDIR, filename), 'wb').write(form.get('contents'))
    try:
        del form['contents']
    except:
        pass
    FILEID = str(random.random())
    wP(form, os.path.join(REZDIR, FILEID))

    catdict = get_rtc_categories()
    catdict[form.get('category')].append(FILEID)
    wP(catdict, RTC_CAT_FILE)

