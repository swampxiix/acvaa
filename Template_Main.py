from WebKit.Page import Page
from WebKit.Cookie import Cookie

from z_account import is_logged_in, is_site_admin, acting_as
from z_constants import DIPLSTR, RESDSTR, MONTHS
from z_forms import text, passwd, hidden, submit
from z_times import get_year

import time

class Template_Main(Page):
    def writeDocType(self):
        self.writeln('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"'
            '"http://www.w3.org/TR/html4/strict.dtd">')

    def writeStyleSheet(self):
        self.writeln('<link rel="shortcut icon" href="/g/favicon.ico" type="image/x-icon" />')
        self.writeln('<link rel="stylesheet" href="/c/reset-fonts-grids.css" type="text/css">')
        self.writeln('<link rel="stylesheet" href="/c/acva.css" type="text/css">')

    def writeJavaScript(self):
#        self.writeln('<script type="text/javascript" src="/js/jquery-1.3.2.min.js"></script>')
        self.writeln('<script type="text/javascript" src="/js/jquery-1.4.2.min.js"></script>')
        self.writeln('<script type="text/javascript" src="/js/jquery.cookie.js"></script>')
        self.writeln('<script type="text/javascript" src="/js/acva.js"></script>')

    def writeBody(self):
        wr = self.writeln
        wr('<body>')
        self.writeBodyParts()
        # This is where google analytics stuff goes!
        wr('</body>')

    def writeBodyParts(self):
        wr = self.writeln
        self.writeHeader()
        wr('<div id="doc2" class="yui-t1">')
        wr('<div id="bd" role="main">')
        wr('<div id="yui-main">')
        wr('<div class="yui-b">')
        wr('<div class="yui-g">')
#        if IS_LOGGED_IN:
#            un = self.request().cookies().get('username')
#            wr('<h3>Welcome back.</h3>')
#            wr('<P>You are currently logged in as <b>%s</b>. Among other things, you can <a href="Account">access your account</a> or <a href="Logout">log out</a>.</P>' % (un))
#        else:
#        if not IS_LOGGED_IN: # MOVED TO HORIZONTAL HEADER AREA see writeGlobalNav()
#            wr('<div class="sb"><div class="st">')
#            self.render_login_form()
#            wr('</div></div>')

        self.writeContent()
        wr('</div><!-- .yui-g -->')
        wr('</div><!-- .yui-b -->')
        wr('</div><!-- #yui-main -->')
        self.writeNav()
        wr('</div><!-- #bd -->')
        self.writeFooter()
        wr('</div><!-- #doc2 .yui-t1 -->')


    def writeHeader(self):
        IS_LOGGED_IN = is_logged_in(self.request())
        global IS_LOGGED_IN
        wr = self.writeln
        wr('<div id="doc2" class="yui-t1 logoplace">')
        wr('<a href="/Index" title="ACVAA Homepage"><img src="/g/header.png" alt="Header Image" width="948" height="184" border="0"></a>')
        wr('</div><!-- #doc2 .yui-t1 -->')
        self.writeGlobalNav()

    def writeGlobalNav(self):
        if not self.request().fields().has_key('from_url'):
            from_url = self.get_from_url()
        else:
            from_url = self.request().fields().get('from_url')
        wr = self.write
        wr('<div id="stripes">')
        wr('<div id="whitestripe">')
        wr('<div id="doc2" class="yui-t1">')
        if IS_LOGGED_IN:
            wr('<div class="button b2">')
            wr('<a href="/Logout">Log Out</a>')
            wr('</div>')
            wr('<div class="button b2">')
            wr('<a href="/Account">Your Account</a>')
            wr('</div>')
            un = self.request().cookies().get('username')
            wr('<div class="flt_r" style="padding: 3px 5px; margin-top: 2px;">')
            if acting_as(self.request()):
                wr('<span style="background-color: #F00; color: #FFF; font-weight: bold; padding: 2px 5px;">YOU ARE ACTING AS:</span> ')
            wr('%s</div>' % un)
        else:
            self.render_login_form()
        wr('<a href="/Index" title="ACVAA Homepage"><img src="/g/acva.png" alt="acvaa.org" width="172" height="32" border="0"></a>')
        wr('</div><!-- #doc2 .yui-t1 -->')
        wr('</div><!-- #whitestripe -->')
        wr('</div><!-- #stripes -->')

    def writeNav(self):
        ISA = is_site_admin(self.request())
        rolestr = self.request().cookies().get('role', '')
        IS_RES = rolestr == RESDSTR
        IS_DIP = rolestr == DIPLSTR
        PREV_SHOWN = False

        wr = self.writeln
        wr('<div class="yui-b">')

        wr('<a href="/Index" class="menu_link mlm">Home</a>')

        wr('<div class="menu_section" id="menu_about">')
        wr('<div class="menu_head mh_expanded">')
        wr('About the ACVAA')
        wr('</div>')
        wr('<div class="menu_links">')
        wr('<a href="/Mission_Statement" class="menu_link">Mission Statement</a>')
        wr('<a href="/docs/History" class="menu_link">History of the ACVAA</a>')
        wr('<a href="/Constitution" class="menu_link">Constitution &amp; Bylaws</a>')
        wr('<a href="/Foundation/" class="menu_link">The ACVAA Foundation</a>')
        wr('<span style="color: #324150; font-weight: bold;">Standards</span>')
        wr('<a style="padding-left: 5px;" href="/docs/Position_Statements" class="menu_link">Position Statements</a>')
        wr('<a style="padding-left: 5px;" href="/docs/ACVA_Training_Standards_2009.doc" class="menu_link">Residency Training Standards</a>')
        wr('</div>')
        wr('</div>')

        wr('<a href="/Directory" class="menu_link mlm">Member Directory</a>')
        wr('<a href="/News" class="menu_link mlm">News</a>')
        wr('<a href="/Calendar" class="menu_link mlm">Events Calendar</a>')
        wr('<a href="/Jobs" class="menu_link mlm">Employment Opportunities</a>')

        if ISA:
            wr('<div class="menu_section" id="menu_admin">')
            wr('<div class="menu_head mh_expanded">')
            wr('Administration')
            wr('</div>')
            wr('<div class="menu_links">')
            wr('<a href="/UM_Index" class="menu_link">Manage Users</a>')
            # Events mgmt. is here until SHB decides ppl other than admins can add them.
            wr('<a href="/Events" class="menu_link">Manage Events</a>')
            wr('</div>')
            wr('</div>')

        if (IS_LOGGED_IN and IS_DIP) or ISA:
            PREV_SHOWN = True
            wr('<div class="menu_section" id="menu_dips">')
            wr('<div class="menu_head mh_expanded">')
            wr('Diplomates')
            wr('</div>')
            wr('<div class="menu_links">')
            wr('<a href="/Account" class="menu_link">Your Account</a>')
            wr('<a href="/Annual" class="menu_link">2012 Annual Meeting</a>')
            wr('<a href="/Action" class="menu_link">Action Items</a>')
#            if ISA:
#                wr('<a href="/Events" class="menu_link">Manage Events</a>')
            wr('<a href="/BOD" class="menu_link">Board of Directors</a>')
            wr('<a href="/Committees" class="menu_link">Committees</a>')
            wr('<a href="/Reports" class="menu_link">Annual Reports</a>')
            wr('<a href="/Documents?cat=diplomates" class="menu_link">Documents &amp; Forms</a>')
            wr('</div>')
            wr('</div>')

        if (IS_LOGGED_IN and (IS_RES or IS_DIP)) or ISA:
            wr('<div class="menu_section" id="menu_cans">')
            wr('<div class="menu_head mh_expanded">')
            wr('Candidates')
            wr('</div>')
            wr('<div class="menu_links">')
            if not PREV_SHOWN:
                wr('<a href="/Account" class="menu_link">Your Account</a>')
                if ISA:
                    wr('<a href="/Events" class="menu_link">Manage Events</a>')
            wr('<a href="/docs/Welcome" class="menu_link">Welcome to the ACVAA</a>')
            wr('<a href="/Documents?cat=candidates" class="menu_link">Documents &amp; Forms</a>')
            wr('</div>')
            wr('</div>')

        wr('<div class="menu_section" id="menu_vets">')
        wr('<div class="menu_head mh_expanded">')
        wr('Veterinarians')
        wr('</div>')
        wr('<div class="menu_links">')
        wr('<a href="/docs/Small_Animal_Monitoring_2009.doc" class="menu_link">Small Animal Monitoring Guidelines</a>')
        wr('<a href="/docs/Equine" class="menu_link">Equine Anesthesia Guidelines</a>')
        wr('<a href="/docs/Residency_Programs" class="menu_link">Anesthesia Residency Programs</a>')
        wr('<a href="/Directory?consult=true" class="menu_link">Consultants for Hire</a>')
        wr('<a href="/Speaker" class="menu_link">Need an ACVAA Speaker?</a>')
        wr('</div>')
        wr('</div>')

        wr('<div class="menu_section" id="menu_owners">')
        wr('<div class="menu_head mh_expanded">')
        wr('Pet Owners')
        wr('</div>')
        wr('<div class="menu_links">')
        wr('<a href="/Owners" class="menu_link">Care for your Pet</a>')
#        wr('<a href="/Locator" class="menu_link">Find a Doctor</a>')
        wr('<a href="/Locator" class="menu_link">Find an Anesthesiologist</a>')
        wr('</div>')
        wr('</div>')

        wr('<a href="/Links" class="menu_link mlm">Links to Other Sites</a>')

        wr('<div class="menu_section">')
        wr('<a href="https://www.facebook.com/AmericanCollegeVeterinaryAnesthesiologists"><img src="/g/facebook.png" alt="Facebook" title="Facebook" border="0"></a>')
        wr('</div>')


        if IS_LOGGED_IN:
            wr('<a href="/Logout" class="menu_link mlm">Log Out</a>')

        wr('</div><!-- .yui-b -->')

#        g = self.request().cookies().get('g')
#        if g == 'd':
#            if (IS_LOGGED_IN and IS_DIP) or ISA:
#                self.render_dipl_menu()
#        if g == 'r':
#            if (IS_LOGGED_IN and (IS_RES or IS_DIP)) or ISA:
#                self.render_resd_menu()
#        if (not g) or g == 'v':
#            self.render_vet_menu()
#        if (not g) or g == 'p':
#            self.render_owner_menu()


    def writeContent(self):
        pass

    def writeFooter(self):
        wr = self.writeln
        wr('<div id="ft" role="contentinfo">')
        wr('<p>Copyright &copy; 1995&ndash;%s American College of Veterinary Anesthesia and Analgesia with all rights reserved.<br />' % (get_year()))
        wr('<a href="Terms">Terms of Use</a> &middot; <a href="mailto:execdir@acva.org">Contact</a></p>')
        wr('</div><!-- #ft -->')

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
        wr('<form method="POST" action="/Login_Attempt">')
        wr('<div class="login">')
        if not self.request().fields().has_key('from_url'):
            wr(hidden('from_url', self.get_from_url()))
        else:
            wr(hidden('from_url', self.request().fields().get('from_url')))
        wr('Username: ')
        wr(text('username', clss='input'))
        wr(' Password: ')
        wr(passwd('password', clss='input'))
        wr('<input type="submit" class="button b2" value="Sign In" style="float: none;">')
        wr('<span class="sm"><a href="Login_Help">Help?</a></span>')
        wr('</div>')
        wr('</form>')

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
        wr('<script type="text/javascript" src="/js/jquery-1.3.2.min.js"></script>')
        wr('<script type="text/javascript" src="/js/acva.js"></script>')

        wr('<script type="text/javascript" src="/js/jquery.bgiframe.min.js"></script>')
        wr('<script type="text/javascript" src="/js/date.js"></script>')
        wr('<script type="text/javascript" src="/js/jquery.datePicker.js"></script>')
        wr('<script type="text/javascript">')
        wr('''
$(function()
{
	
	// initialise the "Select date" link
	$('#date-pick')
		.datePicker(
			// associate the link with a date picker
			{
				createButton:false,
				startDate:'01/01/%s',
				endDate:'31/12/%s'
			}
		).bind(
			// when the link is clicked display the date picker
			'click',
			function()
			{
				updateSelects($(this).dpGetSelected()[0]);
				$(this).dpDisplay();
				return false;
			}
		).bind(
			// when a date is selected update the SELECTs
			'dateSelected',
			function(e, selectedDate, $td, state)
			{
				updateSelects(selectedDate);
			}
		).bind(
			'dpClosed',
			function(e, selected)
			{
				updateSelects(selected[0]);
			}
		);
		
	var updateSelects = function (selectedDate)
	{
		var selectedDate = new Date(selectedDate);
		$('#d option[value=' + selectedDate.getDate() + ']').attr('selected', 'selected');
		$('#m option[value=' + (selectedDate.getMonth()+1) + ']').attr('selected', 'selected');
		$('#y option[value=' + (selectedDate.getFullYear()) + ']').attr('selected', 'selected');
	}
	// listen for when the selects are changed and update the picker
	$('#d, #m, #y')
		.bind(
			'change',
			function()
			{
				var d = new Date(
							$('#y').val(),
							$('#m').val()-1,
							$('#d').val()
						);
				$('#date-pick').dpSetSelected(d.asString());
			}
		);
            ''' % (get_year()-1, get_year()+5))

#        id = self.request().fields().get('id')
        if not load_prev: # only load default (today) if add, not edit
            wr('''

	// default the position of the selects to today
	var today = new Date();
	updateSelects(today.getTime());
	
	// and update the datePicker to reflect it...
	$('#d').trigger('change');
            ''')
        wr('''
});
            ''')

        wr('</script>')

    def writeCalPickCSS(self):
        self.writeln('<link rel="shortcut icon" href="/g/favicon.ico" type="image/x-icon" />')
        self.writeln('<link rel="stylesheet" href="/c/reset-fonts-grids.css" type="text/css">')
        self.writeln('<link rel="stylesheet" href="/c/acva.css" type="text/css">')
        self.writeln('<link rel="stylesheet" href="/c/cal_picker.css" type="text/css">')