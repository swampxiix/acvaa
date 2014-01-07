from Template_Authenticated import Template_Authenticated

from z_account import get_user_acct
from z_constants import STATES
from z_forms import text, select, hidden, passwd, submit

class Account_Form (Template_Authenticated):
    def title(self):
        un = self.request().cookies().get('username')
        global un
        return '%s Account Information' % (un)

    def writeContent(self):
        wr = self.writeln
        qs = self.request().fields()
        if self.request()._environ.get('REQUEST_METHOD') == 'POST':
            form = self.request().fields()
            wr(form)
        else:
            wr('<h1><em>%s</em> Account Information</h1>' % (un))

            p = get_user_acct(un)

            wr('<P>You can make changes to your account information here.</P>')

            wr('<form method="POST" action="Account">')
            wr('<table id="contact_info">')

            wr('<tr><td colspan="3">')
            wr('<fieldset>')
            wr('<legend>Tell us about you.</legend>')
            wr('<tr><td><label>Salutation</label>')
            wr('<td>%s' % (text('salute', p.get('salute', ''), clss='input', size='5')))
            wr('<td class="hint">(e.g., Dr., Mr., Ms., etc.)')
            wr('<tr><td><label>First Name</label>')
            wr('<td>%s' % (text('fn', p.get('fn', ''), clss='input')))
            wr('<td class="req">required')
            wr('<tr><td><label>Middle Initial</label>')
            wr('<td>%s' % (text('mi', p.get('mi', ''), clss='input', size='2')))
            wr('<tr><td><label>Last Name</label>')
            wr('<td>%s' % (text('sn', p.get('sn', ''), clss='input')))
            wr('<td class="req">required')
            wr('</fieldset>')

            wr('<tr><td colspan="3">')
            wr('<fieldset>')
            wr('<legend>Where are you located?</legend>')
            wr('<tr><td><label>Address 1</label>')
            wr('<td>%s' % (text('addr1', p.get('addr1', ''), clss='input')))
            wr('<tr><td><label>Address 2</label>')
            wr('<td>%s' % (text('addr2', p.get('addr2', ''), clss='input')))
            wr('<tr><td><label>City</label>')
            wr('<td>%s' % (text('city', p.get('city', ''), clss='input')))
            wr('<td class="req">required')
            wr('<tr><td><label>State</label>')
            wr('<td>%s' % (select (name='state', opts=STATES, selected=p.get('state', ''), clss='input')))
            wr('<td class="req">required')
            wr('<tr><td><label>ZIP Code</label>')
            wr('<td>%s' % (text('zip', p.get('zip', ''), clss='input', size='6')))
            wr('</fieldset>')

            wr('</table>')
            wr('</form>')
