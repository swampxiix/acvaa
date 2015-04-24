from Template_Main import Template_Main

from z_account import check_email_address, is_email_registered, \
    save_registration, get_user_acct, hash_string, get_user_role

from z_constants import STATES, HARV_DIPL, HARV_RESD, COUNTRY_SELECT
from z_forms import hidden, text, select, passwd, radio, radio_jq

class Register (Template_Main):

    def writeNav(self):
        wr = self.writeln
        wr('''
<div class="menu_links">
  <h2>Need Help?</h2>
  <P>
    If you have problems registering &amp; can\'t figure out where things are going awry, please <a href="mailto:execdir@acvaa.org">contact us</a>.
  </P>
</div>
            ''')

    def title(self):
        return 'ACVAA Site Registration'

    def writeContent(self):
        wr = self.writeln
        qs = self.request().fields()
        wr('<h1>%s</h1>' % (self.title()))

        harvest_code = qs.get('hc')
        if harvest_code == HARV_DIPL:
            acct_type = 'Diplomate'
        elif harvest_code == HARV_RESD:
            acct_type = 'Candidate'

        if self.request()._environ.get('REQUEST_METHOD') == 'POST':
            form = self.request().fields()
            ERROR = None
            required = {'hc': 'validation code', 'fn': 'first name', 'sn': 'surname', 'city': 'city', 'state': 'state', 'email': 'email', 'pw1': 'first password', 'pw2': 'second password'}
            for r in required.keys():
                if not form.get(r):
                    ERROR = 'The field "%s" is required.' % (required.get(r))
            if form.get('pw1') != form.get('pw2'):
                ERROR = 'The two passwords you entered are not the same.'
            if not ERROR:
                ERROR = check_email_address(form.get('email'))
            if not ERROR:
                if is_email_registered(form.get('email')):
                    ERROR = 'We already have an account that uses the email address: %s.' % (form.get('email'))

            if ERROR:
                self.render_form_error('Registration Error', ERROR)
            else:
                newid = save_registration(form)

                # Auto Login
                userinfo = get_user_acct(newid)
                hvc = hash_string(userinfo.get('vcode'))
                ex1 = self.getCookieExpiry('maxAge', y=10)
                ex2 = self.getCookieExpiry('Expires', y=10)
                self.setCookie('username', newid, ex1, ex2)
                self.setCookie('hash', hvc, ex1, ex2)
                possible_role = get_user_role(newid)
                if possible_role:
                    self.setCookie('role', possible_role, ex1, ex2)

                wr('<h2>Success!</h2>')
                wr('<P>Your ACVAA %s account has been created. Your site user name is:</P>' % (acct_type))
                wr('<h3>%s</h3>' % (newid))
                wr('''
<P><em>IMPORTANT!</em> Don\'t lose your user name.</P>

<P>An email confirming your account registration will be sent ASAP; it will also include your site user name.</P>

<p>
You are now logged in. You can:
</p>

<p>
<a href="Account">Manage your account</a><br />
You can also change your privacy settings here.
</p>

<p>
<a href="Directory">View the member directory</a>
</p>

<p>
<a href="Calendar">Check out the events calendar</a>
</p>
                    ''')

        else:
            if harvest_code and (harvest_code in [HARV_DIPL, HARV_RESD]):
                wr('<div class="sb"><div class="st">')
                wr('<h3>Note</h3>')
                wr('<P>Submitting this form will create a new %s account for you on the ACVAA site.</P>' % (acct_type))
                wr('<P>Please provide as much information as possible; you can specify your privacy settings as you go.</P>')
                wr('</div></div>')
                wr('<form method="POST" action="Register">')
                wr(hidden('hc', harvest_code))
                wr('<h2>%s</h2>' % (acct_type))
                wr('<P><table id="contact_info">')
                wr('<tr><td colspan="3">')
                wr('<fieldset>')
                wr('<legend>Tell us about you.</legend>')
                wr('<tr><td colspan="3">This information will be available to the public.')
                wr('<tr><td><label>First Name</label>')
                wr('<td>%s' % (text('fn', '', clss='input')))
                wr('<td class="req">required')
                wr('<tr><td><label>Middle Initial</label>')
                wr('<td>%s' % (text('mi', '', clss='input', size='2')))
                wr('<tr><td><label>Last Name</label>')
                wr('<td>%s' % (text('sn', '', clss='input')))
                wr('<td class="req">required')
                wr('<tr><td><label>Degrees Held</label>')
                wr('<td>%s' % (text('degrees', '', clss='input', size='6')))
                wr('<td class="hint">(e.g., Ph.D., MBA, MS, etc.)')
                wr('</fieldset>')
                wr('<tr><td colspan="3">')
                wr('<fieldset>')
                wr('<legend>Where are you located?</legend>')
                wr('<tr><td><label>Country</label>')
                wr('<td>%s' % (COUNTRY_SELECT))
                wr('<td class="req">required')
                wr('<tr><td><label>Address 1</label>')
                wr('<td>%s' % (text('addr1', '', clss='input')))
                wr('<tr><td><label>Address 2</label>')
                wr('<td>%s' % (text('addr2', '', clss='input')))
                wr('<tr><td><label>City</label>')
                wr('<td>%s' % (text('city', '', clss='input')))
                wr('<td class="req">required')
                wr('<tr><td><label>State/Prov.</label>')
                wr('<td id="state_slot">')
                wr('<td class="req">required')
                wr('<tr><td><label>ZIP/Postal Code</label>')
                wr('<td>%s' % (text('zip', '', clss='input', size='6')))
                wr('<tr><td colspan="3">Who should be allowed to view your full address?')
                # radio_jq (name, value='', clss='', id='', checked=False)
                wr('<tr><td><td colspan="2">')
                wr('''
                    <label for="hide1">
                    %s
                    Nobody; show only my city &amp; state
                    </label><br />
                    ''' % (radio_jq('show_address', 'hide', '', 'hide1', checked=True)))
                wr('''
                    <label for="dips1">
                    %s
                    ACVAA Diplomates only
                    </label><br />
                    ''' % (radio_jq('show_address', 'diplomates', '', 'dips1', checked=False)))
                wr('''
                    <label for="both1">
                    %s
                    ACVAA Diplomates &amp; Candidates
                    </label><br />
                    ''' % (radio_jq('show_address', 'both', '', 'both1', checked=False)))
                wr('''
                    <label for="all1">
                    %s
                    Everyone, even the general public
                    </label>
                    ''' % (radio_jq('show_address', 'all', '', 'all1', checked=False)))
                wr('</fieldset>')
                wr('<tr><td colspan="3">')
                wr('<fieldset>')
                wr('<legend>How can you be contacted?</legend>')
                wr('<tr><td><label>Email</label>')
                wr('<td>%s' % (text('email', '', clss='input')))
                wr('<td class="req">required')
                wr('<tr><td colspan="3">Who should be allowed to view your email address?')
                wr('<tr><td><td colspan="2">')
                wr('''
                    <label for="hide2">
                    %s
                    Nobody
                    </label><br />
                    ''' % (radio_jq('show_email', 'hide', '', 'hide2', checked=True)))
                wr('''
                    <label for="dips2">
                    %s
                    ACVAA Diplomates only
                    </label><br />
                    ''' % (radio_jq('show_email', 'diplomates', '', 'dips2', checked=False)))
                wr('''
                    <label for="both2">
                    %s
                    ACVAA Diplomates &amp; Candidates
                    </label><br />
                    ''' % (radio_jq('show_email', 'both', '', 'both2', checked=False)))
                wr('''
                    <label for="all2">
                    %s
                    Everyone, even the general public
                    </label>
                    ''' % (radio_jq('show_email', 'all', '', 'all2', checked=False)))
                wr('<tr><td><label>Phone</label>')
                wr('<td>%s' % (text('phone', '', clss='input')))
                wr('<tr><td><label>Fax</label>')
                wr('<td>%s' % (text('fax', '', clss='input')))
                wr('<tr><td colspan="3">Who should be allowed to view your phone &amp; fax numbers?')
                wr('<tr><td><td colspan="2">')
                wr('''
                    <label for="hide3">
                    %s
                    Nobody
                    </label><br />
                    ''' % (radio_jq('show_numbers', 'hide', '', 'hide3', checked=True)))
                wr('''
                    <label for="dips3">
                    %s
                    ACVAA Diplomates only
                    </label><br />
                    ''' % (radio_jq('show_numbers', 'diplomates', '', 'dips3', checked=False)))
                wr('''
                    <label for="both3">
                    %s
                    ACVAA Diplomates &amp; Candidates
                    </label><br />
                    ''' % (radio_jq('show_numbers', 'both', '', 'both3', checked=False)))
                wr('''
                    <label for="all3">
                    %s
                    Everyone, even the general public
                    </label>
                    ''' % (radio_jq('show_numbers', 'all', '', 'all3', checked=False)))
                wr('<tr><td colspan="3">')
                wr('<fieldset>')
                wr('<legend>Choose a password &amp; enter it twice.</legend>')
                wr('<tr><td><label>Password</label>')
                wr('<td>%s' % (passwd('pw1', '', clss='input')))
                wr('<td class="req">required')
                wr('<tr><td><label>Password</label>')
                wr('<td>%s' % (passwd('pw2', '', clss='input')))
                wr('<td class="req">required')
                wr('</fieldset>')
                wr('<tr><td><td colspan="2">')
                wr('<input type="image" src="/g/create_acct_button.png" style="margin-top: 20px;">')
                wr('</table></P>')
                wr('</form>')
            else:
                wr('''<h1 class="error">Validation Error</h1>
                <P>
                Sorry, but you cannot register with the ACVAA site unless you
                use a web address with a proper validation code.
                <em>This is most likely due to the web address having been
                mistyped.</em>
                </P>
                <P>
                Please use only the address provided in the email from ACVAA.
                <em>Copying &amp; pasting the address into your browser is the
                easiest way to avoid mistakes.</em>
                </P>
                <P>
                If you have further problems or questions, please contact
                %s or %s.
                </P>''' % (self.lydia(), self.steph()))
