import urllib, os.path
from z_constants import REGDIR, rP, wP

JOURNALIST = os.path.join(REGDIR, 'wileyjournal.list')

def wiley_auth():
    wiley_url = 'http://onlinelibrary.wiley.com/login-proxy-tps?targetURL=http://onlinelibrary.wiley.com/resolve/doi?DOI=10.1111/(ISSN)1467-2995&domain=acvaa.org'
    response = urllib.urlopen(wiley_url)
    redirect = response.read()
    return redirect

def get_journal_access ():
    return rP(JOURNALIST)

def set_journal_access (form):
    """
    form is {username: yes|no}
    """
    accesslist = get_journal_access()
    if not accesslist:
        accesslist = []
    for username in form.keys():
        if form.get(username) == 'yes':
            if username not in accesslist:
                accesslist.append(username)
        else:
            if username in accesslist:
                del accesslist[accesslist.index(username)]
    wP(accesslist, JOURNALIST)
