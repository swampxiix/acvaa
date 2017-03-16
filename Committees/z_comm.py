import os, glob, re, string
from acva.z_constants import BASEDIR, rP, wP

COMDIR = os.path.join(BASEDIR, 'Committees')
DATADIR = os.path.join(COMDIR, 'data')

######################################################
# General Purpose Methods

def get_all_dirs_in (fullpath):
    dirs = []
    all = glob.glob(os.path.join(fullpath, '*'))
    for path in all:
        if os.path.isdir(path):
            dirs.append(path)
    return dirs

def get_next_id (list_of_things):
    if list_of_things:
        list_of_things = sorted(list_of_things, key=lambda s: [int(t) if t.isdigit() else t.lower() for t in re.split('(\d+)', s)])
        highestnumber = int(os.path.basename(list_of_things[-1])) # last in list
        return string.zfill(highestnumber+1, 4)
    else:
        return '0001'

######################################################
# Committees

def get_all_committee_dirs ():
    return get_all_dirs_in(fullpath=DATADIR)

def get_next_committee_id ():
    alldirs = get_all_committee_dirs()
    return get_next_id(alldirs)

COMM_MAP = os.path.join(DATADIR, 'committee.map')
def get_committees ():
     # {'0001': {'name': str}, '0002': ... }
    return rP(COMM_MAP)

COMM_ORD = os.path.join(DATADIR, 'committee.order')
def get_committee_order ():
    # ['0001', '0002', ...]
    a = rP(COMM_ORD)
    if a:
        return a
    else:
        return []

def add_committee (comm_name):
    # Create committee directory
    this_id = get_next_committee_id()
    newpath = os.path.join(DATADIR, this_id)
    os.mkdir(newpath)
    comm_map = get_committees()
    comm_map[this_id] = {'name': comm_name}
    writePick(comm_map, COMM_MAP)
    comm_ord = get_committee_order() # []
    if this_id not in comm_ord:
        comm_ord.append(this_id)
        writePick(comm_ord, COMM_ORD)
    return this_id

def get_committee_info (comm_id):
    comms = get_committees()
    return comms.get(comm_id, {})

def rename_committee (comm_id, new_name):
    comms = get_committees()
    comms[comm_id]['name'] = new_name
    writePick(comms, COMM_MAP)

def delete_committee (comm_id):
    """
    This does not touch the directory in which the committee members
    were saved. It merely removes it from the indices.
    """
    comms = get_committees()
    if comm_id in comms.keys():
        del comms[comm_id]
        writePick(comms, COMM_MAP)
    order = get_committee_order()
    if comm_id in order:
        del order[order.index(comm_id)]
        writePick(order, COMM_ORD)

def reorder_committees (new_order): # Blue Monday
    writePick(new_order, COMM_ORD)

######################################################
# Members

def get_all_member_files (comm_id):
    comm_directory = os.path.join(DATADIR, comm_id)
    mb_paths = []
    allpaths = glob.glob(os.path.join(comm_directory, '*'))
    for fpath in allpaths:
        try:
            x = int(os.path.basename(fpath))
            mb_paths.append(fpath)
        except ValueError:
            pass
    return mb_paths

def get_next_member_id (comm_id):
    allpaths = get_all_software_files(comm_id)
    return get_next_id(allpaths)

def get_members (comm_id):
    MB_MAP = os.path.join(DATADIR, comm_id, 'members.map')
    return rP(MB_MAP)

def get_members_order (comm_id):
    MB_ORD = os.path.join(DATADIR, comm_id, 'members.order')
    a = rP(MB_ORD)
    if a:
        return a
    else:
        return []

def add_member (comm_id, mb_title, mb_name, mb_email, mb_year):
    this_id = get_next_member_id(comm_id)
    members_map = get_members(comm_id)
    members_map[this_id] = {'title': mb_title, 'name': mb_name, 'email': mb_email, 'year': mb_year}
    writePick( members_map, os.path.join(DATADIR, comm_id, 'members.map') )
    members_ord = get_members_order(comm_id) # []
    if this_id not in members_ord:
        members_ord.append(this_id)
        writePick( members_ord, os.path.join(DATADIR, comm_id, 'members.order') )
    return this_id

def delete_member (comm_id, mb_id):
    mb_map = get_members(comm_id)
    if mb_id in mb_map.keys():
        del mb_map[mb_id]
        writePick(mb_map, os.path.join(DATADIR, comm_id, 'members.map'))
    order = get_members_order(comm_id)
    if mb_id in order:
        del order[order.index(mb_id)]
        writePick(order, os.path.join(DATADIR, comm_id, 'members.order'))

def reorder_members (comm_id, new_order): # Bizarre Love Triangle
    MB_ORD = os.path.join(DATADIR, comm_id, 'members.order')
    writePick(new_order, MB_ORD)















