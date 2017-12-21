"""
DOUBLE CHECK TO ENSURE NO FUNCTIONS IN THIS MODULE HAVE THE SAME NAME
AS THOSE IN z_docs.py
"""

import os
from z_constants import BASEDIR, rP, wP
from z_docs import sanitize_file_name

DOCS_DIR = os.path.join(BASEDIR, 'DocRepo') # was "Documents" but that caused namespace collision
TITLES_FILE = os.path.join(DOCS_DIR, '.titles.pick')
CATEGORIES_FILE = os.path.join(DOCS_DIR, '.categories.pick')
ACCESS_FILE = os.path.join(DOCS_DIR, '.access.pick')
ARCHIVED_FILE = os.path.join(DOCS_DIR, '.archived.pick')
MASTER_CATEGORY_LIST = os.path.join(DOCS_DIR, '.categories.master')

MASTER_ROLES_LIST = ['Diplomates', 'Residents', 'Veterinarians', 'Pet Owners']

######################################################
# Functions existing merely for convenience.

def rm_fr_list (alist, anitem):
    if anitem in alist:
        del alist[alist.index(anitem)]
    return alist

def listify_a_thing (thing):
    if type(thing) is list:
        return thing
    if type(thing) is str:
        return [thing]

######################################################
# Managing the master list of all potential doc categories.

def get_all_possible_categories ():
    return rP(MASTER_CATEGORY_LIST)

def edit_master_category (newcatname, oldcatname=None):
    p = get_all_possible_categories() or []
    if oldcatname:
        p = rm_fr_list(p, oldcatname)
    if newcatname not in p:
        p.append(newcatname)
    wP(p, MASTER_CATEGORY_LIST)

def remove_master_category (catname):
    # Make sure you can't remove category that's not empty yet!
    p = get_all_possible_categories()
    if is_category_empty(catname):
        p = rm_fr_list(p, catname)
        wP(p, MASTER_CATEGORY_LIST)

def reorder_master_category_list (catname, direction):
    existing_order = get_all_possible_categories()
    existing_index = existing_order.index(catname)
    popped = existing_order.pop(existing_index)
    if direction == 'up':
        new_index = existing_index - 1
    else:
        new_index = existing_index + 1
    existing_order.insert(new_index, popped)
    wP(existing_order, MASTER_CATEGORY_LIST)

######################################################
# Main write operations for document and its metadata.

#------------------------------------------------------
# File

def handle_cats (filename, fcat):
    fcat2 = listify_a_thing(fcat)
    for cat in fcat2:
        if cat:
            save_doc_to_category(filename, cat)

def handle_roles (filename, frol):
    frol2 = listify_a_thing(frol)
    for role in frol2:
        if role:
            save_doc_access(filename, role)

def save_doc_file (form):
    fobj = form.get('datafile') # existence of file already checked
    contents, filename = fobj.value, fobj.filename
    filename = sanitize_file_name(filename)
    open(os.path.join(DOCS_DIR, filename), 'wb').write(contents)
    save_doc_title(filename, form.get('title'))

    fcat = form.get('category')
    handle_cats(filename, fcat)

    frol = form.get('role')
    handle_roles(filename, frol)

def edit_doc_file (form):
    filename = form.get('filename')
    save_doc_title(filename, form.get('title'))

    fcat = form.get('category')
    handle_cats(filename, fcat)
    # Patrol for removals
    apcs = get_all_possible_categories() # list
    existing_cats = get_categories() # dict {key: [list]}
    for C in apcs:
        filelist = existing_cats.get(C, []) # list
        if filename in filelist:
            fcat2 = listify_a_thing(fcat)
            if C not in fcat:
                remove_doc_from_category(filename, C)

    frol = form.get('role')
    handle_roles(filename, frol)
    # Patrol for removals
    existing_rols = get_access()
    for R in MASTER_ROLES_LIST:
        filelist = existing_rols.get(R, [])
        if filename in filelist:
            frol2 = listify_a_thing(frol)
            if R not in frol:
                remove_doc_access (filename, R)

def rm_doc_file (filename):
    fullpath = os.path.join(DOCS_DIR, filename)
    # Nuke and pave registries.
    remove_doc_title(filename)
    edit_doc_categories(filename, [])
    edit_doc_access(filename, [])
    activate_doc(filename)
    # Delete.
    os.unlink(fullpath)

#------------------------------------------------------
# Document title

def save_doc_title (filename, title):
    # use also for editing
    p = rP(TITLES_FILE)
    p[filename] = title
    wP(p, TITLES_FILE)

def remove_doc_title (filename):
    p = rP(TITLES_FILE)
    if filename in p.keys():
        del p[filename]
        wP(p, TITLES_FILE)

#------------------------------------------------------
# Document category membership

def save_doc_to_category (filename, category):
    # One category at a time, please.
    # {categoryname: [list,of,filenames], other: [], }
    p = rP(CATEGORIES_FILE)
    file_list = p.get(category, [])
    if filename not in file_list:
        file_list.append(filename)
        p[category] = file_list
        wP(p, CATEGORIES_FILE)

def remove_doc_from_category (filename, category):
    p = rP(CATEGORIES_FILE)
    file_list = p.get(category, [])
    new_list = rm_fr_list(file_list, filename)
    p[category] = new_list
    wP(p, CATEGORIES_FILE)

def edit_doc_categories (filename, list_of_cats_to_be_in):
    all_possible_categories = get_all_possible_categories()
    for catname in all_possible_categories:
        if catname not in list_of_cats_to_be_in:
            # Attempt removal.
            remove_doc_from_category(filename, catname)
    categories = get_categories()
    for catname in list_of_cats_to_be_in:
        save_doc_to_category(filename, catname)

#------------------------------------------------------
# Document access control

def save_doc_access (filename, role):
    # One role at a time, please.
    # {role: [list,of,filenames], other: [], }
    p = rP(ACCESS_FILE)
    file_list = p.get(role, [])
    if filename not in file_list:
        file_list.append(filename)
        p[role] = file_list
        wP(p, ACCESS_FILE)

def remove_doc_access (filename, role):
    p = rP(ACCESS_FILE)
    file_list = p.get(role, [])
    new_list = rm_fr_list(file_list, filename)
    p[role] = new_list
    wP(p, ACCESS_FILE)

def edit_doc_access (filename, list_of_roles_to_allow):
    all_possible_roles = MASTER_ROLES_LIST
    for rolename in all_possible_roles:
        if rolename not in list_of_roles_to_allow:
            # Attempt removal.
            remove_doc_access(filename, rolename)
    access_dict = get_access()
    for rolename in list_of_roles_to_allow:
        save_doc_access(filename, rolename)

#------------------------------------------------------
# Archive switches

def archive_doc (filename):
    filename_list = get_archived()
    if filename not in filename_list:
        filename_list.append(filename)
    wP(filename_list, ARCHIVED_FILE)

def activate_doc (filename):
    filename_list = get_archived()
    new_list = rm_fr_list (filename_list, filename)
    wP(new_list, ARCHIVED_FILE)

######################################################
# Access

def get_archived ():
    return rP(ARCHIVED_FILE)

def get_categories ():
    return rP(CATEGORIES_FILE)

def get_access ():
    return rP(ACCESS_FILE)

def get_titles ():
    return rP(TITLES_FILE)

def get_document_properties (filename):
    filename_title_dict = get_titles()
    title = filename_title_dict.get(filename)   
    cat_filelist_dict = get_categories()
    my_cats = []
    for C in cat_filelist_dict.keys():
        filelist = cat_filelist_dict.get(C, [])
        if filename in filelist:
            my_cats.append(C)
    role_filelist_dict = get_access()
    my_rols = []
    for R in MASTER_ROLES_LIST:
        filelist = role_filelist_dict.get(R, [])
        if filename in filelist:
            my_rols.append(R)
    arch = get_archived()
    final = {'title': title, 'categories': my_cats, 'roles': my_rols, 'is_archived': filename in arch}
    return final

######################################################
# Boolean checks

def is_category_empty (catname):
    doc_cat_pick = get_categories()
    doclist = doc_cat_pick.get(catname, [])
    if len(doclist) > 0:
        return False
    else:
        return True






