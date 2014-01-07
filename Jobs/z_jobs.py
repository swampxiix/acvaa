import time, glob, os
from acva.z_constants import JOBDIR, JOBCOUNT, compnum, rP, wP
from acva.z_events import cleanse_url
from acva.z_times import get_int_from_YMD, get_tuple_from_YMD

######################################################
# Testers

def is_date_valid (m, d, y):
    job_exp = get_int_from_YMD(y, m, d)
    t = time.gmtime(time.time()) 
    c = get_int_from_YMD(t[0], t[1], t[2])
    return job_exp > c

def ck_job_info (form):
    ERROR, ERROR_TYPE = None, None
    req = ['category', 'expires', 'job_title', 'job_inst', 'description']
    for r in req:
        if not form.get(r):
            ERROR = 'You must provide information for the form field "%s".' % (r)
            ERROR_TYPE = 'Incomplete Info'
    m, d, y = form.get('expires')
    if not is_date_valid(m, d, y):
        ERROR = 'The date for this event is in the past, or is today\'s date.'
        ERROR_TYPE = 'Date Error'
    return ERROR, ERROR_TYPE

def is_expired (m, d, y):
    exp_int = get_int_from_YMD(y, m, d)
    t = time.gmtime(time.time())
    c = get_int_from_YMD(t[0], t[1], t[2])
    return exp_int < c

######################################################
# Creators

def get_new_job_ID ():
    newid = rP(JOBCOUNT)
    nextid = newid +1
    wP(nextid, JOBCOUNT)
    return str(newid)

def save_job (form):
    if form.get('id'): # edit
        JOB_ID = form.get('id')
    else: # new
        JOB_ID = get_new_job_ID()
    form['id'] = JOB_ID
    form['posted'] = time.localtime(time.time())
    if form.get('web_link_url'):
        form['web_link_url'] = cleanse_url(form.get('web_link_url'))
    M, D, Y = form.get('expires')
    form['exp_tuple'] = get_tuple_from_YMD(Y, M, D)
    fullpath = os.path.join(JOBDIR, JOB_ID)
    wP(form, fullpath)

######################################################
# Accessors

def get_job_info (JOB_ID):
    fullpath = os.path.join(JOBDIR, JOB_ID)
    if os.path.exists(fullpath):
        return rP(fullpath)
    else:
        return {}

def get_all_jobs ():
    jfiles = glob.glob(os.path.join(JOBDIR, '*'))
    FINAL = {}
    for j in jfiles:
        jid = os.path.basename(j)
        FINAL[jid] = get_job_info(jid)
    return FINAL

def get_jobs_by_cat ():
    jobsdict = get_all_jobs()
    FINAL = {}
    for jid in jobsdict.keys():
        jdict = jobsdict.get(jid, {})
        thiscat = jdict.get('category')
        if not FINAL.has_key(thiscat):
            FINAL[thiscat] = {}
        FINAL[thiscat][jid] = jdict
    return FINAL

######################################################
# Destroyers

def delete_job (JOB_ID):
    fullpath = os.path.join(JOBDIR, JOB_ID)
    os.unlink(fullpath)
