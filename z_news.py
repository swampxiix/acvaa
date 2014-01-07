from z_constants import BASEDIR, rP, wP
import os, time, glob

NEWSDIR = os.path.join(BASEDIR, 'news_files')
AMTGDIR = os.path.join(BASEDIR, 'Annual', 'news')
ACTIDIR = os.path.join(BASEDIR, 'action_docs')

def get_id ():
    return str(int(time.time()))

def save_news (form):
    dirtosaveto = NEWSDIR
    if form.get('annualnews') == 'true':
        dirtosaveto = AMTGDIR
        del form['annualnews']
    if form.get('actionitem') == 'true':
        dirtosaveto = ACTIDIR
        del form['actionitem']
    if not form.get('id'):
        form['id'] = get_id()
    form['added'] = time.strftime('%d %b %Y', time.localtime(int(form['id'])))
    filepath = os.path.join(dirtosaveto, form['id'])
    wP(form, filepath)

def get_news_item (id):
    for ddir in (NEWSDIR, AMTGDIR, ACTIDIR):
        p = os.path.join(ddir, id)
        if os.path.exists(p):
            return rP(p)

def now_year ():
    return str(time.localtime(time.time())[0])

def get_news_by_year (year=None):
    if not year:
        year = now_year()
    MATCH = []
    all = glob.glob(os.path.join(NEWSDIR, '*'))
    all.sort()
    all.reverse()
    for nipath in all:
        niname = os.path.basename(nipath)
        niyear = str(time.localtime(int(niname))[0])
        if niyear == year:
            MATCH.append(rP(os.path.join(nipath)))
    return MATCH

def get_archive_years ():
    yrs = []
    all = glob.glob(os.path.join(NEWSDIR, '*'))
    for nipath in all:
        niname = os.path.basename(nipath)
        niyear = str(time.localtime(int(niname))[0])
        if niyear != now_year() and niyear not in yrs:
            yrs.append(niyear)
    yrs.sort()
    yrs.reverse()
    return yrs

def get_annual_news():
    AN = []
    all = glob.glob(os.path.join(AMTGDIR, '*'))
    all.sort()
    all.reverse()
    for x in all:
        AN.append(rP(os.path.join(x)))
    return AN

def get_action_items():
    AN = []
    all = glob.glob(os.path.join(ACTIDIR, '*'))
    all.sort()
    all.reverse()
    for x in all:
        AN.append(rP(os.path.join(x)))
    return AN

def delete_news_item (id, ntype='news'):
    dirtodelfrom = NEWSDIR
    if ntype == 'annual':
        dirtodelfrom = AMTGDIR
    if ntype == 'actionitem':
        dirtodelfrom = ACTIDIR
    filepath = os.path.join(dirtodelfrom, id)
    os.unlink(filepath)

