import sha, os, random, glob

from z_constants import ACCTDIR, rP, wP, DIPLSTR, RESDSTR, HARV_DIPL, \
    HARV_RESD, EMAIL_REGISTER, compnum, DIPL_REGISTER, RESD_REGISTER

from z_email import send_reset_password, send_registration_confirm

######################################################
# Crypto

def hash_string(S):
    return sha.new(S).hexdigest()

def generate_random():
    id = []
    while len(id) < 12:
        id.append(str(random.randint(0,9)))
    return ''.join(id)

######################################################
# Test Conditions

def check_login_input (form):
    ERROR = None
    username, passwd = form.get('username'), form.get('password')
    if not username:
        ERROR = 'You must enter your user name in the login form.'
    elif not passwd:
        ERROR = 'You must enter your password in the login form.'
    return ERROR

def authenticate (form):
    ERROR = check_login_input(form)
    if not ERROR:
        username, passwd = form.get('username'), form.get('password')
        if username:
            username = username.lower()
            userpick = get_user_acct(username, True)
            if hash_string(passwd) != userpick.get('password'):
                ERROR = 'Wrong credentials: User name or password doesn\'t match.'
    return ERROR

def is_logged_in (req):
    # pass in self.request()
    ili = False
    c = req.cookies()
    username, hash = c.get('username'), c.get('hash')
    if username:
        username = username.lower()
        userpick = get_user_acct(username)
        if hash == hash_string(userpick.get('vcode', '')):
            ili = True
    return ili

def check_email_characters (E):
    # This relies on check_email_address() below.
    ERROR = False
    for char in E:
        decimalValue = ord(char)
        if decimalValue < 33 or decimalValue > 126:
            ERROR = True
    return ERROR

def check_email_format (E):
    # This relies on check_email_address() below.
    ERROR = False
    # Checks only the a@b.c format, not valid chars or destination
    if (not '@' in E) or (not '.' in E):
        ERROR = True
    ES1 = E.split('@')
    ES2 = ES1[-1].split('.')
    if len(ES2) < 2 or not ES2[0]:
        ERROR = True
    for x in ES1:
        if not x:
            ERROR = True
    for x in E.split('.'):
        if not x:
            ERROR = True
    return ERROR

def check_email_address (E):
    ERROR = False
    ERROR = check_email_characters(E)
    if not ERROR:
        ERROR = check_email_format(E)
    if ERROR:
        return 'The email address you provided is not valid.'

def is_email_registered (email):
    if email:
        email = email.lower()
        d = rP(EMAIL_REGISTER)
        return email in d.keys()

def is_site_admin (req):
    # pass in self.request()
    ISA = False
    if is_logged_in(req):
        c = req.cookies()
        username, hash = c.get('username'), c.get('hash')
        if username:
            username = username.lower()
            userpick = get_user_acct(username)
            if 'admin' in userpick.get('roles'):
                ISA = True
    return ISA

######################################################
# Accessors

def get_user_acct (username, with_pass=False):
    if username:
        username = username.lower()
        a = os.path.join(ACCTDIR, username)
        if os.path.exists(a):
            b = rP(a)
            if not with_pass:
                del b['password']
            return b
        else:
            return {}
    else:
        return {}

def get_user_role (username):
    if username:
        username = username.lower()
        ui = get_user_acct(username)
        roles = ui.get('roles', [])
        if 'diplomate' in roles:
            return DIPLSTR
        elif 'resident' in roles:
            return RESDSTR

def get_new_user_id (fn, sn):
    fn, sn = fn.strip().lower(), sn.strip().lower()
    s = fn[0] + sn
    x = glob.glob(os.path.join(ACCTDIR, '%s*' % (s)))
    if x:
        return s + str(len(x)+1)
    else:
        return s

def get_all_users ():
    allpaths = glob.glob(os.path.join(ACCTDIR, '*'))
    FINAL = {}
    for fpath in allpaths:
        username = os.path.basename(fpath).lower()
        upick = get_user_acct(username)
        upick['username'] = username
        uuid = '%s_%s_%s' % (upick.get('sn'), upick.get('fn'), username)
        FINAL[uuid] = upick
    return FINAL

def get_users (utype):
    if utype in ['diplomate', 'diplomates', 'd']:
        REG = DIPL_REGISTER
    elif utype in ['resident', 'residents', 'r']:
        REG = RESD_REGISTER
    else:
        return {}

    L = rP(REG)
    FINAL = {}
    for username in L:
        upick = get_user_acct(username)
        upick['username'] = username
        uuid = '%s_%s_%s' % (upick.get('sn'), upick.get('fn'), username)
        FINAL[uuid] = upick
    return FINAL

######################################################
# Modifiers

def reset_password (username):
    if username:
        username = username.lower()
        ui = get_user_acct(username, with_pass=True)
        newpass = generate_random()
        ui['password'] = hash_string(newpass)
        wP(ui, os.path.join(ACCTDIR, username))
        send_reset_password(ui.get('email'), newpass)

def change_password (username, newpass):
    if username:
        username = username.lower()
        ui = get_user_acct(username, with_pass=True)
        ui['password'] = hash_string(newpass)
        wP(ui, os.path.join(ACCTDIR, username))

from z_events import cleanse_url

def change_for_hire_status (username, form):
    if username:
        username = username.lower()
        ui = get_user_acct(username, with_pass=True)
        for param in ['show_for_hire', 'for_hire_areas', 'for_hire_services']:
            ui[param] = form.get(param)
        if form.get('for_hire_url'):
            ui['for_hire_url'] = cleanse_url(form.get('for_hire_url'))
        else:
            ui['for_hire_url'] = ''
        wP(ui, os.path.join(ACCTDIR, username))

def save_registration (form):
    # required fields & matching passwords already checked
    form['roles'] = []
    if form.get('hc') == HARV_DIPL:
        form['roles'].append('diplomate')
        MAINROLE = 'diplomate'
    elif form.get('hc') == HARV_RESD:
        form['roles'].append('resident')
        MAINROLE = 'resident'
    form['password'] = hash_string(form.get('pw1'))
    for a in ['x', 'y', 'hc', 'pw1', 'pw2']:
        if form.has_key(a):
            del form[a]
    form['vcode'] = generate_random()
    new_userid = get_new_user_id(form.get('fn'), form.get('sn'))
    destination = os.path.join(ACCTDIR, new_userid)
    wP(form, destination)
    # cache role
    cache_role (new_userid, MAINROLE, 'reg')
    # duplicate email addresses should have already been checked
    register_email_addr(form.get('email'), new_userid)
    send_registration_confirm(form.get('email'), new_userid)
    return new_userid

def save_user_info (username, form):
    if username:
        username = username.lower()
        ui = get_user_acct(username, with_pass=True)
        # Is user changing email address?
        if form.get('email') != form.get('original_email'):
            unregister_email_addr(username)
            register_email_addr (form.get('email'), username)
        # Remove unwanted form fields.
        cruft = ['form_hash', 'form_username', 'original_email']
        for c in cruft:
            if form.has_key(c):
                del form[c]
        # Update & Save
        for k in form.keys():
            ui[k] = form[k]
        wP(ui, os.path.join(ACCTDIR, username))

#==========================================
# Registry Stuff

def register_email_addr (email, userid):
    # duplicate email addresses should have already been checked
    if email:
        email = email.lower()
        d = rP(EMAIL_REGISTER)
        if not d.has_key(email):
            d[email] = userid
        wP(d, EMAIL_REGISTER)

def unregister_email_addr (userid):
    d = rP(EMAIL_REGISTER)
    for k in d.keys():
        if d[k] == userid:
            del d[k]
    wP(d, EMAIL_REGISTER)

def cache_role (username, role, action):
    if username:
        username = username.lower()
        if role == 'resident':
            REG = RESD_REGISTER
        if role == 'diplomate':
            REG = DIPL_REGISTER
        L = rP(REG)
        if not L: L = []
        if action == 'reg':
            if username not in L:
                L.append(username)
                wP(L, REG)
        if action == 'dereg':
            if username in L:
                del L[L.index(username)]
                wP(L, REG)

#==========================================
# Admin Instantiated Modifications

def delete_user_account (userid):
    userfile = os.path.join(ACCTDIR, userid)
    if os.path.exists(userfile):
        unregister_email_addr(userid)
        os.unlink(userfile)
    # cache role
    for x in ['diplomate', 'resident']:
        cache_role (userid, x, 'dereg')

from types import *

def save_user_roles(username, roles):
    if username:
        username = username.lower()
        ui = get_user_acct(username, with_pass=True)
        if type(roles) is ListType:
            ui['roles'] = roles
        elif type(roles) is StringType:
            ui['roles'] = [roles]
        wP(ui, os.path.join(ACCTDIR, username))
        # cache role
        for x in ['diplomate', 'resident']:
            if x in ui['roles']:
                cache_role (username, x, 'reg')
            else:
                cache_role (username, x, 'dereg')

def acting_as (req):
    c = req.cookies()
    return c.get('actingasuser', None)

