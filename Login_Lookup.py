from Template_Main import Template_Main

from z_account import get_user_acct, reset_password

class Login_Lookup (Template_Main):

    def writeContent(self):
        wr = self.writeln
        req = self.request()
        form = req.fields()

        if self.request()._environ.get('REQUEST_METHOD') == 'POST':
            username = form.get('username')
            p = get_user_acct(username)
            email = p.get('email')
            if email:
                reset_password(username)

            wr('<h1>Please Check Your Email</h1>')
            wr('<P>You should receive a new message from us with your account\'s new password.</P>')
            wr('<P>If not, then something\'s gone wrong; please contact an ACVAA site administrator.</P>')

        else:
            wr('<h1>You do not have permission to access this page.</h1>')

