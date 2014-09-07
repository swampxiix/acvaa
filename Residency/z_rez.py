import os, glob, uuid
from acva.z_constants import REZDIR, rP, wP

def get_residencies ():
    progdict = {}
    allfiles = glob.glob(os.path.join(REZDIR, '*'))
    for file in allfiles:
        fdict = rP(file)
        progdict[fdict.get('institution')] = fdict
    return progdict

def get_one_residency (id):
    return rP(os.path.join(REZDIR, id))

def save_residency (form):
    if not form.get('id'):
        id = str(uuid.uuid4())
        form['id'] = id
    filepath = os.path.join(REZDIR, form.get('id'))
    wP(form, filepath)

def delete_residency (id):
    filepath = os.path.join(REZDIR, id)
    os.unlink(filepath)
