import os, calendar, glob, time
from z_constants import rP, EVENTDIR, EVENT_REGISTER, wP
from z_calgrid import getGrid
from z_times import get_int_from_YMD

######################################################
# Testers

def is_date_valid (event_id):
    t = time.gmtime(time.time()) 
#    c = calendar.timegm( (t[0], t[1], t[2], 0, 0, 0, 0, 1, -1) )
    c = get_int_from_YMD(t[0], t[1], t[2])
    return int(event_id) >= c

def ck_new_event (form):
    ERROR, ERROR_TYPE = None, None
    req = ['title', 'date', 'description']
    for r in req:
        if not form.get(r):
            ERROR = 'You must provide information for the form field "%s".' % (r)
            ERROR_TYPE = 'Event Form Error'
    m, d, y = form.get('date')
    event_id = create_event_id(y, m, d)
    if not is_date_valid(event_id):
        ERROR = 'The date for this event is in the past.'
        ERROR_TYPE = 'Date Error'
    return ERROR, ERROR_TYPE


def cleanse_url (url):
    if url.split('//')[0] not in ['http:', 'https:']:
        url = 'http://' + url
    if len(url.split('//')) > 2:
        url = 'http://' + url.split('//')[-1]
    return url


######################################################
# Creators

def create_event_id (y, m, d):
#    id_int = calendar.timegm((int(y), int(m), int(d), 0, 0, 0, 0, 1, -1))
    id_int = get_int_from_YMD(y, m, d)
    while os.path.exists(os.path.join(EVENTDIR, str(id_int))):
        id_int += 1
    return str(id_int)

def save_event (form):
    event_url = form.get('link_url')
    if event_url:
        event_url = cleanse_url(event_url)
        form['link_url'] = event_url
    m, d, y = form.get('date')
    event_id = create_event_id(y, m, d)
    filepath = os.path.join(EVENTDIR, event_id)
    wP(form, filepath)
    register_event(form.get('username'), event_id)
    return event_id

######################################################
# Accessors

def get_event_info (id):
    pick = rP(os.path.join(EVENTDIR, id))
    t = time.gmtime(int(id))
    pick['dayofweek'] = time.strftime('%a', t)
    pick['display_date'] = time.strftime('%A, %B %d, %Y', t)
    pick['month'] = time.strftime('%B', t)
    pick['day'] = str(t[2])
    pick['year'] = str(t[0])
    return pick

def get_all_events ():
    all = glob.glob(os.path.join(EVENTDIR, '*'))
    return all

def get_future_events ():
    t = time.gmtime(time.time()) 
#    c = calendar.timegm( (t[0], t[1], t[2], 0, 0, 0, 0, 1, -1) )
    c = get_int_from_YMD(t[0], t[1], t[2])
    all = get_all_events()
    f = []
    for e in all:
        bn = os.path.basename(e)
        if int(bn) >= c:
            f.append(e)
    f.sort()
    return f

def get_user_events (username):
    evs = []
    rg = rP(EVENT_REGISTER)
    if rg.has_key(username):
        if rg.get(username):
            evs = rg.get(username)
    return evs

def get_next_event (incl_restricted=False):
    future = get_future_events()
    if future:
        future.sort()
        if incl_restricted: # show all, no check necessary
            return get_event_info(os.path.basename(future[0]))
        else:
            ei = {}
            for e in future:
                ei = get_event_info(os.path.basename(e))
                if ei.get('visibility') == 'all':
                    return ei

def get_calendar ():
    grid = getGrid()
    return grid

######################################################
# Modifiers

def register_event (username, event_id):
    pick = rP(EVENT_REGISTER)
    if not pick.has_key(username):
        pick[username] = []
    pick[username].append(event_id)
    wP(pick, EVENT_REGISTER)

def deregister_event (username, event_id):
    pick = rP(EVENT_REGISTER)
    elist = pick.get(username, [])
    while event_id in elist:
        del elist[elist.index(event_id)]
    pick[username] = elist
    wP(pick, EVENT_REGISTER)

######################################################
# Destroyers

def delete_event (username, event_id):
    deregister_event (username, event_id)
    fp = os.path.join(EVENTDIR, event_id)
    os.unlink(fp)


