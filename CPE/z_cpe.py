import os.path
from acva.z_constants import BASEDIR

CPEDIR = os.path.join(BASEDIR, 'CPE')
CPEDOCS = os.path.join(CPEDIR, 'docs')
INFILE = 'introduction.txt'
GLFILE = 'guidelines.txt'
SMFILE = 'summary.txt'
APFILE = 'application.txt'
PGFILE = 'programs.txt'

LOOKUP = {  INFILE: 'Index',
            GLFILE: 'Guidelines', 
            SMFILE: 'Summary',
            APFILE: 'Application',
            PGFILE: 'Programs',
            }

def get_raw_from (filename):
    docpath = os.path.join(CPEDOCS, filename)
    if os.path.exists(docpath):
        file = open(docpath, 'r')
        txt = file.read()
        file.close()
        return txt
    else:
        return ''

def get_html_from (filename):
    txt = get_raw_from(filename)
    txt = txt.replace('\r\n', '\n')
    txt = txt.replace('\n', '<br>')
    return txt

def write_raw_to (filename, rawtext):
    docpath = os.path.join(CPEDOCS, filename)
    if os.path.exists(docpath): # no new docs on the fly
        file = open(docpath, 'w')
        file.write(rawtext)
        file.close()

