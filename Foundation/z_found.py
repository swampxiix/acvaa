import os.path
from acva.z_constants import BASEDIR, rP, wP
FDIR = os.path.join(BASEDIR, "Foundation")
REGULAR = os.path.join(FDIR, 'donors.regular')
CHARTER = os.path.join(FDIR, 'donors.charter')
FOUNDER = os.path.join(FDIR, 'donors.founder')
D = {'r': REGULAR, 'c': CHARTER, 'f': FOUNDER}
TRAVELFLAG = os.path.join(FDIR, 'travel.flag')

def get_donors (dtype='r'):
    L = rP(D.get(dtype))
    if not L: L = []
    L = sorted(L, key=lambda x: (x.isdigit() and float(x)) or x.lower())
    return L

def add_donor (dtype, dname):
    fn = D.get(dtype)
    L = rP(fn)
    if not L: L = []
    if dname not in L:
        L.append(dname)
    wP(L, fn)

def del_donor (dtype, dname):
    fn = D.get(dtype)
    L = rP(fn)
    if dname in L:
        del L[L.index(dname)]
    wP(L, fn)

def show_travel():
    p = rP(TRAVELFLAG)
    return p

def toggle_travel():
    flag = rP(TRAVELFLAG)
    if flag == True:
        wP(False, TRAVELFLAG)
    else:
        wP(True, TRAVELFLAG)


