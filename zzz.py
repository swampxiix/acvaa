import glob, os.path
from z_constants import rP, wP
from z_geo import USA_STATES_LOOKUP, CAN_STATES_LOOKUP, MEX_STATES_LOOKUP

ADIR = '/usr/local/wwrun/acva/accounts'

def fstates ():
    allaccts = glob.glob(os.path.join(ADIR, '*'))
    for fpath in allaccts:
        p = rP(fpath)
        ct = p.get('country')
        st = p.get('state')
        if ct == 'USA':
            if st not in USA_STATES_LOOKUP.keys():
                print '%s (USA) state is %s' % (os.path.basename(fpath), st)
        if ct == 'Canada':
            if st not in CAN_STATES_LOOKUP.keys():
                print '%s (CAN) state is %s' % (os.path.basename(fpath), st)
        if ct == 'Mexico':
            if st not in MEX_STATES_LOOKUP.keys():
                print '%s (MEX) state is %s' % (os.path.basename(fpath), st)

def chst (acct, ns):
    pathtofile = os.path.join(ADIR, acct)
    p = rP(pathtofile)
    p['state'] = ns
    wP(p, pathtofile)

