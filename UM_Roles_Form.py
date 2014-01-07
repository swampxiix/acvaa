from Template_Admin import Template_Admin

from z_account import get_user_acct, save_user_roles
from z_constants import ALL_ROLES
from z_forms import checkbox, hidden, submit

class UM_Roles_Form (Template_Admin):

    def title(self):
        return 'ACVAA: Edit User Roles'

    def writeContent(self):
        wr = self.writeln
        qs = self.request().fields()
        username = qs.get('u')

        if self.request().cookies().get('username') == username:
            wr('<h1 class="error">You cannot manage your own account.</h1>')
            wr('<P>This is to keep you from accidentally deleting your account, or revoking your own administrative privileges.')
        elif username == 'master':
            wr('<h1 class="error">You cannot manage the master account.</h1>')
            wr('<P>This is to keep you from accidentally revoking the site developer\'s access.')

        else:
            wr('<h1>%s</h1>' % (self.title()))
            wr('<h1><em>%s</em></h1>' % (username))
            ud = get_user_acct(username)

            if self.request()._environ.get('REQUEST_METHOD') == 'POST':
                form = qs
                if form.get('roles'):
                    save_user_roles(form.get('u'), form.get('roles'))
                    self.response().sendRedirect('UM_Index?rolok=%s' % (username))

                else:
                    wr('<h1 class="error">A user account must have at least one role specified.</h1>')
                    wr('<P>Please <a href="javascript:history.go(-1)">go back</a> &amp; try again.</P>')

            else:
                wr('<form method="POST" action="UM_Roles_Form">')
                wr(hidden('u', username))
                wr('<P><table>')
                for r in ALL_ROLES:
                    wr('<tr>')
                    wr('<td class="t14">')
                    wr(r.capitalize())
                    wr('<td class="t14">')
                    wr(checkbox('roles', r, (r in ud.get('roles')) ))
                wr('</table></P>')
                wr(submit('Save'))
                wr('<input type="button" value="Never mind. Leave roles alone." onclick="javascript:history.go(-1)">')
                wr('</form>')
