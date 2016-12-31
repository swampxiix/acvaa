import os, string, glob
from z_constants import BASEDIR, rP, wP

DOCS_DIR = os.path.join(BASEDIR, 'docs')
DOC_CONST_DIR = os.path.join(DOCS_DIR, 'constitution')
DOC_DIP_DIR = os.path.join(DOCS_DIR, 'diplomates')
DOC_CAN_DIR = os.path.join(DOCS_DIR, 'candidates')
DOC_RPT_DIR = os.path.join(DOCS_DIR, 'annual_reports')

######################################################
# Constitution

DOC_CONST_INFO = os.path.join(DOC_CONST_DIR, '.info')

def save_constitution (form):
#     try:
#         M, D, Y = form.get('date')
#     except TypeError:
#         M, D, Y, = form.get('date').split('/')
    M, D, Y, = form.get('date').split('/')

    # Save data file
    fobj = form.get('datafile') # existence of file already checked
    contents, filename = fobj.value, fobj.filename
    filename = sanitize_file_name(filename)
    open(os.path.join(DOC_CONST_DIR, filename), 'wb').write(contents)
    form['datafile'] = filename
    wP(form, DOC_CONST_INFO)

def get_constitution_info ():
    return rP(DOC_CONST_INFO)

######################################################
# Documents, Forms, Reports, etc.

def register (regfile, filename, title):
    r = rP(regfile)
    r[filename] = title
    wP(r, regfile)

def unregister (regfile, filename):
    r = rP(regfile)
    if filename in r.keys():
        del r[filename]
    wP(r, regfile)

def get_doc_dir (doctype, category=None):
    dd = None
    if doctype == 'document':
        if category == 'diplomates':
            dd = DOC_DIP_DIR
        if category == 'candidates':
            dd = DOC_CAN_DIR
    if doctype == 'report':
        dd = DOC_RPT_DIR
    return dd

def save_document (form):
    fobj = form.get('datafile') # existence of file already checked
    contents, filename = fobj.value, fobj.filename
    filename = sanitize_file_name(filename)
    DEST = get_doc_dir(form.get('filetype'), form.get('category'))
    if DEST:
        REG = os.path.join(DEST, '.info')
        open(os.path.join(DEST, filename), 'wb').write(contents)
        register(REG, filename, form.get('title'))

def get_doc_dict (dtype, dcat=None):
    pd = get_doc_dir(dtype, dcat)
    if pd:
        return ( os.path.basename(pd), rP(os.path.join(pd, '.info')) )

def del_document (doctype, category, filename):
    dd = get_doc_dir(doctype, category)
    regfile = os.path.join(dd, '.info')
    unregister (regfile, filename)
    fullpath = os.path.join(dd, filename)
    os.unlink(fullpath)

def archive_document (doctype, category, filename):
    # This adds if not in list, removes if in list. Toggle status, basically.
    dd = get_doc_dir(doctype, category)
    archfile = os.path.join(dd, '.archivelist')
    archivelist = rP(archfile)
    if not archivelist:
        archivelist = []
    if filename not in archivelist:
        archivelist.append(filename)
    else:
        del archivelist[archivelist.index(filename)]
    wP(archivelist, archfile)

def get_archive_list (doctype, category):
    dd = get_doc_dir(doctype, category)
    archfile = os.path.join(dd, '.archivelist')
    return rP(archfile)

######################################################
# General

def sanitize_file_name (filename):
    allowed = string.digits + string.ascii_letters + '_.'
    filename = filename.strip()
    filename = filename.replace(' ', '_')
    filename = filename.replace('-', '_')
    filename = filename.replace(':', '_')
    # Expunge all non-allowed characters.
    for char in filename:
        if char not in allowed:
            filename = filename.replace(char, '')
    # Handle double dots.
    while '..' in filename:
        filename = filename.replace('..', '.')
    # Handle double unders.
    while '__' in filename:
        filename = filename.replace('__', '_')
    # No hidden allowed
    if filename.startswith('.'):
        filename = filename[1:]
    return filename
