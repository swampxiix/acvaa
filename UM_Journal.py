from Template_Admin import Template_Admin

from z_account import get_all_users
from z_forms import submit
from z_wiley import get_journal_access, set_journal_access

class UM_Journal (Template_Admin):

    def title(self):
        return 'ACVAA: Journal Access Management'

    def writeContent(self):
        wr = self.writeln
        wr('<h1>%s</h1>' % (self.title()))
        form = self.request().fields()

        if self.request()._environ.get('REQUEST_METHOD') == 'POST':
            set_journal_access(form)
            self.response().sendRedirect('UM_Journal?saved=1')

        else:
            if form.get('saved'):
                self.render_special_msg('Journal access settings saved.')
            JOURNALIST = get_journal_access()
            if not JOURNALIST:
                JOURNALIST = []
            all = get_all_users()
            aks = all.keys()
            aks = sorted(aks, key=lambda x: (x.isdigit() and float(x)) or x.lower())

            wr('<form action="UM_Journal" method="POST">')
            wr('<table>')
            wr('<tr>')
            wr('<th>Name')
            wr('<th colspan="2">Allow Journal Access')

            count = 0
            for ak in aks:
                count += 1
                ud = all[ak]
                username = ud.get('username')
                wr('<tr class="c"')
                if not count % 3:
                    wr('style="background-color: #E0E0E0;"')
                wr('>')

                wr('<td class="t12">%s, %s' % ( ud.get('sn'), ud.get('fn') ))
                wr('<td>')
                wr('<label for="%s_journal_yes"><input type="radio" name="%s" id="%s_journal_yes" value="yes"' % (username, username, username))
                if username in JOURNALIST:
                    wr(' checked="checked"')
                wr('> Yes</label>')
                wr('<td>')
                wr('<label for="%s_journal_no"><input type="radio" name="%s" id="%s_journal_no" value="no"' % (username, username, username))
                if username not in JOURNALIST:
                    wr(' checked="checked"')
                wr('> No</label>')
            wr('<tr><td colspan="3" style="text-align: center;">')
            wr('%s' % (submit('Save Journal Access Settings')))
            wr('</table>')
            wr('</form>')
