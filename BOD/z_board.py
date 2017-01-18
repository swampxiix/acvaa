from acva.z_constants import BASEDIR, rP, wP
from acva.z_times import get_int_from_YMD
from acva.z_geo import USA_STATES_ORDER, USA_STATES, CAN_STATES_ORDER, CAN_STATES
import os, glob

BODDIR = os.path.join(BASEDIR, 'BOD')
MINS_DIR = os.path.join(BODDIR, 'minutes')
MINDOC_DIR = os.path.join(BODDIR, 'minutes_docs')

######################################################
# Board of Directors

BODFILE = os.path.join(BODDIR, 'bod.pick')

def getBOD():
    return rP(BODFILE)

def updateBOD(form):
    FINAL = {}
    for k in form.keys():
        FINAL[k] = {}
        FINAL[k]['name'], FINAL[k]['email'], FINAL[k]['year'] = form.get(k)
    wP(FINAL, BODFILE)

######################################################
# Minutes

def check_minutes_datafile (form):
    ERROR = None
    M, D, Y = form.get('date')
    # Check for existing pickle
    file_id = str(get_int_from_YMD(Y, M, D))
    if os.path.exists(os.path.join(MINS_DIR, file_id)):
        ERROR = 'Minutes already exist for that date.'
    # Check for existing data file
    fobj = form.get('datafile') # existence of file already checked
    fext = os.path.splitext(fobj.filename)[-1]
    doc_fn = 'acva_minutes_%s_%s_%s%s' % (Y, M, D, fext)
    if os.path.exists(os.path.join(MINDOC_DIR, doc_fn)):
        ERROR = 'Minutes document already exists for that date.'
    return ERROR

def save_minutes (form):
    M, D, Y = form.get('date')
    # Save data file
    fobj = form.get('datafile') # existence of file already checked
    contents = fobj.value
    fext = os.path.splitext(fobj.filename)[-1]
    doc_fn = 'acva_minutes_%s_%s_%s%s' % (Y, M, D, fext)
    open(os.path.join(MINDOC_DIR, doc_fn), 'wb').write(contents)
    # Save pickle
    form['datafile'] = doc_fn
    file_id = str(get_int_from_YMD(Y, M, D))
    wP(form, os.path.join(MINS_DIR, file_id))

def get_all_minutes ():
    FINAL = {}
    all_ids = glob.glob(os.path.join(MINS_DIR, '*'))
    for fpath in all_ids:
        file_id = os.path.basename(fpath)
        file_dict = rP(fpath)
        FINAL[file_id] = file_dict
    return FINAL

def get_minutes (id):
    return rP(os.path.join(MINS_DIR, id))

def kill_minutes (id):
    meet_dict = get_minutes(id)
    datafilepath = os.path.join(MINDOC_DIR, meet_dict.get('datafile'))
    os.unlink(datafilepath)
    picklepath = os.path.join(MINS_DIR, id)
    os.unlink(picklepath)

######################################################
# Regions

regions = {
    1: ['CT', 'ME', 'MA', 'NB', 'NH', 'NJ', 'NY', 'NL', 'NS', 'ON', 'PA', 'PE', 'QC', 'RI', 'VT', ],
    2: ['AL', 'DE', 'FL', 'GA', 'KY', 'MD', 'NC', 'SC', 'TN', 'VA', 'WV', ],
    3: ['KS', 'MB', 'NE', 'ND', 'OK', 'SD', 'TX', 'CO', 'NM', 'SK', ],
    4: ['IL', 'IN', 'MI', 'MN', 'OH', 'WI', 'AR', 'IA', 'LA', 'MS', 'MO', ],
    5: ['AK', 'AB', 'AZ', 'BC', 'CA', 'HI', 'ID', 'MT', 'NU', 'NV', 'NT', 'OR', 'UT', 'WA', 'WY', 'YT', "All countries other than US and Canada"],
    }

# (name, userid)
# regional_reps = {
#     1: ('Sophie Cuvelliez', 'scuvelliez'),
#     2: ('Andre Shih', ''),
#     3: ('Nora Matthews', 'nmatthews'),
#     4: ('Lesley Smith', 'lsmith'),
#     5: ('Matt Read', 'mread'),
#     }

reg_hex = {
    1: 'ff8080',
    2: 'fff980',
    3: 'a4ff80',
    4: 'ffc480',
    5: '80c0ff',
    }

def get_region_by_state (state):
    for r in regions.keys():
        if state in regions[r]:
            return r

def get_region_dict (country='US'):
    SLIST = []
    if country == 'CA':
        for s in CAN_STATES_ORDER:
            SLIST.append(CAN_STATES.get(s))
    else:
        for s in USA_STATES_ORDER:
            SLIST.append(USA_STATES.get(s))
    FINAL = {}
    for s in SLIST:
        FINAL[s] = get_region_by_state(s)
    return FINAL
