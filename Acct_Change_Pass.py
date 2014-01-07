from Template_Authenticated import Template_Authenticated

from z_account import change_password

class Acct_Change_Pass (Template_Authenticated):

    def writeContent(self):
        wr = self.writeln
        if self.request()._environ.get('REQUEST_METHOD') == 'POST':
            C = self.request().cookies()
            un, hash = C.get('username'), C.get('hash')
            form = self.request().fields()
            ERROR = None
            if (un == form.get('form_username')) and (hash == form.get('form_hash')):
                if form.get('pw1') == form.get('pw2'):
                    change_password(un, form.get('pw1'))
                else:
                    ERROR = 'The passwords you entered are not the same.'
            else:
                ERROR = 'Credentials failure.'

            if ERROR:
                self.render_form_error('Form Error', ERROR)
            else:
                self.response().sendRedirect('Account?pc=1')


