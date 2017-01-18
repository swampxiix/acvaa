import os.path
from z_account import get_users

FLAGDIR = '/var/www/html/g/flags'

def get_flag (country, align=None):
    country = country.replace(' ', '_')
    country = country.replace('.', '')
    # Returns markup.
    mkup = ''
    if not country:
        return mkup
    if os.path.exists(os.path.join(FLAGDIR, '%s.png' % (country.lower()))):
        mkup = '''<img src="/g/flags/%s.png" vspace="2" alt="%s" ''' % (country.lower(), country)
        if align:
            mkup += '''align="%s" ''' % (align)
        mkup += '/>'
    return mkup

def get_locations ():
    # {Country: {State: {City: [(d1id, d1name), (d2id ,d2name)], }, }, }
    MASTER = {}
    dips = get_users('d')
    ks = dips.keys()
    ks.sort()
    for k in ks:
        ddict = dips[k]
        if ddict.get('sec_policy') == 'paranoid':
            pass
        else:
            country = ddict.get('country')
            if country:
                if not MASTER.has_key(country):
                    MASTER[country] = {}
                CDICT = MASTER[country]
    
            state = ddict.get('state')
            if state:
                if not CDICT.has_key(state):
                    CDICT[state] = {}
                SDICT = CDICT[state]
    
            city = ddict.get('city')
            if city:
                if not SDICT.has_key(city):
                    SDICT[city] = []
    
            did = ddict.get('username')
            dname = '%s %s %s' % (ddict.get('fn', ''), ddict.get('mi', ''), ddict.get('sn', ''))
            if ddict.get('title'):
                dname += ', %s' % (ddict['title'])
    
            tupe = (did, dname)
            if city:
                SDICT[city].append(tupe)
    return MASTER
