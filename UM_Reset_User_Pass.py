from Template_Admin import Template_Admin

from z_forms import hidden, submit
from z_account import reset_password

class UM_Reset_User_Pass (Template_Admin):

    def title(self):
        return 'ACVAA: Reset User Password'

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
    
            if self.request()._environ.get('REQUEST_METHOD') == 'POST':
                form = self.request().fields()
                username = qs.get('u')
                reset_password(username)
                wr('<P>An email containing a new password has been sent to this user.</P>')
    
            else:
                wr('<P>Are you sure you want to reset the password for user account: %s?</P>' % (username))
                wr('<form method="POST" action="UM_Reset_User_Pass">')
                wr(hidden('u', username))
                wr('<P>')
                wr(submit('Yes'))
                wr('<input type="button" value="No, I\'ve made an error in judgment!" onclick="javascript:history.go(-1)">')
                wr('</P>')
                wr('</form>')
