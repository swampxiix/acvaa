from WebKit.Page import Page
from WebKit.Cookie import Cookie

from z_account import is_logged_in, is_site_admin, acting_as
from z_constants import DIPLSTR, RESDSTR, MONTHS, rText, wText, \
    menu_alltop, menu_admin, menu_dips, menu_cands, menu_allbottom
from z_forms import text, passwd, hidden, submit
from z_times import get_year

import time

class Template_Main (Page):
    def writeDocType(self):
        self.writeln('<!DOCTYPE html>')

    def writeHeadParts(self):
        """Switched the order of these b/c bootstrap said to do that.
        """
        self.writeMetaData() # was second
        self.writeTitle() # was first
        self.writeStyleSheet()
        self.writeJavaScript()

    def writeMetaData(self):
        """Bootstrap-required meta tags.
        """
        self.writeln('''
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
            ''')

    def writeStyleSheet(self):
        self.writeln('''
<link rel="shortcut icon" href="/g/favicon.ico" type="image/x-icon" />
<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">
<link rel="stylesheet" href="/c/bootstrap.min.css" type="text/css">
<link rel="stylesheet" href="/c/acva.css" type="text/css">
<link rel="stylesheet" href="/c/acvaa_bootstrap.css" type="text/css">
            ''')


    def writeJavaScript(self):
        self.writeln('''
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
<script type="text/javascript" src="/js/jquery-2.1.3.min.js"></script>
<script type="text/javascript" src="/js/jquery.cookie.js"></script>
<script type="text/javascript" src="/js/bootstrap.min.js"></script>
<script type="text/javascript" src="/js/acva.js"></script>
<!--[if lt IE 9]>
<script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
<script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
<![endif]-->
            ''')

    def writeBody(self):
        wr = self.writeln
        wr('<body>')
        self.writeBodyParts()
        # This is where google analytics stuff goes!
        wr('</body>')

    def writeBodyParts(self):
        wr = self.writeln
        self.writeHeader()
        self.writeSubHeader()
        wr('''
<div class="container" id="body-container">
  <div class="row">
    <!-- LEFT MENU COLUMN ###################################################### -->
    <div class="col-md-3" id="mobile-side-menu">
      <div id="show-mobile-menu" class="btn btn-orange btn-sm">
        Show Menu
      </div>
    </div>
    <div class="col-md-3" id="side-menu">
            ''')
        self.writeNav()
        wr('''
    </div><!-- .col-md-3 #side-menu -->
    <!-- RIGHT CONTENT COLUMN ###################################################### -->
    <div class="col-md-9" id="main-content">
            ''')
        self.writeContent()
        wr('''
    </div><!-- .col-md-9 -->
  </div><!-- .row -->
</div><!-- #body-container -->
            ''')
        self.writeFooter()


    def writeHeader(self):
        IS_LOGGED_IN = is_logged_in(self.request())
        global IS_LOGGED_IN
        wr = self.writeln
        wr('''
<div class="container" id="header">
  <a href="http://www.acvaa.org/"><img width="709" height="184" alt="ACVAA logo and wordmark" src="/g/header_2015.png" class="img-responsive" border="0"></a>
</div><!-- #header -->
            ''')

    def writeSubHeader(self):
        if not self.request().fields().has_key('from_url'):
            from_url = self.get_from_url()
        else:
            from_url = self.request().fields().get('from_url')
        wr = self.write
        wr('''
<div class="container" id="subhead-wrapper">
  <div class="container" id="subheader">
    <div class="row">
      <div class="col-md-3" id="social-media">
        <a href="http://www.acvaa.org/">acvaa.org</a>
        <a href="https://www.facebook.com/AmericanCollegeVeterinaryAnesthesiologists"><i class="fa fa-facebook-official"></i></a>
      </div>
      <div class="col-md-9" id="account-header">
            ''')
        if IS_LOGGED_IN:
            if acting_as(self.request()):
                wr('<span style="background-color: #F00; color: #FFF; font-weight: bold; padding: 2px 5px;">YOU ARE ACTING AS:</span> ')
            un = self.request().cookies().get('username')
            wr(un)
            wr('''
        <a class="btn btn-default btn-sm" href="/Account" role="button">Your Account</a>
        <a class="btn btn-default btn-sm" href="/Logout" role="button">Sign Out</a>
                ''')
        else:
            self.render_login_form()
        wr('''
      </div>

    </div><!-- .row -->
  </div>
</div><!-- #subhead-wrapper -->

            ''')

    def writeNav(self):
        ISA = is_site_admin(self.request())
        rolestr = self.request().cookies().get('role', '')
        IS_RES = rolestr == RESDSTR
        IS_DIP = rolestr == DIPLSTR
        PREV_SHOWN = False
        wr = self.writeln
        wr(rText(menu_alltop))
        if ISA:
            wr(rText(menu_admin))
        if (IS_LOGGED_IN and IS_DIP) or ISA:
            wr(rText(menu_dips))
        if (IS_LOGGED_IN and (IS_RES or IS_DIP)) or ISA:
            wr(rText(menu_cands))
        wr(rText(menu_allbottom))

    def writeContent(self):
        pass

    def writeFooter(self):
        wr = self.writeln
        wr('''
<div class="container" id="footer">
  <div class="row">
    <div class="col-md-9 col-md-offset-3">
      <P>
        <a href="/Terms">Terms of Use</a> &middot; <a href="mailto:execdir@acvaa.org">Need Help? Contact Us.</a>
      </P>
      <P class="legal">
        Copyright &copy; 1995&ndash;%s American College of Veterinary Anesthesia and Analgesia with all rights reserved.    </P>
      </P>
    </div><!-- .col-md-9 .col-md-offset-3 -->
  </div><!-- .row -->
</div><!-- #footer -->
            ''' % (get_year()))


###############################################################################

    def getCookieExpiry(self, cvtype, d=None, y=None):
        now = time.time()
        if d:
            expires = 60*60*24*int(d)
        if y:
            expires = 60*60*24*365.25*int(y)
        if cvtype == 'maxAge':
            return expires
        if cvtype == 'Expires':
            return time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.gmtime(now+expires))

    def setCookie(self, key, value, maxAge=None, Expires=None):
        cookie = Cookie(key, value)
        if maxAge:
            cookie.setMaxAge(maxAge)
        if Expires:
            cookie.setExpires(Expires)
        self.response().addCookie(cookie)

    def killCookie(self, key):
        self.response().delCookie(key)

###############################################################################
# Fetchers

    def get_from_url (self):
        from_url = 'http://%s%s' % (self.request()._environ.get('HTTP_HOST'), self.request()._environ.get('PATH_INFO'))
#        qs = self.request().fields()
#        if qs:
#            from_url += '?'
#            for a in qs.keys():
#                from_url += '%s=%s$' % (a, qs.get(a))
        return from_url

###############################################################################
# Renderers

    def render_login_form (self):
        wr = self.writeln
        wr('''
<div class="login">
  <form class="form-inline" method="POST" action="/Login_Attempt">''')
        if not self.request().fields().has_key('from_url'):
            wr(hidden('from_url', self.get_from_url()))
        else:
            wr(hidden('from_url', self.request().fields().get('from_url')))
        wr('''
    <div class="form-group">
      <label class="sr-only" for="username">Username</label>
      <input type="text" class="form-control" id="username" name="username" placeholder="Username">
    </div>
    <div class="form-group">
      <label class="sr-only" for="password">Password</label>
      <input type="password" class="form-control" id="password" name="password" placeholder="Password">
    </div>
    <input class="btn btn-orange btn-sm" type="submit" value="Sign In">
    <span class="sm"><a href="Login_Help">Help?</a></span>
  </form>
</div>
            ''')

    def render_form_error (self, errtype, errmsg):
        wr = self.writeln
        wr('<h1 class="error">%s</h1>' % (errtype))
        wr('<P>Here\'s why:</P>')
        wr('<h3>%s</h3>' % (errmsg))
        wr('<P>Please <a href="javascript:history.go(-1)">go back</a>, fix the problem &amp; try again.</P>')

    def render_special_msg (self, msg):
        wr = self.writeln
        wr('<div class="spcl_msg">')
        wr(msg)
        wr('</div>')

    def render_date_picker (self, YR, MO, DY, dname="date"):
        wr = self.writeln
        wr('<select name="%s" id="m" class="input">' % (dname))
        for i in range(1,13):
            self.write('<option value="%s"' % (i))
            if i == MO:
                self.write(' SELECTED')
            wr('>%s</option>' % (MONTHS.get(i)))
        wr('</select>')
        wr('<select name="%s" id="d" class="input">' % (dname))
        for i in range(1,32):
            self.write('<option value="%s"' % (i))
            if i == DY:
                self.write(' SELECTED')
            wr('>%s</option>' % (i))
        wr('</select>')
        wr('<select name="%s" id="y" class="input">' % (dname))
        for i in range(get_year()-1, get_year()+5):
            self.write('<option value="%s"' % (i))
            if i == YR:
                self.write(' SELECTED')
            wr('>%s</option>' % (i))
        wr('</select>')
        wr('<a href="#" id="date-pick"><img src="/g/calendar.png" alt="" width="16" height="16" border="0"></a>')


###############################################################################
# Emails

    def lydia (self):
        return '''
<script type="text/javascript">
<!--
document.write('<a href="&#109;&#97;&#105;&#108;&#116;&#111;&#58;'+'&#108;&#100;&#111;&#110;&#108;&#100;&#115;&#110;@'+'&#101;&#97;&#114;&#116;&#104;&#108;&#105;&#110;&#107;&#46;&#110;&#101;&#116;'+'">'+'&#68;&#114;&#46;&#32;&#68;&#111;&#110;&#97;&#108;&#100;&#115;&#111;&#110;'+'</a>');
//-->
</script>'''

    def steph (self):
        return '''
<script type="text/javascript"><!--
document.write('<a href="&#109;&#97;&#105;&#108;&#116;&#111;&#58;'+'&#115;&#109;&#104;&#97;&#109;&#105;@'+'&#118;&#116;&#46;&#101;&#100;&#117;'+'">'+'&#68;&#114;&#46;&#32;&#66;&#101;&#114;&#114;&#121;'+'</a>');
//-->
</script>'''

###############################################################################
# For unknown reasons, this widget stopped working. It would not load previous
# settings into the date pulldowns. Although code-wise, they were SELECTED,
# the javascript was undoing that & would only ever show today's date.
# Probably due to the "if not id" conditional.

    def writeCalPickJS(self, load_prev=False):
        wr = self.writeln
        wr('''
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
<script type="text/javascript" src="/js/jquery-2.1.3.min.js"></script>
<script type="text/javascript" src="/js/jquery.cookie.js"></script>
<script type="text/javascript" src="/js/bootstrap.min.js"></script>
<script type="text/javascript" src="/js/acva.js"></script>
<script type="text/javascript" src="/js/jquery.bgiframe.min.js"></script>
<script type="text/javascript" src="/js/date.js"></script>
<script type="text/javascript" src="/js/jquery-ui.min.js"></script>
<!--[if lt IE 9]>
<script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
<script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
<![endif]-->
<script>
$(function() {
  $( "#datepicker" ).datepicker();
});
</script>
            ''')
    def writeCalPickCSS(self):
        wr = self.writeln
        wr('''
<link rel="shortcut icon" href="/g/favicon.ico" type="image/x-icon" />
<link rel="stylesheet" href="/c/bootstrap.min.css" type="text/css">
<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">
<link rel="stylesheet" href="/c/jquery-ui.min.css" type="text/css">
<link rel="stylesheet" href="/c/acva.css" type="text/css">
<link rel="stylesheet" href="/c/cal_picker.css" type="text/css">
<link rel="stylesheet" href="/c/acvaa_bootstrap.css" type="text/css">
            ''')
